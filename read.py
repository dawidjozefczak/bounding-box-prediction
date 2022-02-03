import csv
import queue
from sqlite3 import converters
from matplotlib.pyplot import fill
import pandas as pd
import os
from PIL import Image, ImageDraw
import numpy as np
from collections import deque
import json

df = pd.read_csv("video_0332.csv")

# print(df.head())
# ID,bounding_box,future_bounding_box,scenefolderpath,filename,crossing_obs,crossing_true,label

ID = df['ID']
bounding_box = df['bounding_box']
future_bounding_box = df['future_bounding_box']
scenefolderpath = df['scenefolderpath']
filename = df['filename']
crossing_obs = df['crossing_obs']
crossing_true = df['crossing_true']
label = df['label']

filenamelist = []
crossing_obslist = []
crossing_truelist = []
bounding_boxlist = []
future_bounding_boxlist = []


for i in range(len(ID)):
    print(i)
#     #----filename
    nwe = str(filename[i])
    nwe2 = nwe.replace("\'", "\"")
    alist = json.loads(nwe2)
    filenamelist.append(alist)
#     #----crossing_obs
    crossing_obslist.append(json.loads(crossing_obs[i]))
#     #----crossing_true
    crossing_truelist.append(json.loads(crossing_true[i]))
#     #----bounding_box
    bounding_boxlist.append(json.loads(bounding_box[i]))
#     #----future_bounding_box
    future_bounding_boxlist.append(json.loads(future_bounding_box[i]))

# print(crossing_truelist[0])
for j in range(len(ID)):
    for i in range(len(filenamelist[j])):
        scene = Image.open(os.path.join('video_0332/') + filenamelist[j][i])
        img = ImageDraw.Draw(scene)
        if (crossing_truelist[j][i] == 1):
            sizeb = 20
        else:
            sizeb = 5

        x1 = bounding_boxlist[j][i][0]
        x2 = bounding_boxlist[j][i][1]
        y1 = bounding_boxlist[j][i][2]
        y2 = bounding_boxlist[j][i][3]

        x_low_left = int(x1 - y1/2)     #x1 
        y_low_left = int(x2 - y2/2)     #x2 
        x_high_right = int(x1 + y1/2)   #y1
        y_high_right = int(x2 + y2/2)   #y2

        points = (x_low_left, x_high_right), (y_low_left, x_high_right), (y_low_left, y_high_right), (x_low_left, y_high_right), (x_low_left, x_high_right)
        # points = (x_low_left, y_low_left), (y_high_right, y_low_left), (y_high_right, y_high_right), (x_low_left, y_high_right), (x_low_left, y_low_left)
        img.line(points, fill="red", width=sizeb)
        
        fx1 = future_bounding_boxlist[j][i][0]
        fx2 = future_bounding_boxlist[j][i][1]
        fy1 = future_bounding_boxlist[j][i][2]
        fy2 = future_bounding_boxlist[j][i][3]

        fx_low_left = int(fx1 - fy1/2)     #x1
        fy_low_left = int(fx2 - fy2/2)     #x2
        fx_high_right = int(fx1 + fy1/2)   #y1
        fy_high_right = int(fx2 + fy2/2)   #y2

        fpoints = (fx_low_left, fx_high_right), (fy_low_left, fx_high_right), (fy_low_left, fy_high_right), (fx_low_left, fy_high_right), (fx_low_left, fx_high_right)
        # fpoints = (fx_low_left, fy_low_left), (fy_high_right, fy_low_left), (fy_high_right, fy_high_right), (fx_low_left, fy_high_right), (fx_low_left, fy_low_left)
        img.line(fpoints, fill="blue", width=sizeb)
        
        scene.save(os.path.join('video_0332/') + filenamelist[j][i])

