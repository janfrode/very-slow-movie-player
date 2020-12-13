
I stumbled over some articles about creating a very-slow-movie-player for
e-ink displays, and it sounded fun. I don't have an e-ink display, but I
have a raspberry pi with a 10" display I use as a family organizer in the
kitchen. It's normally running MagicMirror^2 to display a family calender,
and some weather forecasts. 

https://www.sunfounder.com/collections/touchscreens/products/10inch-touchscreen-for-raspberrypi

First idea was to use the MagicMirror^2 MMM-BackgroundSlideshow to run the slow
movie from pre-processed files. So a brute-force solution was to run the
generate.py script to create all the frames as separate images, then point the
the MMM-BackgroundSlideshow config to it:

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

Since my screen is in portrait mode 800x1280, I cropped out this from the center of 
the image -- keeping aspect ratio. Hopefully the central part contains the important bits. 

This kind of worked -- but was very flickering between each frame. Next I modified 
generate.py script to use pygame to display each frame in fullscreen using "pygame".
This was done using the vsmp.py script.
