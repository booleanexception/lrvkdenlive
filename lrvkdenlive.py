#!/usr/bin/env python3

import hashlib # for md5
import sys # for args
import shutil # for copy2

from pathlib import Path

#where to copy the files, should be ok
to_path = Path(Path.home() / ".cache/kdenlive/proxy")


if len(sys.argv) != 2:
    print("Syntax: lrvkdenlive /from/path/ ")
    print("- GoPro LRV to kdenlive proxy clips")
    print("- Copies GoPros Low Resolution Video files to the Proxy Clips folder of the FOSS video editing software kdenlive")
    exit()

from_path = Path(sys.argv[1])

for lrv_file in from_path.glob('*.LRV'):
    mp4_file = next(lrv_file.parent.glob('*' + lrv_file.stem[2:] + '.MP4'))

    if not mp4_file.exists():
        print(f"[0.1] found LRV, but {mp4_file.name} does not exist")
        continue

    filesize = mp4_file.stat().st_size

    if filesize <= 2000000:
        print(f"[0.2] {mp4_file.name} is too small, skipping")
        continue

    with mp4_file.open("rb") as f:
        fdata = f.read(1000000)

        f.seek(filesize - 1000000)
        fdata += f.read(1000000)

        result = hashlib.md5(fdata)

    hash = result.hexdigest()

    proxy_file = to_path / (hash + '.mkv') # kdenlive only considers mkvs?

    if proxy_file.exists():
        print(f"[1.1] {mp4_file.name} already proxied")
        continue

    print(f"[2] >>> Copying {lrv_file.name} -> {proxy_file.name}")

    shutil.copy2(lrv_file, proxy_file)
