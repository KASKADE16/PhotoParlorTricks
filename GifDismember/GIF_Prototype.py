# 将gif图分解成多张png
from PIL import Image

im = Image.open('aiba.gif')

def iter_frames(im):
    try:
        i = 0
        while 1:
            im.seek(i)
            imframe = im.copy()
            if i == 0:
                palette = imframe.getpalette()
            else:
                imframe.putpalette(palette)
            yield imframe
            i += 1
    except EOFError:
        pass


for i, frame in enumerate(iter_frames(im)):
    frame.save('aiba' + str(i) + '.png', **frame.info) #最终图片的保存格式


