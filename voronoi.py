
import math
import cv2
import numpy
import random

POINTCOUNT = 20
xWIN       = 100
yWIN       = 100
COLORS     = [(255,0,0),(0,255,0),(0,0,255),(255,255,0)]
BKGRD      = (255,255,255)
PNTCLR     = (0,0,0)


vor        = "Voronoi"
img = numpy.zeros((xWIN,yWIN,3))


def drawstuff(po,im):
    for p in po:
        print p
        cv2.circle(im,p,1,PNTCLR,-1)



def main():
    points = []
    for i in range(0,POINTCOUNT-1):
        print "new point"
        newX = random.randint(0,xWIN)
        newY = random.randint(0,yWIN)
        newPoint = (newX,newY) 
        points.append(newPoint)

    print points

    cv2.namedWindow(vor,cv2.WINDOW_NORMAL)

    global img
    img[:][:] = BKGRD

    cv2.imshow(vor,img)
    cv2.waitKey(0)

    drawstuff(points,img)

    cv2.imshow(vor,img)
    cv2.waitKey(0)

def trongle(po,im):
    trglst = []
    


if __name__ == '__main__':
    main()