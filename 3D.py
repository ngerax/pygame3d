import numpy as np
import pygame as pg
pg.init()
clock=pg.time.Clock()
a,b,olda,oldb,count=np.pi,0,np.pi,0,0
scale=700
dragging=False
d=4.285
WHITE=(255,255,255)
def e(x,y,z):
    N1=-(x*np.sin(a)+y*np.cos(a))
    D1=(x*np.cos(a)-y*np.sin(a))*np.cos(b)-z*np.sin(b)+d
    N2=(x*np.cos(a)-y*np.sin(a))*np.sin(b)+z*np.cos(b)
    D2=(x*np.cos(a)-y*np.sin(a))*np.cos(b)-z*np.sin(b)+d
    if (x*np.cos(a)-y*np.sin(a))>-d and (x*np.cos(a)-y*np.sin(a))*np.cos(b)-z*np.sin(b)>-d:
        return (N1/D1,N2/D2)
    else:
         return(0,0)
def pos(A):
    if str(type(A))=="<class 'tuple'>":
        Po=e(A[0],A[1],A[2])
        return (int(500+4*scale*(Po[0])),int(500-4*scale*(Po[1])))
    elif str(type(A))=="<class 'list'>":
        templi=[]
        for i in range(len(A)):
            templi.append(pos(A[i]))
        return templi
def point(x,y,z):
    Po=e(x,y,z)
    #pg.draw.circle(screen,(255,255,255),(int(500+scale*(Po[0])),int(500-scale*(Po[1]))),1)
    screen.fill((255,255,255),(pos((x,y,z)),(2,2)))
def line(A,B,width,COLOR):
    for i in range(100):
        t=maps(i,0,100,0,1)
        dt=maps(i+1,0,100,0,1)
        x,y,z=A[0]*(1-t)+B[0]*t,A[1]*(1-t)+B[1]*t,A[2]*(1-t)+B[2]*t
        ax,ay,az=A[0]*(1-dt)+B[0]*dt,A[1]*(1-dt)+B[1]*dt,A[2]*(1-dt)+B[2]*dt
        pg.draw.line(screen,COLOR,pos((x,y,z)),pos((ax,ay,az)),width)
def maps(value,i1,f1,i2,f2):
    return (f2-i2)*((value-i1)/(f1-i1))+i2
def vzeros(n,m):
    varr=[]
    for i in range(n):
        temp=[]
        for j in range(m):
            temp.append((0,0,0))
        varr.append(temp)
    return varr
def triangle(A3,B3,C3,COLOR, outline):
    A,B,C=[pos(x) for x in [A3,B3,C3]]
    pg.draw.polygon(screen,COLOR,[A,B,C])
    if outline==True:
        pg.draw.aalines(screen,(0,0,0),True,[A,B,C])
def jens(x):
    return int(max(255-max(-1.5*255*alter((x+60*1.5)/(120*1.5))+127.5,0),0))
def htorgb(h):
    return (jens(h),jens(h-120),jens(h+120))
def alter(x):
    return (np.mod((2*x-1),2)-1)*(-1)**(np.floor(x+0.5))
def drawtri(L):
    Dist =[]
    for i in range(len(L)):
        avgx,avgy,avgz=0.5*(L[i][0][0]+L[i][1][0]+L[i][2][0]),0.5*(L[i][0][1]+L[i][1][1]+L[i][2][1]),0.5*(L[i][0][2]+L[i][1][2]+L[i][2][2])
        Dist.append([(P[0]-avgx)**2+(P[1]-avgy)**2+(P[2]-avgz)**2,i])
    Dist=np.array(Dist)
    Dist=Dist[Dist[:,0].argsort()[::-1]]
    for i in range(len(Dist)):
        ar1,ar2,ar3,ar4,ar5 =L[int(Dist[i][1])][0],L[int(Dist[i][1])][1],L[int(Dist[i][1])][2],L[int(Dist[i][1])][3],L[int(Dist[i][1])][4]
        triangle(ar1,ar2,ar3,ar4,ar5)
screen=pg.display.set_mode((1000,1000))
total=8
r=.5
globe=vzeros(total+1,total+1)
for i in range(total+1):
    theta=maps(i,0,total,0,np.pi)
    for j in range(total+1):
        phi=maps(j,0,total,-np.pi,np.pi)
        x,y,z=np.sin(theta)*np.cos(phi),np.sin(theta)*np.sin(phi),np.cos(theta)
        globe[i][j]=(r*x,r*y,r*z)
def sphere(outline):
    for i in range(total):
        for j in range(total):
            triangles.append([globe[i][j],globe[i+1][j],globe[i][j+1],htorgb(maps(j,0,total,0,360)),outline])
            triangles.append([globe[i+1][j],globe[i][j+1],globe[i+1][j+1],htorgb(maps(j,0,total,0,360)),outline])
def cube(C,r,outline):
    Li=[(-1,-1,-1),(-1,-1,1),(-1,1,-1),(-1,1,1),(1,-1,-1),(1,-1,1),(1,1,-1),(1,1,1)]
    TR=[(0,1,2),(1,2,3),(0,1,5),(0,4,5),(1,5,7),(1,3,7),(0,4,6),(0,2,6),(2,3,7),(2,6,7),(4,5,6),(5,6,7)]
    TR1=[(0,2,3),(0,1,3),(0,1,4),(1,4,5),(3,5,7),(1,3,5),(2,4,6),(0,4,2),(2,3,6),(3,6,7),(4,7,6),(5,4,7)]
    Pun=[]
    for i in range(8):
        Pun.append((C[0]+Li[i][0]*r,C[1]+Li[i][1]*r,C[2]+Li[i][2]*r))
    for j in range(6):
        triangles.append([Pun[TR[2*j][0]],Pun[TR[2*j][1]],Pun[TR[2*j][2]],htorgb(maps(j,0,6,0,360)),False])
        triangles.append([Pun[TR[2*j+1][0]],Pun[TR[2*j+1][1]],Pun[TR[2*j+1][2]],htorgb(maps(j,0,6,0,360)),False])
    for j in range(6):
        triangles.append([Pun[TR1[2*j][0]],Pun[TR1[2*j][1]],Pun[TR1[2*j][2]],htorgb(maps(j,0,6,0,360)),False])
        triangles.append([Pun[TR1[2*j+1][0]],Pun[TR1[2*j+1][1]],Pun[TR1[2*j+1][2]],htorgb(maps(j,0,6,0,360)),False])
    if outline==True:
        pg.draw.aalines(screen,(0,0,0),True,pos([Pun[5],Pun[7]]))
xpp=0
while True:
    screen.fill((0,0,0))
    triangles=[]
    pg.display.set_caption(str(clock.get_fps()))
    P=[-d*np.cos(b)*np.cos(a),d*np.cos(b)*np.sin(a),d*np.sin(b)]
    for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
            if event.type == pg.MOUSEBUTTONDOWN:
                if event.button==1:
                    dragging=True
                if event.button==4:
                    scale *=1.05
                    d=3000/scale
                    screen.fill((0,0,0))
                elif event.button == 5:   
                    scale*=0.95
                    d=3000/scale
                    screen.fill((0,0,0))
            if event.type == pg.MOUSEMOTION:
                if dragging:
                    count+=1
                    if count==1:
                        startx,starty=pg.mouse.get_pos()
                    a,b  =(olda-(startx-pg.mouse.get_pos()[0])/500,oldb-(starty-pg.mouse.get_pos()[1])/500)
                    screen.fill((0,0,0))
            if event.type ==pg.MOUSEBUTTONUP:
                if event.button==1:
                    olda,oldb=a,b
                    count=0
                    dragging=False
    sphere(True)
    cube((np.sin(xpp),0,1.0),0.25,True)
    drawtri(triangles)
    line((0,0,0),(1,0,0),4,(255,0,0))
    line((0,0,0),(0,1,0),4,(0,255,0))
    line((0,0,0),(0,0,1),4,(0,0,255))
    xpp+=0.1
    clock.tick()
    pg.display.update()
