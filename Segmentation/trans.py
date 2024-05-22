import numpy as np
import cv2
import glob
def npz():
    #原图像路径
    path = r'predict_data0413/origin/output/images/*.png'
    #项目中存放训练所用的npz文件路径
    path2 = r'predict_data0413/Synapse/test_vol_h5/'
    for i,img_path in enumerate(glob.glob(path)):
    	#读入图像
        image = cv2.imread(img_path)
        image = cv2.cvtColor(image,cv2.COLOR_BGR2RGB)
        #读入标签
        label_path = img_path.replace('images','labels')
        label = cv2.imread(label_path,flags=0)
        label[label==38]=1
        label[label==75]=2
		#保存npz
        np.savez(path2+img_path.split('/')[-1].split('.')[0],image=image,label=label)
        if i >=500:

            print(img_path.split('/')[-1].split('.')[0])

    print('ok')
npz()