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

from multiprocessing import popen_fork
import random
#from turtle import color
import matplotlib.pyplot as plt
import numpy as np
#import time
from swamp import Duck, Newt, Shrimp
import terrainCreator as tc

terrain = tc.creatMap()

XMAX = 1000
YMAX = 1000
b = np.zeros((XMAX,YMAX))

def plotTerrain(map):
    #rock = 1
    # shallows = 2,3
    # deepWater = 4 
    # land = 5
    rocks=[]
    shallows=[]
    deepWater=[]
    lans=[]
    xvalues = []
    yvalues = []
    
    for i in range(1000):
        for j in range(1000):
            if map[i][j]== 1:
                xvalues.append(map[i])
                yvalues.append(map[j])
    plt.scatter(xvalues,yvalues, color='gray')

    for i in range(1000):
        for j in range(1000):
            if map[i][j]== 2 or map[i][j]==3:
                xvalues.append(map[i])
                yvalues.append(map[j])
    plt.scatter(xvalues,yvalues, color='lightblue')
    
    for i in range(1000):
        for j in range(1000):
            if map[i][j]== 4:
                xvalues.append(map[i])
                yvalues.append(map[j])
    plt.scatter(xvalues,yvalues, color='darkBlue')
    
    for i in range(1000):
        for j in range(1000):
            if map[i][j]== 5:
                xvalues.append(map[i])
                yvalues.append(map[j])
    plt.scatter(xvalues,yvalues, color='brown')
    
            
def plotDuck(dList):
    xvalues = []
    yvalues = []
    sizes = []
    for d in dList:
        #print(d)
        xvalues.append(d.getPos()[0])
        yvalues.append(d.getPos()[1])
        sizes.append(d.getSize())
    
    plt.scatter(xvalues, yvalues, s=sizes, color="blue")

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
    
    plt.scatter(xvalues, yvalues, s=sizes, color="red")

def moveCrt(creature,limits):
    x=0
    y=0
  
    while(True):
        xy =creature.getPos()
        creature.stepChange()
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

# will add func to make is so new egg
# spawns next to parrent and not random
# def eggLay():

def search(cList,fList):
    fcords =()
    for j in range(len(cList)):
        for i in range(len(fList)):
            if cList[j].inRange(fList[i].getPos())==True:
                cList[j].Hunt(fList[i].getPos())
                print(cList[j], " is on the hunt")
                cPos = cList[j].getPos()
                pPos = fList[i].getPos()
                xDiff = abs(cPos[0]-pPos[0])
                yDiff = abs(cPos[1]-pPos[1])
                if xDiff == 0 or xDiff == 1:
                    if yDiff == 0 or yDiff == 1:
                        #call remover code
                        print("hi")
                        remover(fList[i],fList)

            else:
                moveCrt(cList[j],(XMAX,YMAX))

def remover(creature,clist):
    index = clist.index(creature)
    print(creature, " has been slain")
    del clist[index]

def main():
    
    ducks = []
    newts = []
    shrimps = []
    food = []
    #  create ducks
    for i in range(5):
        createCreature(ducks,"Duck")
     
    # create newts 
    for i in range(10):
        createCreature(newts,"Newt")
    
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
        search(ducks,newts)
        search(newts,shrimps)
        search(shrimps,food)
#        for i in range(len(ducks)):
#            moveCrt(ducks[i],(XMAX, YMAX))
#        for i in range(len(newts)):
#            moveCrt(newts[i],(XMAX, YMAX))
#        for i in range(len(shrimps)):
#            moveCrt(shrimps[i],(XMAX, YMAX))

        plotDuck(ducks)
        plotNewts(newts)
        plotShrimp(shrimps)

        for i in range(len(ducks)):
            plt.annotate(ducks[i].getState(),ducks[i].getPos())
        for i in range(len(newts)):
            plt.annotate(newts[i].getState(),newts[i].getPos())
        for i in range(len(shrimps)):
            plt.annotate(shrimps[i].getState(),shrimps[i].getPos())
        plt.pause(1)
        plt.clf()

    
if __name__ == "__main__":
    print("\nShe turned me into a newt!\n")
    main()
    print("\nI got better!\n")
