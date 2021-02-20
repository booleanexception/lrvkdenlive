#!/usr/bin/env python3

import hashlib # for md5
import os # for listdir
import sys # for args
import shutil # for copy2
import pwd # for OS username


#where to copy the files, should be ok
to_path = "/home/"+pwd.getpwuid(os.getuid()).pw_name+"/.cache/kdenlive/proxy"


if len(sys.argv) != 2:
    print("Syntax: lrvkdenlive /from/path/ /to/path/")
    print("- GoPro LRV to kdenlive proxy clips")
    print("- Copies GoPros Low Resolution Video files to the Proxy Clips folder of the FOSS video editing software kdenlive")
    exit()

from_path = sys.argv[1]


for path, subdirs, files in os.walk(from_path):
    for file in files:

        if not file.endswith(".LRV"):
            continue

        lrv_file = path+"/"+file
        mp4_file = path+"/"+(file[:-3]+"MP4")

        if not os.path.isfile(mp4_file):
            print("[0.1] found LRV, but "+mp4_file+" does not exist in same folder?")
            continue

        filesize = os.stat(mp4_file).st_size

        if filesize <= 2000000:
            print("[0.2] "+mp4_file+" is too small, skipping")
            continue

        with open(mp4_file, "rb") as f:
            fdata = f.read(1000000)
            
            f.seek(filesize - 1000000)
            fdata += f.read(1000000)
            
            result = hashlib.md5(fdata)

        hash = result.hexdigest()

        proxy_file = to_path+"/"+hash+".mkv"

        if os.path.isfile(proxy_file):
            print("[1.1] "+mp4_file+" already proxied")
            continue

        print("[2] >>> Copying "+lrv_file+" -> "+proxy_file)
        shutil.copy2(lrv_file, proxy_file)