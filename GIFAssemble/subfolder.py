# coding=gbk

import os
from pickle import FALSE
import cv2
import sys
import os.path
import math
import imageio.v2
import argparse
from PIL import Image

class Nstr:  #����ַ���a�����е���b�Ĳ���
    def __init__(self, arg):
       self.x=arg
    def __sub__(self,other):
        c=self.x.replace(other.x,"")
        return c

parser = argparse.ArgumentParser()
parser.add_argument("-f", "--frame", type=int, help="����gif��֡��", default=24, required=False)
parser.add_argument("-r", "--reverse", type=int, help="����gif�Ƿ񵹷�",default=0,required=False)
parser.add_argument("-n", "--name", type=str, help="����gif������", required=False)
args = parser.parse_args()

if len(sys.argv) <= 1:
    args.frame=float(1/24)
    Reversed=0




dir=os.getcwd()
savePath=format(dir)+"\\savepath"
print("�洢�ļ�����"+savePath) #����·��
#if(os.path.exists(savePath)==False):
#   (os.mkdir(savePath))

idx=0
foldername=[]
for dirpath, dirnames, filenames in os.walk(dir):
    print('Directory',dirnames) #���д�������ļ�������
    foldername=dirnames.copy()
    break;
    

print(foldername)

for i in foldername:
#for dirpath in os.walk(dir):
    print("idx="+str(int(idx)))
    print('Directory',dirnames) #���д�������ļ�������
    filename=dirnames[idx]+".gif"  #�ļ���
    
    print("��ǰ�ļ��е�������"+dirnames[idx]);
    if(dirnames[idx]=="savepath"):
        continue
    print(dir+"\\"+dirnames[idx]+"\\0.png")
    baseImg=Image.open(format(dir+"\\"+dirnames[idx]+"\\0.png"))
    print(baseImg)
    baseWideth=baseImg.size[0]
    baseHeight=baseImg.size[1] #���ڵ�һ��ͼƬȷ��gif�Ĵ�С

    print("ͼ��ĳߴ���"+format(baseWideth)+"*"+format(baseHeight))

   
    
    im=[]
    durationG=0;
    folderPath=dir+"\\"+dirnames[idx]
    print("��ǰ���ڴ�����ļ�����"+format(folderPath))
    photolist=os.listdir(folderPath)
    print("һ����"+str(len(photolist))+"����Ƭ")
    if args.reverse==0:
        print("����")
        p=0  
        for i in range(len(photolist)):  #������뷨����gif
            im.append(imageio.v2.imread(format(folderPath+"\\"+str(p)+".png")))  #���ܰ���photolist���ļ��б�˳�����ͼƬ���ᵼ�����򡣶�梳����ѽ�gif�ֽ�Ϊ��0-n��pngͼ��ֱ�����μ�¼ͼƬ����
            p+=1
            #print("using"+photolist[i])
            durationG+=float(1/args.frame/50)          #����ÿһ֡��ʱ��
    else:
        print("����")
        p=len(photolist)-1  
        for i in range(len(photolist)):  #������뷨����gif
            im.append(imageio.v2.imread(format(folderPath+"\\"+str(p)+".png")))  #���ܰ���photolist���ļ��б�˳�����ͼƬ���ᵼ�����򡣶�梳����ѽ�gif�ֽ�Ϊ��0-n��pngͼ��ֱ�����μ�¼ͼƬ����
            p-=1
            #print("using"+photolist[i])
            durationG+=float(1/args.frame/50)        #����ÿһ֡��ʱ��

    print(format(dirnames[idx])+"����ʱ��Ϊ"+format(durationG))
    Filename=dirnames[idx]+".gif"
    imageio.mimsave(format(Filename),im,'GIF',duration=durationG)
    idx+=1
    
    
    
    
    #im = Image.new(mode= "RGBA", size= (baseWideth, baseHeight)) #��������Ƭ������ʵ����
    #im.show()

    #imagefile = [] #�洢���е�ͼ�������
    #width = 0
    #folderPath=procDir+"\\"+dirnames[id]
    #fileNumber=os.listdir(folderPath)
    #tot=len(fileNumber)
    #for i in range(0,5): #������ͼ�������
    #    imagefile.append(Image.open(format(procDir)+"\\"+dirnames[idx]+"\\"+str(i)+'.png')) #��������ͼ�����ƴ���imagfile

    #for image in imagefile:
    #    im.paste(image,(width,0,baseWideth+width,baseHeight)) #��ͼƬ��������һ��ͼƬ��
    #    width = width +2
    
    #im.save(format(savePath)+"\\"+filename+".gif")
    #im.show()
    #idx+=1

    #for filename in filenames:
    #    print('File',filename)


input()
