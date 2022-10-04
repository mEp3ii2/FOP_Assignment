#
# Author : 
# ID : 
#
# swamp.py - Class definitions for simulation of swamp life
#
# Revisions: 
#
# 01/09/2022 – Base version for assignment
#

from turtle import pos
import Movement as mv

class Animal():

    myclass = 'Animal'
    def __init__(self, pos):
        self.pos = pos
        self.age = 0
    
    def __str__(self):
        return self.state + " @ " + str(self.pos)
    def getState(self):
        return self.state

    def getSize(m):
        return 10
    
    def stepChange(self):
        self.age += 1
        moves = mv.Movement()
        xmov = moves[0]
        ymov = moves[1]
        self.pos[0] -= xmov
        self.pos[1] -= ymov
    
    def repoduction(self):
        if self.age == 5:
            return True

    def deathCheck(self):
        if self.age == 10:
            return True
    
    def getPos(self):
        return self.pos
     
    def inRange(self, pos):
        wCords = self.getPos()
        wXmin = wCords[0]-50
        wXmax = wCords[0]+50
        wYmin = wCords[1]-50
        wYmax = wCords[1]+50   
        if wXmin<= pos[0] and pos[0] <= wXmax:
            if wYmin<=pos[1] and pos[1] <=wYmax:
                return True
    def Hunt(self, pos):
        print("on the hunt")
#duck class
class Duck(Animal):
    time2hatch = 4
    states = ["egg","adult"]
    
    #duck init
    def __init__(self, pos):
        self.pos = pos
        self.age = 0
        self.state = self.states[0]

    def __str__(self):
       super().__init__(self)

    #increases age of duck
    #check if ready to hatch
    #
    def stepChange(self):
        self.age += 1
        if self.state == "egg":
            if self.age > self.time2hatch:
                self.state = "adult"
        else:
            moves = mv.Movement()
            xmov = moves[0]
            ymov = moves[1]
            self.pos[0] += xmov
            self.pos[1] += ymov
                        
    def getSize(m):
        if m.state == "egg":
            size = 5
        else:
            size = 15
        return size

class Newt(Animal):

    state = "newt"

class Shrimp(Animal):

    state = "shrimp"

                        
