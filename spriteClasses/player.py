from sprites import artCache as art
import pyglet as py
import variables as var
import random
speed = 1
class Player:
    def __init__(self):
        self.x = 0
        self.y = 0
        self.face=0
        self.state=0
        #0 = U, 1 = D, 2 = L, 3 = R, 4 = UL, 5 = UR, 6 = DL, 7 = DR,
        #self.soul = py.Rect(self.x, self.y, var.GRID_SIZE, var.GRID_SIZE)
            #py.draw.rect(var.WIN, "red", self.soul)
    def key(self,symbol,window):
        if symbol == py.window.key.W:
            self.y+=speed
            self.face = 3
        if symbol == py.window.key.W:
            self.y-=speed
            self.face = 0
        if symbol == py.window.key.D:
            self.x+=speed
            self.face = 7
        if symbol == py.window.key.A:
            self.x-=speed
            self.face = 6
#------------------------------
        if symbol == py.window.key.D&symbol == py.window.key.W:
            self.face=2
        if symbol == py.window.key.A&symbol == py.window.key.W:
            self.face = 1
        if symbol == py.window.key.D&symbol == py.window.key.S:
            self.face=5
        if symbol == py.window.key.A&symbol == py.window.key.S:
            self.face = 4
#-----------------------------------------
        if symbol == py.window.key.Q:
            self.face =+1
            if self.face > 7:
                self.face = 0
        if symbol == py.window.key.E:
            self.face =+1
            if self.face < 0:
                self.face = 7

    def draw(self):
        #self.soul = py.Rect(self.x, self.y, var.GRID_SIZE, var.GRID_SIZE)
        self.body = art.PlayerBaseA[self.face].blit(self.x,self.y)