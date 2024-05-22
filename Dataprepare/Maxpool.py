import os
import torch.nn as nn
import torch
from PIL import Image
import numpy as np
from torchvision import transforms
import torchvision
import torch.nn.functional as F
 
class Maxpool(nn.Module):
    def __init__(self):
        super(Maxpool, self).__init__()
        self.maxpool = nn.MaxPool2d(kernel_size=3, stride=3)
    def forward(self, x):
        x = self.maxpool(x)         
        return x
 
img_dir = 'boliyangbian9000/'
img_names = [i for i in os.listdir(img_dir)]     
img_path = [img_dir + i for i in img_names]      

for i in range(len(img_names)):
    img = Image.open(img_path[i]).convert('RGB')

    transf = transforms.ToTensor()
    img_tensor = transf(img)
    model = Maxpool()
    output = model(img_tensor)
    output_path = r'./outputmaxpool3000/'
    if not os.path.exists(output_path):
        os.mkdir(output_path)
 
    torchvision.utils.save_image(output, output_path + img_names[i])

