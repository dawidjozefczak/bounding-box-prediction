import cv2
import os

image_folder = 'video_0338'
video_name = 'video_0338.mp4'

def save():
    os.system("ffmpeg -r 1 -i img%01d.png -vcodec mpeg4 -y movie.mp4")



    # ffmpeg -r 25 -i video_0324/%05d.png -vcodec mpeg4 -y movie_324.mp4