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
    pCords=np.array([ppos[0],ppos[1]])
    
    #for i in range(8)
    
    point = np.array([x-1,y+1]) #0
    dist = np.linalg.norm(pCords-point)
    distances.append(dist)
    
    point = np.array([x,y+1])   #1
    dist = np.linalg.norm(pCords-point)
    distances.append(dist)

    point = np.array([x+1,y+1]) #2
    dist = np.linalg.norm(pCords-point)
    distances.append(dist)
    
    point = np.array([x-1,y])   #3
    dist = np.linalg.norm(pCords-point)
    distances.append(dist)
    
    point = np.array([x+1,y])   #4
    dist = np.linalg.norm(pCords-point)
    distances.append(dist)

    point = np.array([x-1,y-1])   #5
    dist = np.linalg.norm(pCords-point)
    distances.append(dist)

    point = np.array([x+1,y-1])   #6
    dist = np.linalg.norm(pCords-point)
    distances.append(dist)

    bestdist = min(distances)
    position =distances.index(bestdist)

    if position == 0:
        point =(x-1,y+1)   #0
    elif position == 1:
        point =(x,y+1)     #1
    elif position == 2:
        point =(x+1,y+1)   #2
    elif position == 3:
        point =(x-1,y)     #3
    elif position == 4:
        point =(x+1,y)     #4
    elif position == 5:
        point =(x-1,y-1)   #5
    elif position == 6:
        point =(x+1,y-1)   #6
    
    
    return point
