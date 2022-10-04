import random as rn
import numpy as np 

def Movement():
    xmove=rn.randint(-10,10)
    ymove=rn.randint(-10,10)
    moves=(xmove,ymove)
    return moves

def hunt(hpos,ppos):
    distances =[]
    x = hpos[0]
    y= hpos[1]

    dist = np.linalg.norm(ppos-hpos)
    #for i in range(8)
    point =(x-1,y+1)   #0
    distances.append(ppos-point)
    point =(x,y+1)   #1
    distances.append(ppos-point)
    point =(x+1,y+1)   #2
    distances.append(ppos-point)
    point =(x-1,y)   #3
    distances.append(ppos-point)
    point =(x+1,y)   #4
    distances.append(ppos-point)
    point =(x-1,y-1)   #5
    distances.append(ppos-point)
    point =(x+1,y-1)   #6
    distances.append(ppos-point)

    bestdist = min(distances)
    position =distances.index(bestdist)

    if position == 0:
        point =(x-1,y+1)   #0
    elif position == 1:
        point =(x,y+1)   #1
    elif position == 2:
            point =(x+1,y+1)   #2
    elif position == 3:
        point =(x-1,y)   #3
    elif position == 4:
            point =(x+1,y)   #4
    elif position == 5:
            point =(x-1,y-1)   #5
    elif position == 6:
            point =(x+1,y-1)   #6
    
    
    return point
