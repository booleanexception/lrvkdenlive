#!/usr/bin/env python3

import hashlib
import os
import sys
import shutil

to_path = "/home/basel/.cache/kdenlive/proxy"


if len(sys.argv) != 2:
    print("Syntax: lrvkdenlive /from/path/ /to/path/")
    print("- GoPro LRV to kdenlive proxy clips")
    print("- Copies GoPros Low Resolution Video files to the Proxy Clips folder of the FOSS video editing software kdenlive")
    exit()

from_path = sys.argv[1]

for file in os.listdir(from_path):
    if not file.endswith(".LRV"):
        print("[0.0] "+file+" is no LRV")
        continue

    lrv_file = from_path+file
    mp4_file = from_path+file[:-3]+"MP4"

    if not os.path.isfile(mp4_file):
        print("[0.1] "+mp4_file+" does not exist")
        continue

    filesize = os.stat(mp4_file).st_size

    if filesize <= 2000000:
        print("[0.2] "+mp4_file+" is too small")
        continue

    with open(mp4_file, "rb") as f:
        fdata = f.read(1000000)
        
        f.seek(filesize - 1000000)
        fdata += f.read(1000000)
        
        result = hashlib.md5(fdata)

    hash = result.hexdigest()

    print("[1] "+mp4_file+" has hash: "+hash)

    proxy_file = to_path+"/"+hash+".mkv"

    print("[2] Copying "+lrv_file+" -> "+proxy_file)
    shutil.copy2(lrv_file, proxy_file)