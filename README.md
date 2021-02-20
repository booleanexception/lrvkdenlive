# lrvkdenlive

##What

LRV to Kdenlive, transfer GoPros Low Resolution Videos to Kdenlive without re-rendering

When recording with GoPros you always get a high resolution "MP4" file and a low resolution "LRV" file. The high resolution MP4 file is too heavy in video editing software for most private computers, so most programs generate a so-called "proxy clip" of the MP4 files -- another re-rendered file in very low resolution.

##Why

Kdenlive also has this ability, it re-renders the big MP4 files; which seems a waste of energy and time, since GoProps already have lowres videos prepared.

"lrvkdenlive" solves this problem. It recognizes the lowres "LRV" files in a folder and copies them to the proxy-folder of Kdenlive. I dont know why Kdenlive doesn't do it on its own -- there even seems to be no solution to it since Kdenlive generates a hash that noone seems to have "cracked" yet.

##How

The has is actually childsplay. You take the first 1.000.000 and the last 1.000.000 bytes of the video, attach them to each other and md5 them. It clearly readable in the source (https://github.com/KDE/kdenlive/blob/master/src/bin/projectclip.cpp#L1135). However, this little script solves it, enjoy.