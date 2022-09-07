from pprint import pprint
import cv2
import sys
import os.path
import math

dir=os.getcwd()
srcFace=dir+"/haarcascade_frontalface_alt2.xml"
srcEyes=dir+"/haarcascade_eye.xml"

def detectFace(filename, cascade_file_Face = srcFace,cascade_file_Eyes = srcEyes ):
    if (not os.path.isfile(cascade_file_Face) or not os.path.isfile(cascade_file_Eyes)):
        raise RuntimeError("%s: not found" % cascade_file_Face % "or" % cascade_file_Eyes)

    cascadeFace = cv2.CascadeClassifier(cascade_file_Face)
    cascadeEyes = cv2.CascadeClassifier(cascade_file_Eyes)

    image = cv2.imread(filename, cv2.IMREAD_COLOR)
    #cv2.cvtColor(image,gray,cv2.COLOR_BGR2GRAY)
    gray1 = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    gray2 = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)


    #cv2.equalizeHist(gray,gray)
    gray1 = cv2.equalizeHist(gray1)
    gray2 = cv2.equalizeHist(gray2)
    cnt = 0;

    faces = cascadeFace.detectMultiScale(gray1,
                                     # detector options
                                     scaleFactor = 1.1,
                                     minNeighbors = 5,
                                     minSize = (36, 36))

   # print("FACES = "+str(faces.size()))

    eyes = cascadeEyes.detectMultiScale(gray2,
                                         # detector options
                                         scaleFactor = 1.1,
                                         minNeighbors = 5,
                                         minSize = (16, 16))

    # print("EYES = "+str(eyes.size()))

    for (x, y, w, h) in faces:
        img=image[y:y+h,x:x+w]
        cnt=cnt+1
        fileout=filename+"_FACE"+str(cnt)+"_OUTPUT"+".png"
        cv2.imwrite(fileout, img)
        cv2.rectangle(image, (x, y), (x + w, y + h), (0, 0, 255), 2)

    cnt = 0;
    for (x, y, w, h) in eyes:
        img=image[y:y+h,x:x+w]
        cnt=cnt+1
        fileout=filename+"_EYES"+str(cnt)+"_OUTPUT"+".png"
        cv2.imwrite(fileout, img)
        radius=math.sqrt(w*w+h*h)/3
        x1=x+w/2;
        y1=y+h/2;
        cv2.circle(image,(int(x1),int(y1)),int(radius),(0,194,20),1)

    ExtractAddress=filename+"_OUTPUT.png"
    #cv2.imshow("AnimeFaceDetect", image)
    #cv2.waitKey(0)
    cv2.imwrite(ExtractAddress, image)

if len(sys.argv) != 2:
    sys.stderr.write("usage: detect.py <filename>\n")
    sys.exit(-1)

detectFace(sys.argv[1])