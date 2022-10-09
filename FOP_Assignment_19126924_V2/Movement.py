import random as rn
import numpy as np 

def Movement(speed):
    xmove=rn.randint(-10,10)
    ymove=rn.randint(-10,10)
    moves=(xmove,ymove)
    return moves

def hunt(hpos,ppos):

    hx = hpos[0]
    hy= hpos[1]
    px = ppos[0]       
    py = ppos[1]
    
    if hx > px:
        hx=hx-1
    elif hx < px:
        hx=hx+1
    else:
        pass
    if hy > py:
        hy=hy-1
    elif hy < py:
        hy=hy+1
    else:
        pass
    
    point =(hx,hy)
    return point
    # for i in range(3)
    '''dist = abs((px-(hx-1))+(py-(hy+1)))
    distances.append(dist) #0

    dist = abs((px-(hx))+(py-(hy+1)))
    distances.append(dist) #1

    dist = abs((px-(hx+1))+(py-(hy+1)))    
    distances.append(dist) #2

    dist = abs((px-(hx-1))+(py-(hy)))
    distances.append(dist) #3

    dist = abs((px-(hx+1))+(py-(hy)))
    distances.append(dist) #4

    dist = abs((px-(hx-1))+(py-(hy-1)))
    distances.append(dist) #5

    dist = abs((px-hx)+(py-(hy-1)))
    distances.append(dist) #6

    dist = abs((px-(hx+1))+(py-(hy-1)))
    distances.append(dist) #7

    bestdist = min(distances)
    position =distances.index(bestdist)

    if position == 0:
        point =(hx-1,hy+1)   #0
    elif position == 1:
        point =(hx,hy+1)     #1
    elif position == 2:
        point =(hx+1,hy+1)   #2
    elif position == 3:
        point =(hx-1,hy)     #3
    elif position == 4:
        point =(hx+1,hy)     #4
    elif position == 5:
        point =(hx-1,hy-1)   #5
    elif position == 6:
        point =(hx+1,hy-1)   #6
    
    
    return point'''
