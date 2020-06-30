# -*- coding: utf-8 -*
from PIL import Image

# import os

# img = Image.new('RGB', (23, 255))

img_2 = Image.open('files/1.png')
 
img_2 = img_2.convert('RGB')

r, g, b = img_2.split()

newIm =Image.merge('RGB', (g, r, b))

newIm.save('files/gg.png')
