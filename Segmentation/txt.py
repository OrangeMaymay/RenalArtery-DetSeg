import glob
def write_name():
    #npz文件路径
    files = glob.glob(r'predict_data0414/Synapse/test_vol_h5/images/*.npz')
    #txt文件路径
    f = open(r'lists0414/lists_Synapse/test_vol.txt','w')
    for i in files:
        name = i.split('/')[-1]
        name2 = name.split('.')[0]
        print(name2)
        name = name[:-4]+'\n'
        f.write(name)
write_name()
