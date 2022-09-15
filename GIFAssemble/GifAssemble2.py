
# coding=gbk
#拼接图像.py

from xmlrpc.client import Boolean
import cv2
import sys
import os.path
import math
from PIL import Image

class Nstr:  #清除字符串a中所有等于b的部分
    def __init__(self, arg):
       self.x=arg
    def __sub__(self,other):
        c=self.x.replace(other.x,"")
        return c

def assemble(filename):
    folder 
    path = "D:\DeskTop\CTF\gifs\gg" # 源文件名，需要精确到目录名到多张图片的统一前缀
    save_path = "D:\DeskTop\CTF\gifs"   # 输出文件路径
    target_image="final.png" # 输出图片的名字

    im = Image.new('RGBA',(2*201,600)) #创建新照片，根据实际来
    imagefile = [] #存储所有的图像的名称
    width = 0

    for i in range(0,101): #这里填图像的张数
        imagefile.append(Image.open(path+str(i)+'.png')) #遍历，将图像名称存入imagfile

    for image in imagefile:
        im.paste(image,(width,0,2+width,600)) #将图片张贴到另一张图片上
        width = width +2
    im.save(save_path+target_image)
    im.show()

if len(sys.argv) != 2:
    sys.stderr.write("usage: GIFDm.py <filename>\n")
    sys.exit(-1)




assemble(sys.argv[1])

