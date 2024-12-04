from sprites import artCache as art
import pyglet as py
import main
import random
GRID_SIZE = 50
class Grid:
    def __init__(self,x,y):
        self.x = x * GRID_SIZE
        self.y = y * GRID_SIZE
        self.color = "gray"
        z = random.randint(0,1000)
        if z>980 and z<995:
            self.state = 3
        elif z>995:
            self.state = 0
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