# coding=gbk

import os
import cv2
import sys
import os.path
import math
import imageio.v2
from PIL import Image

class Nstr:  #清除字符串a中所有等于b的部分
    def __init__(self, arg):
       self.x=arg
    def __sub__(self,other):
        c=self.x.replace(other.x,"")
        return c


dir=os.getcwd()
savePath=format(dir)+"\\savepath"
print("存储文件夹是"+savePath) #保存路径
#if(os.path.exists(savePath)==False):
#   (os.mkdir(savePath))

idx=0
foldername=[]
for dirpath, dirnames, filenames in os.walk(dir):
    print('Directory',dirnames) #所有待处理的文件夹名字
    foldername=dirnames.copy()
    break;
    

print(foldername)

for i in foldername:
#for dirpath in os.walk(dir):
    print("idx="+str(int(idx)))
    print('Directory',dirnames) #所有待处理的文件夹名字
    filename=dirnames[idx]+".gif"  #文件名
    
    print("当前文件夹的名字是"+dirnames[idx]);
    if(dirnames[idx]=="savepath"):
        continue
    print(dir+"\\"+dirnames[idx]+"\\0.png")
    baseImg=Image.open(format(dir+"\\"+dirnames[idx]+"\\0.png"))
    print(baseImg)
    baseWideth=baseImg.size[0]
    baseHeight=baseImg.size[1] #基于第一张图片确定gif的大小

    print("图像的尺寸是"+format(baseWideth)+"*"+format(baseHeight))

   
    
    im=[]
    durationG=0;
    folderPath=dir+"\\"+dirnames[idx]
    print("当前正在处理的文件夹是"+format(folderPath))
    photolist=os.listdir(folderPath)
    print("一共有"+str(len(photolist))+"张照片")
    p=0  
    for i in range(len(photolist)):  #替代插入法制作gif
        im.append(imageio.v2.imread(format(folderPath+"\\"+str(p)+".png")))  #不能按照photolist的文件列表顺序插入图片，会导致乱序。而姊程序已将gif分解为从0-n的png图像，直接整形记录图片即可
        p+=1
        #print("using"+photolist[i])
        durationG+=0.0007           #设置每一帧的时间
    print(format(dirnames[idx])+"的总时长为"+format(durationG))
    imageio.mimsave(format(dirnames[idx]+".gif"),im,'GIF',duration=durationG)
    idx+=1
    
    
    
    
    #im = Image.new(mode= "RGBA", size= (baseWideth, baseHeight)) #创建新照片，根据实际来
    #im.show()

    #imagefile = [] #存储所有的图像的名称
    #width = 0
    #folderPath=procDir+"\\"+dirnames[id]
    #fileNumber=os.listdir(folderPath)
    #tot=len(fileNumber)
    #for i in range(0,5): #这里填图像的张数
    #    imagefile.append(Image.open(format(procDir)+"\\"+dirnames[idx]+"\\"+str(i)+'.png')) #遍历，将图像名称存入imagfile

    #for image in imagefile:
    #    im.paste(image,(width,0,baseWideth+width,baseHeight)) #将图片张贴到另一张图片上
    #    width = width +2
    
    #im.save(format(savePath)+"\\"+filename+".gif")
    #im.show()
    #idx+=1

    #for filename in filenames:
    #    print('File',filename)


input()
