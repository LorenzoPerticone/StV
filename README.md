# StV
Streaming-to-Vlc


This simple python3 script allows you to open stream videos from the internet with vlc (with a little change to the source code it is possible to use any video player, as long as it has the right codecs).

It can work with multiple browsers and multiple videos being open at the same time.


HowToUse:
Open your favourite browser (supported browsers include Firefox and Chromium/Chrome), find the video you want to stream and play it. (Muting the embedded player is a good idea, because the video still has to load from that page!)
Once it has started playing, run this program (from the command line or using the graphical user interface).

It will automatically select each and every browser running in your machine which is using flash, and "search it" for videos.

You will then be shown two menus:


-the first is for selecting the browser (the program will automatically select the first browser you opened)

-the second is for selecting the video (again, the first video loaded will be displayed first)


Other than this, it doesn't give you any other information about the name of the browser, nor about wich video you have selected.

This program won't work with just any streaming website, and a complete list is being completed. As for now, supported websites include: 

nowvideo, speedvideo, videopremium, movshare, videomeh.

Sadly, unsupported sites include:

moevideo, streamin, akstream, flashx, backin, openload, videomega, videowood.


Note: this python3 script currently runs only on Linux snd requires python3 and PyQt4. It has been tested on:


Ubuntu and direct derivatives(gnome, mate, kubuntu, lubuntu, xubuntu, edubuntu) 14.04 and 15.04,

Linux Mint 17, 17.1, 17.2, and Linux Mint Debian,

Debian 7, 8 (Wheezy and Jessie) and the current testing release (Stretch)

Fedora 21, 22 and 23

Arch linux and major derivatives (manjaro, antergos, archbang, parabola)

Slackware

Gentoo

Unfortunately I only tested the position of windows on my own machine, always with the same screen and resolution, so any suggestion is welcome.
