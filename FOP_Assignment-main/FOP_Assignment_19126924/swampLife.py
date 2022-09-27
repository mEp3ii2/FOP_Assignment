#
# Author : 
# ID : 
#
# swampLife.py - Basic simulation of swamp life for assignment, S2 2022. 
#
# Revisions: 
#
# 01/09/2022 – Base version for assignment
#

import random
import matplotlib.pyplot as plt
import numpy as np
import time
from swamp import Duck, Newt, Shrimp

XMAX = 1000
YMAX = 1000
b = np.zeros((XMAX,YMAX))

def plotDuck(dList):
    xvalues = []
    yvalues = []
    sizes = []
    for d in dList:
        #print(d)
        xvalues.append(d.getPos()[0])
        yvalues.append(d.getPos()[1])
        sizes.append(d.getSize())
    
    plt.scatter(xvalues, yvalues, s=sizes, color="orange")

def plotNewts(nList):
    xvalues = []
    yvalues = []
    sizes = []
    for n in nList:
        #print(d)
        xvalues.append(n.getPos()[0])
        yvalues.append(n.getPos()[1])
        sizes.append(n.getSize())
    
    plt.scatter(xvalues, yvalues, s=sizes, color="green")

def plotShrimp(sList):
    xvalues = []
    yvalues = []
    sizes = []
    for s in sList:
        #print(d)
        xvalues.append(s.getPos()[0])
        yvalues.append(s.getPos()[1])
        sizes.append(s.getSize())
    
    plt.scatter(xvalues, yvalues, s=sizes, color="orange")

def moveCrt(objList,limits):
    x=0
    y=0

    for o in objList:
        while(True):
            xy =o.super().getPos()
            o.stepChange()
            x = xy[0]
            y = xy[1]
            if x < limits[0] and x > 0:
                if y < limits[1] and y >0:
                    break
            x = xy[0]
            y = xy[1]
	    		
def terrainload():
    print(b)
    terrain = open('terrain.txt')

def createCreature(creatures,species):
    randX = random.randint(0,XMAX)
    randY = random.randint(0,YMAX)
    if species == 'Duck':
        creatures.append(Duck([randX,randY]))
    elif species == 'Newt':
        creatures.append(Newt([randX,randY]))
    elif species == 'Shrimp':
        creatures.append(Shrimp([randX,randY]))
def main():
    
    ducks = []
    newts = []
    shrimps = []

    #  create ducks
    for i in range(5):
        createCreature(ducks,"Duck")
     
    # create newts 
    for i in range(10):
        createCreature(newts,"Newts")
    
    #create shrimps
    for i in range(10):
        createCreature(shrimps,"Shrimp")
     
     
    #simulte for ten timesteps 
    for i in range(10):
        print("\n ### TIMESTEP ",i, "###")
        plt.xlim(0,XMAX)
        plt.ylim(0,YMAX)
        
        for j in range(len(ducks)):
            if ducks[j].repoduction() == True:
                createCreature(ducks,"Duck")
        
        moveCrt(ducks,(XMAX,YMAX))
        moveCrt(newts,(XMAX,YMAX))
        moveCrt(shrimps,(XMAX,YMAX))

        plotDuck(ducks)
        plotNewts(newts)
        plotShrimp(shrimps)

        plt.pause(1)
        plt.clf()

    
if __name__ == "__main__":
    print("\nShe turned me into a newt!\n")
    main()
    print("\nI got better!\n")
