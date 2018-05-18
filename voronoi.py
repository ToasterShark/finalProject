
import math
import cv2
import numpy
import random

POINTCOUNT  = 10
xWIN        = 500
yWIN        = 500

BKGRD       = (255,255,255)
DEULCOL     = (0,0,0)
CIRCCOL     = (0,0,255)
VOROCOL     = (255,255,0)

PNTSIZE     = (xWIN+yWIN)/200

vor        = "Voronoi"
img = numpy.zeros((xWIN,yWIN,3))


def drawstuff(po,trongs,im):
    for p in po:
        cv2.circle(im,p,PNTSIZE,DEULCOL,-1)

    for t in trongs:
        print t[0]
        print t[1]
        print t[2]
        cv2.line(im,t[0],t[1],DEULCOL,2)
        cv2.line(im,t[1],t[2],DEULCOL,2)
        cv2.line(im,t[2],t[0],DEULCOL,2)
        circ = circumcircle(t)
        print circ[0]
        print circ[1]
        print circ[2]
        cv2.circle(im,(int(circ[0]),int(circ[1])),int(circ[2]),CIRCCOL,1)





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
    cv2.resizeWindow(vor,1000,1000)

    global img
    img[:][:] = BKGRD

    cv2.imshow(vor,img)
    cv2.waitKey(0)
    trongs = []
    drawstuff(points,trongs,img)

    cv2.imshow(vor,img)
    cv2.waitKey(0)

    trongs = trongle(points,img)
    drawstuff(points,trongs,img)

    cv2.imshow(vor,img)
    cv2.waitKey(0)

def circumcircle(trong):
    a,b,c = trong
    ax,ay = a
    bx,by = b
    cx,cy = c

    ABX = bx - ax
    ABY = by - ay

    CAX = cx - ax
    CAY = cy - ay

    AB  = ABX * (ax + bx) + ABY * (ay + by)
    CA  = CAX * (cx + ax) + CAY * (cy + ay)

    CB  = 2 * (ABX * (cy - by) - ABY * (cx - bx))

    minx,miny,dx,dy = 0,0,0,0

    if abs(CB) < 0.0000001:
        minx = min(ax,bx,cx)
        miny = min(ay,by,cy)
        dx   = (max(ax,bx,cx) - minx) * .5
        dy   = (max(ay,by,cy) - miny) * .5

        x = minx + dx
        y = miny + dy
        r = (dx**2 + dy**2)**(.5)
    else:
        x = (CAY * AB - ABY * CA)/CB
        y = (ABX * CA - CAX * AB)/CB

        dx = x-ax
        dy = y-ay
        r = (dx**2 + dy**2)**(.5)
    return x,y,r
        

def trongle(po,im):
    trglst = []
    trglst.append( (   (-xWIN,int(yWIN+(yWIN/10)))   ,   (int((xWIN/2)),int((-1.5*yWIN)))   ,   (int((2*xWIN)),int(yWIN+(yWIN/10)))   ) )

    for p in po:
        px,py = p
        bdtrg = []
        bdedg = []
        for trg in trglst:
            cx,cy,cr = circumcircle(trg)
            dx = px-cx
            dy = py-cy
            d = (dx**2 + dy**2)**(.5)
            if d <= cr:
                bdtrg.append(trg)
                bdedg.append((trg[0],trg[1]))
                bdedg.append((trg[1],trg[2]))
                bdedg.append((trg[2],trg[0]))
        poly = []
        for edg in bdedg:
            if bdedg.count(edg)<2:
                poly.append(edg)
        for trg in bdtrg:
            bdtrg.remove(trg)
        for edg in poly:
            newTri = (edg[0],edg[1],p)
            trglst.append(newTri)

    for trg in trglst:
        for v in trg:
            if v is (-xWIN,yWIN+(yWIN/10)) or v is ((xWIN/2),(-1.5*yWIN)) or v is ((2*xWIN),yWIN+(yWIN/10)):
                trglst.remove(trg)
    return trglst





if __name__ == '__main__':
    main()