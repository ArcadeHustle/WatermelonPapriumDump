#!/usr/local/opt/python@3.8/bin/python3
import os
import cv2
import sys

file = sys.argv[1]
folder = file.split(".")[0]
print(folder)

try:
    os.stat(folder)
except:
    os.mkdir(folder)

import cv2
img = cv2.imread(file)
for r in range(0,img.shape[0],32):
    for c in range(0,img.shape[1],32):
        cv2.imwrite(f"sprite_{r}_{c}.png",img[r:r+32, c:c+32,:])
