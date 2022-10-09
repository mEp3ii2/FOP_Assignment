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
from pydoc import cli
import random as rn
#from turtle import title
#from turtle import color
import matplotlib.pyplot as plt
import numpy as np
#import time
from swamp import Duck, Newt, Shrimp
import terrainCreator as tc
import food
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
    
#plots ducks           
def plotDuck(dList):
    xvalues = []
    yvalues = []
    sizes = []
    for d in dList:
        
        xvalues.append(d.getPos()[0])
        yvalues.append(d.getPos()[1])
        sizes.append(d.getSize())
    
    plt.scatter(xvalues, yvalues, s=sizes, color="blue")

# plots newts
def plotNewts(nList):
    xvalues = []
    yvalues = []
    sizes = []
    for n in nList:
        
        xvalues.append(n.getPos()[0])
        yvalues.append(n.getPos()[1])
        sizes.append(n.getSize())
    
    plt.scatter(xvalues, yvalues, s=sizes, color="green")

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
    
    plt.scatter(xvalues, yvalues, s=sizes, color="purple")

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
                    print("no one in range for this little", cList[j].getSpec(),j)
                    moveCrt(cList[j],(XMAX,YMAX))
            else:
                print("no one in range for this little", cList[j].getSpec(),j)
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
    print("Hunter is on the prowl at :",hPos, "target pos: ", pPos)
    dist =(abs(pPos[0]-hPos[0]))+(abs(pPos[1]-hPos[1]))
    if dist == 1 or dist == 0:
        remover(prey,preyList)
        print("Hunter at :",hPos, " moves in for the kill")
    print("final pos", hunter.getPos())

# removes creature from
# there list
def remover(creature,clist):
    index = clist.index(creature)
    print(creature, " has been slain")
    del clist[index]
    

def deathCheck(creatures):
    deathList =()
    for i in range (len(creatures)):
        if creatures[i].deathCheck()== True:
            deathList.append(i)
    for creature in deathList[::-1]:
        print(creatures[creature],"has been passed away")
        del creatures[creature]
    

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

    #  create ducks
    for i in range(5):
        createCreature(ducks,"Duck")
     
    # create newts 
    for i in range(10):
        createCreature(newts,"Newt")
    
    #create shrimps
    for i in range(10):
        createCreature(shrimps,"Shrimp")
    
    fillFood(food)
     
    #simulte for ten timesteps 
    for w in range(10):

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
        plt.pause(3)
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