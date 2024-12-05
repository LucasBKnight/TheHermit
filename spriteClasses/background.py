from sprites import artCache as art
import pyglet as py
import variables as var
import random
class GridClass:
    def __init__(self,x,y):
        self.x = x
        self.y = y
        self.color = "gray"
        z = random.randint(0,1000)
        if z>980 and z<995:
            self.state = 0
        elif z>995:
            self.state = 1
        else:
            self.state = 0
        #self.sprite = py.sprite.Sprite.add()
    def draw(self):
        #grass tile
        if self.state == 0:
            art.GrassTile1.blit(self.x,self.y)
        elif self.state == 1:
            art.CorruptGrassTile1.blit(self.x,self.y)
        #Constructables
        elif self.state == 2:
            art.WallTile1.blit(self.x, self.y)
        elif self.state == 3:
            art.SmithyLVL1.blit(self.x, self.y)

