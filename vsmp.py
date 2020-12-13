#! /usr/bin/env python
import os, time, sys, random
from PIL import Image
import ffmpeg
import time
import pygame
pygame.init()
screen = pygame.display.set_mode((0, 0),pygame.FULLSCREEN)


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

# Start here..:
frame = 100000
while frame < frameCount:
	msTimecode = "%dms"%(frame*41.666666)
	generate_frame(inputVid, "/dev/shm/frame.jpg", msTimecode, width, height)
        image = pygame.image.load("/dev/shm/frame.jpg")
        screen.fill((0,0,0))
        screen.blit(image,(0,0))
        pygame.display.update()
	frame = frame + 1
        time.sleep(5)
