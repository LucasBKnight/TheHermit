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
        z = random.randint(0, 1010)
        if z < 995:
            self.state = 0
        elif z < 1000:
            self.state = 1
        else:
            self.state = 4
            self.crop = True
            self.cropType = 0
            self.ripe = True
            self.fertile = True
            self.state = False
        # self.sprite = py.sprite.Sprite.add()

    def draw(self):
        # grass tile
        glEnable(GL_BLEND)
        glBlendFunc(GL_SRC_ALPHA, GL_ONE_MINUS_SRC_ALPHA)
        if self.crop == False:
            if self.state == 0:
                art.GrassTile1.blit(self.x, self.y)
            elif self.state == 1:
                art.CorruptGrassTile1.blit(self.x, self.y)
            # Constructables
            elif self.state == 2:
                art.WallTile1.blit(self.x, self.y)
            elif self.state == 3:
                art.SmithyLVL1.blit(self.x, self.y)
        elif self.crop == True:
            # plant type?
            if self.cropType == 0:
                # Krovavik
                art.TILE_PLACEHOLDER.blit(self.x, self.y)
            # ripe Checks
            if self.ripe == True:
                art.RipeMarker.blit(self.x + var.GRID_SIZE - 10, self.y + var.GRID_SIZE - 10)
                self.state = False
            elif self.fertile == True:
                art.FertileMarker.blit(self.x + var.GRID_SIZE - 10, self.y + var.GRID_SIZE - 10)
                if self.state == False:
                    py.clock.schedule_once(lambda dt: (setattr(self, 'ripe', True), setattr(self, 'fertile', False)), 5)
