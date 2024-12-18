import random

import pyglet as py
from pyglet.gl import *

import variables as var
from sprites import artCache as art


class GridClass:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.color = "gray"
        self.crop = False
        self.isTilled = False
        self.state = 0
        z = random.randint(0, 1010)
        if z < 995:
            self.state = 0
        elif z < 1000:
            self.state = 1
        else:
            self.crop = True
            self.cropType = 0
            self.ripe = True
            self.fertile = False
            self.Cstate = False
        # self.sprite = py.sprite.Sprite.add()

    def draw(self):
        # grass tile
        glEnable(GL_BLEND)
        glBlendFunc(GL_SRC_ALPHA, GL_ONE_MINUS_SRC_ALPHA)
        if self.crop is False:
            if self.isTilled is True:
                art.TILE_PLACEHOLDER.blit(self.x, self.y)
            else:
                if self.state == 0:
                    art.GrassTile1.blit(self.x, self.y)
                elif self.state == 1:
                    art.CorruptGrassTile1.blit(self.x, self.y)
                # Constructables
                elif self.state == 2:
                    art.WallTile1.blit(self.x, self.y)
                elif self.state == 3:
                    art.SmithyLVL1.blit(self.x, self.y)
        elif self.crop is True:
            # plant type?
            if self.cropType == 0:
                # Krovavik
                art.KrovavikTile.blit(self.x, self.y)
            # ripe Checks
            if self.ripe == True:
                art.RipeMarker.blit(self.x + var.GRID_SIZE - 10, self.y + var.GRID_SIZE - 10)
                self.Cstate = False
            elif self.fertile == True:
                art.FertileMarker.blit(self.x + var.GRID_SIZE - 10, self.y + var.GRID_SIZE - 10)
                if self.Cstate == False:
                    print("Clock Time")
                    py.clock.schedule_once(lambda dt: (setattr(self, 'fertile', False), setattr(self, 'ripe', True)), 5)
