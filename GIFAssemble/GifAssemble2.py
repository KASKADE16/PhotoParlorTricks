
# coding=gbk
#ƴ��ͼ��.py

from xmlrpc.client import Boolean
import cv2
import sys
import os.path
import math
from PIL import Image

class Nstr:  #����ַ���a�����е���b�Ĳ���
    def __init__(self, arg):
       self.x=arg
    def __sub__(self,other):
        c=self.x.replace(other.x,"")
        return c

def assemble(filename):
    folder 
    path = "D:\DeskTop\CTF\gifs\gg" # Դ�ļ�������Ҫ��ȷ��Ŀ¼��������ͼƬ��ͳһǰ׺
    save_path = "D:\DeskTop\CTF\gifs"   # ����ļ�·��
    target_image="final.png" # ���ͼƬ������

    im = Image.new('RGBA',(2*201,600)) #��������Ƭ������ʵ����
    imagefile = [] #�洢���е�ͼ�������
    width = 0

    for i in range(0,101): #������ͼ�������
        imagefile.append(Image.open(path+str(i)+'.png')) #��������ͼ�����ƴ���imagfile

    for image in imagefile:
        im.paste(image,(width,0,2+width,600)) #��ͼƬ��������һ��ͼƬ��
        width = width +2
    im.save(save_path+target_image)
    im.show()

if len(sys.argv) != 2:
    sys.stderr.write("usage: GIFDm.py <filename>\n")
    sys.exit(-1)




assemble(sys.argv[1])

