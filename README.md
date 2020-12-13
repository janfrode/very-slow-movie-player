
I stumbled over some articles about creating a very-slow-movie-player for
e-ink displays, and it sounded fun. I don't have an e-ink display, but I
have a raspberry pi with a 10" display I use as a family organizer in the
kitchen. It's normally running MagicMirror^2 to display a family calender,
and some weather forecasts. 

https://www.sunfounder.com/collections/touchscreens/products/10inch-touchscreen-for-raspberrypi

First idea was to use the MagicMirror^2 MMM-BackgroundSlideshow to run the slow
movie from pre-processed files. So a brute-force solution was to run the
following script:

```
#! /usr/bin/env python
import os, time, sys, random
from PIL import Image
import ffmpeg

def generate_frame(in_filename, out_filename, time, width, height):                                                                              
    (
        ffmpeg
        .input(in_filename, ss=time)
        .filter_('crop', w='1/2*(in_w-650)', h='in_h')
        .filter('scale', width, height, force_original_aspect_ratio=1)
        .filter('pad', width, height, -1, -1)
        .output(out_filename, vframes=1)
        .overwrite_output()
        .run(capture_stdout=True, capture_stderr=True)
    )

inputVid = "/home/pi/Psycho.1960.1080p.BrRip.x264.YIFY.mp4"                                                                                      
width = 800
height = 1280
frameCount = int(ffmpeg.probe(inputVid)['streams'][0]['nb_frames'])

#>>> print frameCount
#156588

frame = 1000
while frame < frameCount:
	msTimecode = "%dms"%(frame*41.666666)
	generate_frame(inputVid, "/home/pi/MagicMirror/modules/MMM-BackgroundSlideshow/very-slow-movie/psycho-" + "%06d" % frame + ".jpg", msTimecode, width, height)
	frame = frame + 2600
```

with the MMM-BackgroundSlideshow config:

```

			  {
				      module: 'MMM-BackgroundSlideshow',
				      position: 'fullscreen_below',
				      config: {
					            imagePaths: ['modules/MMM-BackgroundSlideshow/very-slow-movie/'],
					            transitionImages: false,
					            randomizeImageOrder: false,
					            slideshowSpeed: 10000,	// milliseconds
					          },
				    },
```

