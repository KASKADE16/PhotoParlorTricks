
# coding=gbk

import cv2
import sys
import os.path
import math

def mirror(filename):
    # ͼƬ������
    from PIL import Image
    im = Image.open(filename) #ԴͼƬ
    pim = im.load()
    #an = Image.open(filename+"_reversed.jpg") #���ͼƬ
    an = Image.new('RGB',(im.size[0],im.size[1]),"red")
    ans = an.load()
    for i in range(im.size[0]):
        for j in range(im.size[1]):
            ans[i, j] = pim[im.size[0]-i-1, j]
    an.show() #�����ͼƬ
    #imsave("./images/'"+filename+"_output.png",an)
    an.save(filename+"_output.png") #���洦���ͼƬ


if len(sys.argv) != 2:
    sys.stderr.write("usage: reverse.py <filename>\n")
    sys.exit(-1)

mirror(sys.argv[1])
