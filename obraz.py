#Import required libraries
import os
import sys
from PIL import Image, ImageDraw

#Create Image object
im = Image.open("Images/network.PNG")
path = "txt.png"
name = path[-6:]
#Draw line
draw = ImageDraw.Draw(im)
draw.line((0, 0) + im.size, fill=128)
draw.line((0, im.size[1], im.size[0], 0), fill=128)

#Show image
im.show()
im.save(os.path.join('Images/') + name)