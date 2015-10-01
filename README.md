# StV
Streaming-to-Vlc


This simple python3 script allows one to open stream videos from the internet with vlc (with a little change to the source code it is possible to use any video player, as long as it has the right codecs).

It works with multiple browsers and multiple videos opened.


HowToUse:
Open your favourite browser (supported browsers include Firefox and Chromium/Chrome), find the video you want to stream and play it. (Muting the embedded player is a good idea, because the video still has to load from that page!)
Once it has started playing, run this program (from the command line or using the graphical interface).

It will automatically select each and every browser running in your machine which is using flash, and "search it" for videos.

You will then be promted with two menus:


-the first is for selecting the browser (the program will automatically select the first browser you opened)

-the second is for selecting the video (again, the first video loaded will be displayed first)

Other than this, it doesn't give you any other information about the name of the browser, nor about wich video you have selected.

This program won't work with any streaming website, and a complete list is being completed. As for now, supported sites include: 

nowvideo, speedvideo, videopremium, movshare, videomeh.

Sadly, unsupported sites include:

moevideo, streamin, akstream, flashx, backin, openload, videomega, videowood.


Note: this python3 script currently runs only under Linux, requires python3 and PyQt4 and has been tested on:


Ubuntu and direct derivatives 14.04 and 15.04,

Linux Mint 17, 17.1 and 17.2, also Linux Mint Debian,

Debian 7, 8 (Wheezy and Jessie) and current testing (Stretch)

Fedora 21, 22 and 23

Arch linux and major derivatives (manjaro, antergos, archbang, parabola)

Slackware

Gentoo

Unfortunately I only tested the position of windows on my own machine, always with the same screen and resolution, so any suggestion is welcome.

Also, sorry for my bad english. It's not my native language.
