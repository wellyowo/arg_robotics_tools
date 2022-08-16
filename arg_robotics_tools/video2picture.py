# AUTOGENERATED! DO NOT EDIT! File to edit: ../02_video2picture.ipynb.

# %% auto 0
__all__ = ['get_images_from_video']

# %% ../02_video2picture.ipynb 4
import gdown
from zipfile import ZipFile
from PIL import Image
import sys
import os
import cv2

# %% ../02_video2picture.ipynb 6
def get_images_from_video(video_name, time_F):
    '''
    open and read video,then save the images of video depending on the parameter(time_F) you setup.
    '''
    video_images = []
    vc = cv2.VideoCapture(video_name)
    c = 1
    
    if vc.isOpened(): 
        rval, video_frame = vc.read()
    else:
        rval = False

    while rval:  
        rval, video_frame = vc.read()
        
        if(c % time_F == 0): 
            video_images.append(video_frame)     
        c = c + 1
    vc.release()
    
    return video_images
