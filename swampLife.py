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

from hashlib import new
from multiprocessing import popen_fork
from pydoc import cli
import random as rn
from numpy import random
import matplotlib.pyplot as plt
import numpy as np
from swamp import Duck, Newt, Shrimp
import food
import pandas as pd
from matplotlib.colors import ListedColormap
import csv


XMAX = 1000
YMAX = 1000




def createTerrain():
    map = random.randint(2, size=(XMAX,YMAX))
    return map

def getTerrain():
    map = random.randint(2, size=(XMAX,YMAX))
    
    with open("map.csv","w",newline='') as file:
        mywriter = csv.writer(file, delimiter=',')
        mywriter.writerows(map)
    return map

def plotTerrain(map):
    map = pd.read_csv('map.csv')
    cmap = ListedColormap(["green","lightblue"])
    plt.imshow(map,cmap=cmap) 

#plots ducks           
def plotDuck(dList):
    xvalues = []
    yvalues = []
    sizes = []
    for d in dList:
        
        xvalues.append(d.getPos()[0])
        yvalues.append(d.getPos()[1])
        sizes.append(d.getSize())
    
    plt.scatter(xvalues, yvalues, s=sizes, color="yellow")

# plots newts
def plotNewts(nList):
    xvalues = []
    yvalues = []
    sizes = []
    for n in nList:
        
        xvalues.append(n.getPos()[0])
        yvalues.append(n.getPos()[1])
        sizes.append(n.getSize())
    
    plt.scatter(xvalues, yvalues, s=sizes, color="pink")

# plots shrimps
def plotShrimp(sList):
    xvalues = []
    yvalues = []
    sizes = []
    for s in sList:
        
        xvalues.append(s.getPos()[0])
        yvalues.append(s.getPos()[1])
        sizes.append(s.getSize())
    
    plt.scatter(xvalues, yvalues, s=sizes, color="red")
def plotFood(fList):
    xvalues = []
    yvalues = []
    sizes = []
    for f in fList:
        
        xvalues.append(f.getPos()[0])
        yvalues.append(f.getPos()[1])
        sizes.append(2)
    
    plt.scatter(xvalues, yvalues, s=sizes, color="orange")

# moves creatures and ensures
# they say within the plot range
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
    terrain = open('terrain.txt')

def createCreature(creatures,species):
    randX = rn.randint(0,XMAX)
    randY = rn.randint(0,YMAX)
    if species == 'Duck':
        creatures.append(Duck([randX,randY]))
    elif species == 'Newt':
        creatures.append(Newt([randX,randY]))
    elif species == 'Shrimp':
        creatures.append(Shrimp([randX,randY]))

# will add func to make is so new egg
# spawns next to parent and not random
def eggLay(ducks,pos):
    for i in range(len(ducks)):
        newX = None
        newY = None
        randX = rn.randint(1,2)
        randY = rn.randint(1,2)
        
        if randX == 1:
            newX=pos[0]-1
        else:
            newX=pos[0]+1

        if randY == 1:
            newY=pos[1]-1
        else:
            newY=pos[1]+1
        ducks.append(Duck([newX,newY]))

# create new animals if 
# parent is 5 timesteps old        
def repoduction(creatures):
    for i in range(len(creatures)):
        if creatures[i].repoduction()== True:
            createCreature(creatures,creatures[i].getSpec())

# searches to see if any creatures
# are nearby 
# will call pursue funcion if yes
# otherwise will rand move
def search(cList,fList):
    fcords =()
    dist =[]
    for j in range(len(cList)):
        if cList[j].getState()!='egg':
            dist=[]
            
            for i in range(len(fList)):
                cPos = cList[j].getPos()
                pPos = fList[i].getPos()
                dist.append(abs((pPos[0]-cPos[0])+(pPos[1]-cPos[1])))
            if len(dist):
                closest = min(dist)
                clstInd= dist.index(closest)
                if closest <= 200:
                    "Print target located"
                    pursue(cList[j],fList[clstInd],fList)
                    cList[j].ageUp()
                else:
                    
                    moveCrt(cList[j],(XMAX,YMAX))
            else:
               
                moveCrt(cList[j],(XMAX,YMAX))
        else:
            cList[j].ageUp()
            cList[j].ageCheck()

# move hunter creature towards
# prey creature and will kill
# if in range
def pursue(hunter, prey,preyList):
    
    hPos = hunter.getPos()
    pPos = prey.getPos()
    hunter.Hunt(pPos)
    dist =(abs(pPos[0]-hPos[0]))+(abs(pPos[1]-hPos[1]))
    if dist == 1 or dist == 0:
        print("Hunter at :",hPos, " moves in for the kill")
        print("")
        remover(prey,preyList)
        
    

# removes creature from
# there list
def remover(creature,clist):
    index = clist.index(creature)
    print(creature, " has been slain")
    del clist[index]
    

def deathCheck(creatures,foodList):
    deathList =[]
    for i in range (len(creatures)):
        if creatures[i].deathCheck()== True:
            deathList.append(i)
    for creature in deathList[::-1]:
        print(creatures[creature],"has been passed away")
        corpseFood(creatures[creature].getPos(),foodList)
        del creatures[creature]
    
def corpseFood(pos,nectar):
    nectar.append(food.Food((pos[0],pos[1])))
def fillFood(nectar):
    foodamount = rn.randint(1,6)
    for i in range(foodamount):
        randX = rn.randint(0,XMAX)
        randY = rn.randint(0, YMAX)
        nectar.append(food.Food((randX,randY)))

def main():
    
    ducks = []
    newts = []
    shrimps = []
    food = []

    duckAmount = int(input("How many ducks woud you like? "))
    newtAmount = int(input("How many newts woud you like? "))
    shrimpAmount = int(input("How many shrimp woud you like? "))
    time = int(input("How long would you like the simulation to last? "))
    global XMAX 
    XMAX= int(input("What would you like the x boundary to be? "))
    global YMAX 
    YMAX= int(input("What would you like the y boundary to be? "))
    #  create ducks
    for i in range(duckAmount):
        createCreature(ducks,"Duck")
     
    # create newts 
    for i in range(newtAmount):
        createCreature(newts,"Newt")
    
    #create shrimps
    for i in range(shrimpAmount):
        createCreature(shrimps,"Shrimp")
    
    fillFood(food)
    terrain = getTerrain()
    
    #simulte for ten timesteps 
    for w in range(time):
        plotTerrain(terrain)
        print("\n ### TIMESTEP ",w, "###")
        plt.xlim(0,XMAX)
        plt.ylim(0,YMAX)
        
        for i in range(len(ducks)):
            print(ducks[i])

        for q in range(len(newts)):
            print(newts[q])

        for b in range(len(shrimps)):
            print(shrimps[b])

        print("")
        
        deathCheck(ducks,food)
        deathCheck(newts,food)
        deathCheck(shrimps,food)
        repoduction(ducks)
        repoduction(newts)
        repoduction(shrimps)

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
        plotFood(food)
        plotTitle = "### TimeStep ",w, " Ducks: ", len(ducks), " Newts: ", len(newts)," Shrimp: ", len(shrimps)," ###"
        plt.title(plotTitle)
        title2 = "Swamp"+str(w)
        
        plt.savefig(title2+".png")
        plt.pause(1)
        plt.clf()

        print("Duck ages")
        for i in range(len(ducks)):
            print(ducks[i].getAge())
        

''' for i in range(len(ducks)):
            title = ducks[i].getSpec(),ducks[i].getState()
            plt.annotate(title,ducks[i].getPos())

        for i in range(len(newts)):
            plt.annotate(newts[i].getSpec(),newts[i].getPos())

        for i in range(len(shrimps)):
            plt.annotate(shrimps[i].getSpec(),shrimps[i].getPos()) '''

        

    
if __name__ == "__main__":
    print("\nWelcome to the shit show!\n")
    main()
    print("\nThat hurt!\n")