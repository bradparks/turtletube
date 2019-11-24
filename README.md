# turtletube

Playing youtube videos in a turtle window of Python

I was experimenting with the idea of using turtle window as a player. I google and found [linedraw](https://github.com/LingDong-/linedraw) and some Stackoverflow posts which helped me convert the video to series of images. For downloading videos I am using [youtube-dl](https://github.com/ytdl-org/youtube-dl)

How to run it:-

1. Checkout linedraw, as I don't know if it has a python package separately.
2. Put turtletube.py into linedraw repo.
3. install numpy and opencv-python
4. python3 turtletube.py "youtube-video-url"
  
It took me around 3 hours to get this up and working, and mostly issues were around refresh of turtle screen. I used two separate turtles and swapped them every next frame. That gave it better look. I think depending on the processing power of the system, the speed of video play varies.

Here is a [sample video](https://youtu.be/4ywXNJ_38T0) by running `python3 turtle-tube.py "https://www.youtube.com/watch?v=zE7PKRjrid4"`
 
NOTE:- code quality is shitty. I am gonna rewrite it in more pythonic style. 
