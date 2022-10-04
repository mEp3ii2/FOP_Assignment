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

#from turtle import pos
import Movement as mv

class Animal():

    myclass = 'Animal'
    def __init__(self, pos):
        self.xpos = pos[0]
        self.ypos = pos[1]
        self.age = 0
        self.speed = 10
    
    def __str__(self):
        return self.state + " @ " + str(self.pos)

    def getState(self):
        return self.state
    
    def getPos(self):
        return(self.xpos, self.ypos)
    
    def setPos(self,pos):
        self.xpos = pos[0]
        self.ypos = pos[1]

    def getSize(m):
        return 10
    
    def stepChange(self):
        self.age += 1
        moves = mv.Movement()
        xmov = moves[0]
        ymov = moves[1]
        self.xpos = xmov
        self.ypos = ymov
    
    def repoduction(self):
        if self.age == 5:
            return True

    def deathCheck(self):
        if self.age == 10:
            return True
    
    def getPos(self):
        return self.pos
     
    def inRange(self, cpos):
        wCords = self.getPos()
        wXmin = wCords[0]-50
        wXmax = wCords[0]+50
        wYmin = wCords[1]-50
        wYmax = wCords[1]+50   
        if wXmin<= cpos[0] and cpos[0] <= wXmax:
            if wYmin<= cpos[1] and cpos[1] <=wYmax:
                return True
    
    def Hunt(self, Ppos):
        for i in range(self.speed):
            self.pos=mv.hunt(self.pos,Ppos)

#duck class
class Duck(Animal):

    time2hatch = 4
    states = ["egg","adult"]
    
    #duck init
    def __init__(self, pos):
        self.pos = pos
        self.age = 0
        self.speed = 11
        self.state = self.states[0]

    def __str__(self):
       super().__init__(self)
       
    def inRange(self, cpos):
        wCords = self.getPos()
        wXmin = wCords[0]-50
        wXmax = wCords[0]+50
        wYmin = wCords[1]-50
        wYmax = wCords[1]+50   
        if wXmin<= cpos[0] and cpos[0] <= wXmax:
            if wYmin<= cpos[1] and cpos[1] <=wYmax:
                return True

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
            self.xpos = xmov
            self.ypos = ymov
                        
    def getSize(m):
        if m.state == "egg":
            size = 5
        else:
            size = 15
        return size

class Newt(Animal):

    state = "newt"
    
    def __init__(self, pos):
        self.xpos = pos[0]
        self.ypos = pos[1]
        self.age = 0
        self.speed = 10
    def getPos(self):
        return(self.xpos, self.ypos)

class Shrimp(Animal):
    state = "shrimp"
    
    def __init__(self, pos):
        self.xpos = pos[0]
        self.ypos = pos[1]
        self.age = 0
        self.speed = 11
    
    def getPos(self):
        return(self.xpos, self.ypos)
   

                        
