import pyglet as py
from pyglet.gl import *
from sprites import artCache as art,soundCache as sound
import random
speed = 50

def randStep():
    r = random.randint(1, 3)
    if r==1:
        sound.step1.play()
    elif r==2:
        sound.step2.play()
    elif r==3:
        sound.step3.play()
class Player:
    def __init__(self):
        self.x = 0
        self.inter =0
        self.y = 0
        self.face = 0
        self.state = 0
        self.targetX = [0]
        self.targetY = [0]
        self.target = False
        self.noMove = 0
        # items
        self.materials = {"Krovavik Berries": 0,
                          "Krovavik Berries (Corrupted)": 0,
                          "Fertilizer": 20,
                          "Drachni":4,
                          "PLACEHOLDER BERRIES": 0,
                          }
        self.tools = {"Free":0,"Hoe":1}
        self.workStations = {
            "Blacksmith": 0,
                             }
        # 0 = U, 1 = D, 2 = L, 3 = R, 4 = UL, 5 = UR, 6 = DL, 7 = DR,
        # self.soul = py.Rect(self.x, self.y, var.GRID_SIZE, var.GRID_SIZE)
        # py.draw.rect(var.WIN, "red", self.soul)

    def key(self, symbol):
        # ------------------------------
        if symbol == py.window.key.D & symbol == py.window.key.W:
            self.face = 2
            self.noMove = 0
        elif symbol == py.window.key.A & symbol == py.window.key.W:
            self.face = 1
            self.noMove = 0
        elif symbol == py.window.key.D & symbol == py.window.key.S:
            self.face = 5
            self.noMove = 0
        elif symbol == py.window.key.A & symbol == py.window.key.S:
            self.face = 4
            self.noMove = 0
        # -----------------------------------------
        elif symbol == py.window.key.S:
            self.y -= speed
            self.face = 3
            self.noMove = 0
            randStep()
        elif symbol == py.window.key.W:
            self.y += speed
            self.face = 0
            self.noMove = 0
            randStep()
        elif symbol == py.window.key.D:
            self.x += speed
            self.face = 7
            self.noMove = 0
            randStep()
        elif symbol == py.window.key.A:
            self.x -= speed
            self.face = 6
            self.noMove = 0
            randStep()
        # print(f"x: {self.x}, y: {self.y}")
        # ----------------------------------------------
        if symbol == py.window.key.Q:
            self.face = +1
            if self.face > 7:
                self.face = 0
        if symbol == py.window.key.E:
            self.face = +1
            if self.face < 0:
                self.face = 7

    def draw(self):
        line = []
        circle = []
        self.noMove += 1
        if self.target == True:
            self.noMove = 0
            i = 0
            if self.targetX[i] > self.x:
                self.x += speed
                self.face = 7
            elif self.targetX[i] < self.x:
                self.x -= speed
                self.face = 6
            if self.targetY[i] > self.y:
                self.y += speed
                self.face = 0
            elif self.targetY[i] < self.y:
                self.y -= speed
                self.face = 3
            # stuff
            if self.targetX[i] > self.x and self.targetY[i] > self.y:
                self.face = 2
            if self.targetX[i] < self.x and self.targetY[i] > self.y:
                self.face = 1
            if self.targetX[i] > self.x and self.targetY[i] < self.y:
                self.face = 5
            if self.targetX[i] < self.x and self.targetY[i] < self.y:
                self.face = 4
            if self.inter == 0:
                randStep()
            self.inter += 1
            if self.inter == 1:
                self.inter = 0
            lineWidth = 4
            lineColor = (100, 0, 0)
            for ii in range(len(self.targetX)):
                glBlendFunc(GL_SRC_ALPHA, GL_ONE_MINUS_SRC_ALPHA)
                if ii == 0:
                    circle.append(
                        py.shapes.Circle(self.targetX[ii] + 25, self.targetY[ii] + 25, lineWidth, 10, lineColor))
                    line.append(py.shapes.Line(self.x + 25, self.y + 25, self.targetX[ii] + 25, self.targetY[ii] + 25,
                                               lineWidth, color=lineColor))
                elif ii > 0:
                    circle.append(
                        py.shapes.Circle(self.targetX[ii] + 25, self.targetY[ii] + 25, lineWidth, 10, lineColor))
                    line.append(
                        py.shapes.Line(self.targetX[ii - 1] + 25, self.targetY[ii - 1] + 25, self.targetX[ii] + 25,
                                       self.targetY[ii] + 25, lineWidth, color=lineColor))

            if self.targetX[i] == self.x and self.targetY[i] == self.y:
                if len(self.targetX) == 1 and len(self.targetY) == 1:
                    self.target = False
                    #print("exit")
                if len(self.targetX) > 1:
                   #print("pop x")
                    self.targetX.pop(0)
                if len(self.targetY) > 1:
                    self.targetY.pop(0)
                    #print("pop y")
        # self.soul = py.Rect(self.x, self.y, var.GRID_SIZE, var.GRID_SIZE)
        for i in range(len(line)):
            line[i].draw()
            circle[i].draw()
        glEnable(GL_BLEND)
        glBlendFunc(GL_SRC_ALPHA, GL_ONE_MINUS_SRC_ALPHA)
        self.body = art.PlayerBaseA[self.face].blit(self.x, self.y)
