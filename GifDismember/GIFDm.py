# coding=gbk
# ��gifͼ�ֽ�ɶ���png


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


def dismember(filename):
    im = Image.open(filename)
    fn=Nstr(str(filename))
    back=Nstr(".gif")
    save_path=fn-back
    os.mkdir(save_path)
    try:
        i = 0
        while 1:
            im.seek(i)
            imframe = im.copy()
            print('���ڲ���{}֡...'.format(i))
            im.save('{}/'.format(save_path) + str(i) + '.png')
            i += 1
    except:
        pass
    return save_path,i

    print('�����ɣ����õ�{}��ͼƬ�������ļ�:{}'.format(i,save_path))

     #def iter_frames(im):
     #   try:
     #       i = 0
     #       while 1:
     #           im.seek(i)
     #           imframe = im.copy()
     #           print('���ڲ���{}֡...'.format(i))
     #           if i == 0:
     #               palette = imframe.getpalette()
     #           else:
     #               imframe.putpalette(palette)
     #           yield imframe
     #           i += 1
     #   except EOFError:
     #       pass  
     #for i, frame in enumerate(iter_frames(im)):
     #   frame.save('gifOutput' + str(i) + '.png', **frame.info) #����ͼƬ�ı����ʽ
    


if len(sys.argv) != 2:
    sys.stderr.write("usage: GIFDm.py <filename>\n")
    sys.exit(-1)


dismember(sys.argv[1])
