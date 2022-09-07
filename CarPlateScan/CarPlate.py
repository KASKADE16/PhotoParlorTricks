from pprint import pprint
import cv2
import sys
import os.path
import math

dir=os.getcwd()
srcCar=dir+"/haarcascade_russian_plate_number.xml"

def detectFace(filename, cascade_file_Car = srcCar):
    if (not os.path.isfile(cascade_file_Car) ):
        raise RuntimeError("%s: not found" % cascade_file_Car )

    cascadeCar = cv2.CascadeClassifier(cascade_file_Car)

    image = cv2.imread(filename, cv2.IMREAD_COLOR)
    #cv2.cvtColor(image,gray,cv2.COLOR_BGR2GRAY)
    gray1 = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)


    #cv2.equalizeHist(gray,gray)
    gray1 = cv2.equalizeHist(gray1)
    cnt = 0;

    plates = cascadeCar.detectMultiScale(gray1,
                                     # detector options
                                     scaleFactor = 1.1,
                                     minNeighbors = 5,
                                     minSize = (36, 36))

   # print("FACES = "+str(int(plates.size())))


    for (x, y, w, h) in plates:
        img=image[y:y+h,x:x+w]
        cnt=cnt+1
        fileout=filename+"_FACE"+str(cnt)+"_OUTPUT"+".png"
        cv2.imwrite(fileout, img)
        cv2.rectangle(image, (x, y), (x + w, y + h), (0, 200, 200), 2)

    ExtractAddress=filename+"_OUTPUT.png"
    #cv2.imshow("CarPlateDetect", image)
    #cv2.waitKey(0)
    cv2.imwrite(ExtractAddress, image)

if len(sys.argv) != 2:
    sys.stderr.write("usage: detect.py <filename>\n")
    sys.exit(-1)

detectFace(sys.argv[1])