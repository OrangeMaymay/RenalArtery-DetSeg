import cv2
import os
from PIL import Image
import numpy as np
 
# The folder path of input and output
inPath = r"./boliyangbian/"
output_path = r'./boliyangbian9000/'
if not os.path.exists(output_path):
    os.mkdir(output_path)
outPath = output_path
 
for f in os.listdir(inPath):
    path = inPath + f.strip()
    Image.MAX_IMAGE_PIXELS = None
    mat = Image.open(path)
    img = np.array(mat)
    height = img.shape[0]
    width = img.shape[1]
    heightBlock = 9000
    widthBlock = 9000
    f2 = f.split('.')[0]
    # print(f2)
    for i in range(0,int(height / heightBlock)):
        for j in range(0,int(width / widthBlock)):
            cutImage = img[i*heightBlock:(i+1)*heightBlock, j*widthBlock:(j+1)*widthBlock]
            savePath = outPath + f2 + "_" + str(i*int(width / widthBlock)+(j+1)) + ".png"
            cv2.imwrite(savePath,cutImage)
