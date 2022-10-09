class Food():

    def __init__(self, pos):
        self.xpos =pos[0]
        self.ypos = pos[1]

    def __str__(self):
        pos = (self.xpos,self.ypos)
        return "nectar of the gods @ " + str(pos)
    def getPos(self):
        return(self.xpos, self.ypos)
