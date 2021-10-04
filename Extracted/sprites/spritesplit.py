#!/usr/local/opt/python@3.8/bin/python3
import os
import glob
from PIL import Image
Image.MAX_IMAGE_PIXELS = None # to avoid image size warning

# if you want file of a specific extension (.png):
filelist = [f for f in glob.glob("*.png", recursive=True)]
savedir = "."

start_pos = start_x, start_y = (0, 0)
cropped_image_size = w, h = (32, 32)

for file in filelist:
    img = Image.open(file)
    width, height = img.size

    frame_num = 1
    for col_i in range(0, height, h):
        for row_i in range(0, width, w):
            crop = img.crop((col_i, row_i, col_i + w, row_i + h))
            name = os.path.basename(file)
            name = os.path.splitext(name)[0]
            save_to= os.path.join(savedir, name+"_{:03}_{:03}.png")
            crop.save(save_to.format(row_i, col_i))
            frame_num += 1

