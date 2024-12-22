import math
import random
import sys

import pyglet as py
from pyglet.gl import *

import variables as var
from spriteClasses import background, player, menuWindows as inv
from sprites import artCache as art, soundCache as sound

# main window
WIN = py.window.Window(width=var.WIN_WIDTH, height=var.WIN_HEIGHT, caption="The Hermit")
WIN.set_icon(art.ChemIcon)
WIN.set_visible(True)
# inventory Window
INV_CLASS = inv.menu()
INV = py.window.Window(width=var.INV_WIDTH, height=var.INV_HEIGHT, caption="Inventory")
INV.set_icon(art.ChemIcon)
INV.set_visible(True)

# build window
CON_CLASS = inv.conmenu()
CON = py.window.Window(width=var.CON_WIDTH, height=var.CON_HEIGHT, caption="Build Menu")
CON.set_icon(art.ChemIcon)
CON.set_visible(True)
# CON.set_location(var.WIN_WIDTH * (5 / 8) + 50, var.WIN_HEIGHT)
CRA_CLASS = inv.menu()
CRA = py.window.Window(width=var.CON_WIDTH, height=var.CON_HEIGHT, caption="Build Menu")
CRA.set_icon(art.ChemIcon)
CRA.set_visible(False)
# grid
GRID = []
Player = player.Player()


def grid_setup():
    for i in range(int(var.WIN_HEIGHT / var.GRID_SIZE)):
        for ii in range(int(var.WIN_WIDTH / var.GRID_SIZE)):
            GRID.append(background.GridClass(ii * var.GRID_SIZE, i * var.GRID_SIZE))
            # print(f"Created Tile @({ii*var.GRID_SIZE},{i*var.GRID_SIZE})")
    # print(GRID)


# --------------------------------------------------------
# GLOBAL WINDOW HANDLERS
# --------------------------------------------------------
def GLO_key(symbol):
    Player.key(symbol)
    global map_State
    if symbol == py.window.key.ASCIITILDE:
        WIN.clear()
        # CRA.set_visible(True)
    if symbol == py.window.key.I:
        INV_CLASS.show()
        WIN.set_visible(False)
        WIN.set_visible(True)
    INV.set_visible(INV_CLASS.is_shown())
    if symbol == py.window.key.B:
        CON_CLASS.show()
        WIN.set_visible(False)
        WIN.set_visible(True)
    CON.set_visible(CON_CLASS.is_shown())
    if symbol == py.window.key.EQUAL:
        # Player.materials["Krovavik Berries"] += 1
        # print(Player.materials)
        map_State = 1
    if symbol == py.window.key.PLUS:
        Player.materials["PLACEHOLDER BERRIES"] += 1
        print(Player.materials)
    # escape exit (change to pause screen ast some point)
    if symbol == py.window.key.ESCAPE:
        WIN.close()
        INV.close()
        CON.close()
        py.app.exit()
        sys.exit()


def GLO_clear():
    WIN.clear()


# --------------------------------------------------------
# INVENTORY WINDOW HANDLERS
# --------------------------------------------------------
@INV.event
def on_key_press(symbol, modifiers):
    GLO_key(symbol)

INV_workToTool = 0
INV_workToTool_max = 1
INV_S = py.media.Player()
@INV.event
def on_mouse_press(x, y, button, modifiers):
    global INV_workToTool
    if INV_workToTool==0:
        if var.INV_WIDTH/2+80<x<var.INV_WIDTH/2+105:
            if 200>y>170:
                INV_S.delete()
                INV_S.queue(sound.click)
                INV_S.play()
                INV_workToTool+=1
    if INV_workToTool== 1:
        if var.INV_WIDTH/2-80>x>var.INV_WIDTH/2-105:
            if 200>y>170:
                INV_S.delete()
                INV_S.queue(sound.click)
                INV_S.play()
                INV_workToTool-=1
@INV.event
def on_draw():
    glEnable(GL_BLEND)
    GLO_clear()
    INV.clear()
    INV_sort = sorted(Player.materials.items(), key=lambda x: x[1], reverse=True)
    INV_ord = dict(INV_sort)
    index = 0
    indexx = 0
    for i in INV_ord:
        if INV_ord[i] > 0:
            index += 1
            label = py.text.Label(f"{i}: {Player.materials[i]}",
                                  font_name='Times New Roman',
                                  font_size=10,
                                  x=25 + indexx, y=var.INV_HEIGHT - (25 * index),
                                  anchor_x='left', anchor_y='top')
            label.draw()
            if i == "Krovavik Berries":
                glEnable(GL_BLEND)
                glBlendFunc(GL_SRC_ALPHA, GL_ONE_MINUS_SRC_ALPHA)
                art.KrakovikBerryINV.blit(10 + indexx, var.INV_HEIGHT - (25 * index) - 12)
            elif i == "Fertilizer":
                glEnable(GL_BLEND)
                glBlendFunc(GL_SRC_ALPHA, GL_ONE_MINUS_SRC_ALPHA)
                art.FertilizerINV.blit(10 + indexx, var.INV_HEIGHT - (25 * index) - 12)
            elif i == "Krovavik Berries (Corrupted)":
                glEnable(GL_BLEND)
                glBlendFunc(GL_SRC_ALPHA, GL_ONE_MINUS_SRC_ALPHA)
                art.KrakovikBerryCOR.blit(10 + indexx, var.INV_HEIGHT - (25 * index) - 12)
            elif i == "Drachni":
                glEnable(GL_BLEND)
                glBlendFunc(GL_SRC_ALPHA, GL_ONE_MINUS_SRC_ALPHA)
                art.CoinINV.blit(10 + indexx, var.INV_HEIGHT - (25 * index) - 12)
            elif i == "Dirt":
                glEnable(GL_BLEND)
                glBlendFunc(GL_SRC_ALPHA, GL_ONE_MINUS_SRC_ALPHA)
                art.DirtINV.blit(10 + indexx, var.INV_HEIGHT - (25 * index) - 12)
        if var.INV_HEIGHT - (25 * index) - 12 < 200:
            index = 0
            indexx = var.INV_WIDTH / 2
    j = 1
    yOffWork = -100
    joff = 65
    global INV_workToTool
    if INV_workToTool == 0:
        py.text.Label(f"Workstations",
                      font_name='Times New Roman',
                      font_size=20,
                      x=var.INV_WIDTH/2, y=200,
                      anchor_x='center', anchor_y='top').draw()
        py.shapes.Triangle(var.INV_WIDTH/2+100,185,var.INV_WIDTH/2+85,195,var.INV_WIDTH/2+85,175,(250,250,250)).draw()
        for i in Player.workStations:
            if Player.workStations[i] > 0:
                if i == "Blacksmith":
                    art.SmithyLVL1.blit(j*joff-25,200+yOffWork)
                else:
                    art.TILE_PLACEHOLDER.blit(j*joff-25,200+yOffWork)
                py.text.Label(f"{i} {Player.workStations[i]}",
                                      font_name='Times New Roman',
                                      font_size=10,
                                      x=j*joff, y=200+yOffWork,
                                      anchor_x='center', anchor_y='top').draw()
                j += 1
                if j * joff > var.INV_WIDTH:
                    yOffWork -= 100
    if INV_workToTool == 1:
        py.text.Label(f"Tools",
                              font_name='Times New Roman',
                              font_size=20,
                              x=var.INV_WIDTH / 2, y=200,
                              anchor_x='center', anchor_y='top').draw()
        py.shapes.Triangle(var.INV_WIDTH / 2 - 100, 185, var.INV_WIDTH / 2 - 85, 195, var.INV_WIDTH / 2 - 85,
                                   175, (250, 250, 250)).draw()
        for i in Player.tools:
            if Player.tools[i] > 0:
                if i == "Blacksmith":
                    art.SmithyLVL1.blit(j * joff - 25, 200 + yOffWork)
                else:
                    art.TILE_PLACEHOLDER.blit(j * joff - 25, 200 + yOffWork)
                py.text.Label(f"{i} {Player.tools[i]}",
                                      font_name='Times New Roman',
                                      font_size=10,
                                      x=j * joff, y=200 + yOffWork,
                                      anchor_x='center', anchor_y='top').draw()
                j += 1
                if j*joff > var.INV_WIDTH:
                    yOffWork-=100

# --------------------------------------------------------
# BUILD WINDOW HANDLERS
# --------------------------------------------------------
# @CON.event
# def on_show():
# bello
# print()

@CON.event()
def on_key_press(symbol, modifiers):
    GLO_key(symbol)


class fert:
    def __init__(self, x, y, title, textArt, PlayerDict, DictType, LvlOrAmn_sub,LvlOrAmn_dom, introTxt,visible):
        self.x = x
        self.y = y
        self.Col = (255, 255, 255)
        self.SubCol = (255, 255, 255)
        self.build = False
        self.title = title
        self.textArt = textArt
        self.PlayerDict = PlayerDict
        self.DictType = DictType
        self.LvlOrAmn = LvlOrAmn_sub
        self.introTxt = introTxt
        self.visible = visible
        self.cap = LvlOrAmn_dom

    def ConText(self):
        if self.PlayerDict[self.DictType] < self.LvlOrAmn:
            self.SubCol = (100, 0, 0)
        else:
            self.SubCol = (255, 255, 255)
        #if not self.cap>lvl>self.LvlOrAmn:
        #    self.visible = False
        if self.visible is True:
            fertlilizeMain = py.text.Label(f"{self.title}",
                                           font_name='Times New Roman',
                                           font_size=20,
                                           x=self.x, y=self.y,
                                           anchor_x='center', anchor_y='bottom', color=self.Col)
            fertlilizeSub = py.text.Label(f"{self.introTxt} {self.LvlOrAmn}/{self.PlayerDict[self.DictType]}",
                                          font_name='Times New Roman',
                                          font_size=10,
                                          x=self.x - 5, y=self.y - 15,
                                          anchor_x='center', anchor_y='bottom', color=self.SubCol)
            glEnable(GL_BLEND)
            glBlendFunc(GL_SRC_ALPHA, GL_ONE_MINUS_SRC_ALPHA)
            self.textArt.blit(self.x + fertlilizeSub.content_width/2, self.y - 13)
            fertlilizeMain.draw()
            fertlilizeSub.draw()

    def clicked(self, x, y):
        global CON_var
        if x > self.x - 50 and x < self.x + 50 and y > self.y - 50 and y < self.y + 50 and self.visible is True:
            for i in CON_var:
                if CON_var[i].build is True and CON_var[i] != self:
                    CON_var[i].build = False
                    CON_var[i].Col = (255, 255, 255)
            if not self.build:
                self.Col = (100, 0, 0)
                self.build = True
                # print("false")
            else:
                self.Col = (255, 255, 255)
                self.build = False
                print("aaa")
            print(self)
            INV_S.delete()
            INV_S.queue(sound.click)
            INV_S.play()


class PLbutton:
    def __init__(self,x,y,material):
        self.x = x
        self.y = y
        self.material = material
        #self.text = text
        self.active = False
        self.Col = (255, 255, 255)
    def clicked(self, x, y):
        if x > self.x - 50 and x < self.x + 50 and y > self.y - 50 and y < self.y + 50:
            for i in planting_sub.values():
                if i.active is True and i != self:
                    i.active = False
                    i.Col = (255, 255, 255)
            if not self.active:
                self.Col = (100, 0, 0)
                self.active = True
                planting.introTxt = self.material
                planting.DictType = self.material
                planting.textArt = art.INV_sorter(self.material)
                print("false")
            else:
                self.Col = (255, 255, 255)
                self.active = False
                print("aaa")
            print(self)
            INV_S.delete()
            INV_S.queue(sound.click)
            INV_S.play()
    def draw(self):
        if Player.materials[self.material] >= 1:
            py.text.Label(f"{self.material}",
                          font_name='Times New Roman',
                          font_size=10,
                          x=self.x, y=self.y,
                          anchor_x='center', anchor_y='bottom', color=self.Col).draw()
CON_var = {
    "Fertil": fert(100, var.CON_HEIGHT - 40, "Fertilize", art.FertilizerINV, Player.materials, "Fertilizer", 1,100, "Uses",True),
    "Smith": fert(100, var.CON_HEIGHT - 120, "Blacksmith", art.INV_Smiles, Player.tools, "Free", 0,2, "Free",True),
    "Till": fert(200, var.CON_HEIGHT - 40,"Till",art.INV_Smiles,Player.tools,"Hoe",1,100,"Hoe",True)
        }
planting = fert(var.CON_WIDTH/2, var.CON_HEIGHT - 40,"Planting",art.INV_Smiles,Player.materials,"Dirt",1,100,"Seeds",True)
planting_sub = {
    "Krovavik Berry" : PLbutton(100,var.CON_HEIGHT - 100,"Krovavik Berries"),
}
CON_S = py.media.Player()
@CON.event
def on_mouse_press(x, y, button, modifiers):
    # menu Page 0
    if CON_CLASS.page == 0:
        if button == pyglet.window.mouse.LEFT:
            # fertilizer
            for i in CON_var.values():
                i.clicked(x,y)
    if CON_CLASS.page == 2:
        planting.clicked(x,y)
        for i in planting_sub.values():
            i.clicked(x, y)
    if CON_CLASS.page < CON_CLASS.MaxPage - 1 and button == pyglet.window.mouse.LEFT and x < var.CON_WIDTH - 5 and x > var.CON_WIDTH - 25 and y < var.CON_HEIGHT / 2 + 15 and y > var.CON_HEIGHT / 2 - 15:
        CON_CLASS.page += 1
        CON_S.delete()
        CON_S.queue(sound.click)
        CON_S.play()
    if CON_CLASS.page > 0 and button == pyglet.window.mouse.LEFT and x > 5 and x < 25 and y < var.CON_HEIGHT / 2 + 15 and y > var.CON_HEIGHT / 2 - 15:
        CON_CLASS.page -= 1
        CON_S.delete()
        CON_S.queue(sound.click)
        CON_S.play()


@CON.event
def on_draw():
    glEnable(GL_BLEND)
    GLO_clear()
    CON.clear()
    # con page 0
    if CON_CLASS.page == 0:
        CON_var["Fertil"].ConText()
        CON_var["Till"].ConText()
        if Player.workStations["Blacksmith"] < 1 and CON_var["Smith"].visible is True:
            CON_var["Smith"].ConText()
    elif CON_CLASS.page == 2:
        planting.ConText()
        for i in planting_sub.values():
            i.draw()
    py.text.Label(f"Page: {CON_CLASS.page + 1}/{CON_CLASS.MaxPage}",
                  font_name='Times New Roman',
                  font_size=10,
                  x=var.CON_WIDTH - 10, y=0,
                  anchor_x='right', anchor_y='bottom', color=(255, 255, 255)).draw()
    if CON_CLASS.page < CON_CLASS.MaxPage - 1:
        pyglet.shapes.Triangle(var.CON_WIDTH - 5, var.CON_HEIGHT / 2, var.CON_WIDTH - 20, var.CON_HEIGHT / 2 + 15,
                               var.CON_WIDTH - 20, var.CON_HEIGHT / 2 - 15, color=(245, 245, 245)).draw()
    if CON_CLASS.page > 0:
        pyglet.shapes.Triangle(5, var.CON_HEIGHT / 2, 20, var.CON_HEIGHT / 2 + 15, 20, var.CON_HEIGHT / 2 - 15,
                               color=(245, 245, 245)).draw()
    # print(CON.get_location())
    if CON_CLASS.page == 2:
        py.text.Label("")

# --------------------------------------------------------
# MAIN WINDOW HANDLERS
# --------------------------------------------------------
def M50(n):
    return math.floor(n / 50) * 50

HOLD = 0
HOLD_i = 0
WIN_S = py.media.Player()
@WIN.event
def on_mouse_press(x, y, button, modifiers):
    global HOLD,HOLD_i
    if button == py.window.mouse.LEFT:
        if CON_var["Fertil"].build is True:
            for i in range(len(GRID)):
                if GRID[i].crop is True:
                    if GRID[i].fertile is False and GRID[i].ripe is False and M50(x) == GRID[i].x and M50(y) == GRID[i].y and \
                            Player.materials["Fertilizer"] > 0:
                        if GRID[i].x + var.P_RANGE  >= Player.x >= GRID[i].x - var.P_RANGE  and \
                        GRID[i].y + var.P_RANGE  >= Player.y >= GRID[i].y - var.P_RANGE :
                            print("fertile")
                            GRID[i].fertile = True
                            Player.materials["Fertilizer"] -= 1
                            WIN_S.delete()
                            WIN_S.queue(sound.CONSTRUCTION_SOUND)
                            WIN_S.play()
                        else:
                            Player.targetX.append(GRID[i].x)
                            Player.targetY.append(GRID[i].y)
                            Player.target = True
                            HOLD = 1
                            HOLD_i = i
        elif CON_var["Smith"].build is True:
            CON_var["Smith"].visible = False
            for i in range(len(GRID)):
                if Player.workStations["Blacksmith"] < 1 and M50(x) == GRID[i].x and M50(y) == GRID[i].y:
                    if GRID[i].x + var.P_RANGE  >= Player.x >= GRID[i].x - var.P_RANGE and \
                            GRID[i].y + var.P_RANGE  >= Player.y >= GRID[i].y - var.P_RANGE:
                        GRID[i].crop = False
                        GRID[i].state = 3
                        Player.workStations["Blacksmith"] = 1
                        WIN_S.delete()
                        WIN_S.queue(sound.CONSTRUCTION_SOUND)
                        WIN_S.play()
                        print(f"Smith {i}, {GRID[i].state}")
                    else:
                        Player.targetX.append(GRID[i].x)
                        Player.targetY.append(GRID[i].y)
                        Player.target = True
                        HOLD = 2
                        HOLD_i = i
        elif CON_var["Till"].build is True:
            # CON_var["Smith"].visible = False
            for i in range(len(GRID)):
                if GRID[i].isTilled is False and M50(x) == GRID[i].x and M50(y) == GRID[i].y:
                    if GRID[i].x + var.P_RANGE >= Player.x >= GRID[i].x - var.P_RANGE and \
                            GRID[i].y + var.P_RANGE >= Player.y >= GRID[i].y - var.P_RANGE:
                        GRID[i].crop = False
                        GRID[i].state = 1
                        GRID[i].isTilled = True
                        if random.randint(1,6) == 6:
                            Player.materials["Dirt"]+=1
                        # Player.workStations["Blacksmith"] = 1
                        WIN_S.delete()
                        WIN_S.queue(sound.CONSTRUCTION_SOUND)
                        WIN_S.play()
                        print(f"Till {i}, {GRID[i].state}")
                    else:
                        Player.targetX.append(GRID[i].x)
                        Player.targetY.append(GRID[i].y)
                        Player.target = True
                        HOLD = 3
                        HOLD_i = i
        elif planting.build is True:
            for i in range(len(GRID)):
                if GRID[i].isTilled is True and M50(x) == GRID[i].x and M50(y) == GRID[i].y:
                    if GRID[i].x + var.P_RANGE >= Player.x >= GRID[i].x - var.P_RANGE and \
                            GRID[i].y + var.P_RANGE >= Player.y >= GRID[i].y - var.P_RANGE:
                        GRID[i].crop = True
                        GRID[i].state = 0
                        GRID[i].isTilled = False
                        GRID[i].cropType = 1
                        Player.materials["Krovavik Berries"]-=1
                        GRID[i].ripe = False
                        WIN_S.delete()
                        WIN_S.queue(sound.CONSTRUCTION_SOUND)
                        WIN_S.play()
                        print(f"Plant {i}, {GRID[i].state}")
                    else:
                        Player.targetX.append(GRID[i].x)
                        Player.targetY.append(GRID[i].y)
                        Player.target = True
                        HOLD = 3
                        HOLD_i = i
        else:
            Player.target = True
            if modifiers == py.window.key.MOD_SHIFT:
                Player.targetX.append(M50(x))
                Player.targetY.append(M50(y))
            else:
                Player.targetX.clear()
                Player.targetY.clear()
                Player.targetX.append(M50(x))
                Player.targetY.append(M50(y))
            #sound.click.play()
            #find different sound


@WIN.event
def on_show():
    aksndajsd = 5


@WIN.event()
def on_key_press(symbol, modifiers):
    GLO_key(symbol)

map_State = 0

@WIN.event
def on_draw():
    global HOLD,HOLD_i
    GLO_clear()
    glEnable(GL_BLEND)
    # Background
    if map_State == 0:
        for i in range(len(GRID)):
            GRID[i].draw()
            # print(f"GRID[{i}].state is {GRID[i].state}")
            if GRID[i].crop is True:
                if GRID[i].ripe is True and Player.x == GRID[i].x and Player.y == GRID[i].y:
                    GRID[i].ripe = False
                    #berry pickup
                    if GRID[i].cropType == 0:
                        if random.randint(0, 4) == 1:
                            Player.materials["Krovavik Berries (Corrupted)"] += 1
                        else:
                            Player.materials["Krovavik Berries"] += 1
                        WIN_S.delete()
                        WIN_S.queue(sound.harvest1)
                        WIN_S.play()
                    #tilled berry Pickup
                    elif GRID[i].cropType == 1:
                        Player.materials["Krovavik Berries"] += 4
                        WIN_S.delete()
                        WIN_S.queue(sound.harvest1)
                        WIN_S.play()
    elif map_State == 1:
        art.Village.blit(0,0)
    if HOLD != 0:
        if GRID[HOLD_i].x + var.P_RANGE >= Player.x >= GRID[HOLD_i].x - var.P_RANGE  and \
                            GRID[HOLD_i].y + var.P_RANGE  >= Player.y >= GRID[HOLD_i].y - var.P_RANGE :
            #ferting
            if HOLD == 1:
                GRID[HOLD_i].fertile = True
                Player.materials["Fertilizer"] -= 1
                WIN_S.delete()
                WIN_S.queue(sound.CONSTRUCTION_SOUND)
                WIN_S.play()
            #smithing
            elif HOLD == 2:
                GRID[HOLD_i].crop = False
                GRID[HOLD_i].state = 3
                Player.workStations["Blacksmith"] = 1
                CON_var["Smith"].build = False
                CON_var["Smith"].visible = False
                WIN_S.delete()
                WIN_S.queue(sound.CONSTRUCTION_SOUND)
                WIN_S.play()
            #tilling
            elif HOLD == 3:
                GRID[HOLD_i].crop = False
                GRID[HOLD_i].state = 1
                GRID[HOLD_i].isTilled = True
                if random.randint(1, 6) == 6:
                    Player.materials["Dirt"] += 1
                WIN_S.delete()
                WIN_S.queue(sound.CONSTRUCTION_SOUND)
                WIN_S.play()
            #till berries
            elif HOLD == 4:
                GRID[HOLD_i].crop = True
                GRID[HOLD_i].state = 0
                GRID[HOLD_i].cropType = 1
                GRID[HOLD_i].isTilled = False
                Player.materials["Krovavik Berries"] -= 1
                GRID[HOLD_i].ripe = False
                WIN_S.delete()
                WIN_S.queue(sound.CONSTRUCTION_SOUND)
                WIN_S.play()
            HOLD = 0
            Player.target=False
            Player.targetX.clear()
            Player.targetY.clear()
# Draw stuff here, after background you idiot, this is like the fifth time you've drawn it above the clear function
    glBlendFunc(GL_SRC_ALPHA, GL_ONE_MINUS_SRC_ALPHA)
    Player.draw()


def main_start():
    # Run the application
    grid_setup()
    py.app.run()


main_start()
