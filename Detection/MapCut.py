import cv2
import os
import glob
from PIL import Image
import numpy as np
import shutil
yuan_path=os.path.abspath(r'/DKDorigin') 
mask_path=os.path.abspath(r'/DKDoriginmask')
save_path=os.path.abspath(r"/DKDoriginadd")
# print(1)
def cut(img_path,img_path1,name):
    img = cv2.imread(img_path)
    # img = cv2.resize(img, (256, 256))
    img2 = cv2.imread(img_path1)
 
    rows,cols,channels=img.shape
    hsv=cv2.cvtColor(img2,cv2.COLOR_BGR2HSV)
 
    lower_blue=np.array([0,0,0])
    upper_blue=np.array([180,255,46])
 
    mask = cv2.inRange(hsv, lower_blue, upper_blue)
    #cv2.imshow('Mask', mask)
 
    erode=cv2.erode(mask,None,iterations=1)
    #cv2.imshow('erode',erode)
    dilate=cv2.dilate(erode,None,iterations=1)
    #cv2.imshow('dilate',dilate)
 
    for i in range(rows):
        for j in range(cols):
            if dilate[i,j]==0:
                img2[i,j]=img[i,j]
 
    #cv2.imshow('image', img2)
 
    #cv2.waitKey(0)
    #cv2.destroyAllWindows()
 
    cv2.imwrite(os.path.join(save_path,name),img2)
    print(1)
yuan1 = [] #yuan1指文件夹里的文件，包括文件后缀格式；
yuanname1 = [] #yuanname1指里面的文件名称，不包括文件后缀格式
#通过glob.glob来获取第一个文件夹下，所有'.jpg'文件
yuanList1 = glob.glob(os.path.join(yuan_path, '*.png'))
# print(yuanList1)
 
#遍历所有文件，获取文件名称（包括后缀）
for item in yuanList1:
    yuan1.append(os.path.basename(item))
# print(yuan1)
#遍历文件名称，去除后缀，只保留名称
for item in yuan1:
    (temp1, temp2) = os.path.splitext(item)
    yuanname1.append(temp1)
# print('aaaaa',yuanname1)
#对于第二个文件夹路径，做同样的操作
 
mask2 = []
maskname2 = []
maskList2 = glob.glob(os.path.join(mask_path, '*.png'))
 
for item in maskList2:
    mask2.append(os.path.basename(item))
 
for item in mask2:
    (temp1, temp2) = os.path.splitext(item)
    temp1 = temp1.split("_json")[0]
    maskname2.append(temp1)
# print('bbbbb',maskname2)
 
#通过遍历，获取第一个文件夹下，文件名称（不包括后缀）与第二个文件夹相同的文件，并另存在outDir文件夹下。文件名称与第一个文件夹里的文件相同，后缀格式亦保持不变。
for item1 in yuanname1:
    for item2 in maskname2:
        if item1 == item2:
            dir = yuanList1[yuanname1.index(item1)]
            dir1 = maskList2[maskname2.index(item1)]
            img = Image.open(dir)
            name = os.path.basename(dir)
            name1 = os.path.basename(dir1)
            print(dir)
            print(dir1)  
            print(1)
            cut(dir,dir1,name)
            print(name)
            # img.save(os.path.join(outDir, name))
            # shutil.copyfile(dir1,os.path.join(outDir, name1))
