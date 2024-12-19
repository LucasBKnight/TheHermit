import math
import random
import sys

import pyglet as py
from pyglet.gl import *

import variables as var
from spriteClasses import background, player, menuWindows as inv
from sprites import artCache as art,soundCache as sound

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
    if symbol == py.window.key.ASCIITILDE:
        WIN.clear()
        #CRA.set_visible(True)
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
        #print(Player.materials)
        CON_CLASS.page = 1
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
@INV.event()
def on_key_press(symbol, modifiers):
    GLO_key(symbol)


@INV.event
def on_draw():
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
                art.KrakovikBerryINV.blit(10 + indexx, var.INV_HEIGHT - (25 * index) - 12)
            elif i == "Fertilizer":
                art.FertilizerINV.blit(10 + indexx, var.INV_HEIGHT - (25 * index) - 12)
            elif i == "Krovavik Berries (Corrupted)":
                art.KrakovikBerryCOR.blit(10 + indexx, var.INV_HEIGHT - (25 * index) - 12)
        if var.INV_HEIGHT - (25 * index) - 12 < 200:
            index = 0
            indexx = var.INV_WIDTH / 2


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
    def __init__(self,x,y):
        self.x = x
        self.y = y
        self.Col = (255, 255, 255)
        self.SubCol = (255, 255, 255)
        self.build = False


Fertil = fert(100,var.CON_HEIGHT - 40)
Smith = fert(100,var.CON_HEIGHT - 120)

@CON.event
def on_mouse_press(x, y, button, modifiers):
    #menu Page 0
    if CON_CLASS.page == 0:
        if button == pyglet.window.mouse.LEFT:
            #fertilizer
            if x > Fertil.x - 50 and x < Fertil.x + 50 and y > Fertil.y - 50 and y < Fertil.y + 50:
                if Smith.build is True:
                    Smith.build = False
                    Smith.Col = (255, 255, 255)
                if Fertil.build == False:
                    Fertil.Col = (100, 0, 0)
                    Fertil.build = True
                elif Fertil.build == True:
                    Fertil.Col = (255, 255, 255)
                    Fertil.build = False
                sound.click.play()
            #smithy
            if x > Smith.x - 50 and x < Smith.x + 50 and y > Smith.y - 50 and y < Smith.y + 50:
                if Fertil.build is True:
                    Fertil.build = False
                    Fertil.Col = (255, 255, 255)
                if Smith.build == False:
                    Smith.Col = (100, 0, 0)
                    Smith.build = True
                elif Smith.build == True:
                    Smith.Col = (255, 255, 255)
                    Smith.build = False
                sound.click.play()
    if CON_CLASS.page < CON_CLASS.MaxPage-1 and button == pyglet.window.mouse.LEFT and x<var.CON_WIDTH-5 and x>var.CON_WIDTH-25 and y<var.CON_HEIGHT/2+15 and y>var.CON_HEIGHT/2-15:
        CON_CLASS.page+=1
        sound.click.play()
    if CON_CLASS.page > 0 and button == pyglet.window.mouse.LEFT and x>5 and x<25 and y<var.CON_HEIGHT/2+15 and y>var.CON_HEIGHT/2-15:
        CON_CLASS.page-=1
        sound.click.play()
def ConText(title,Fert,textArt,PlayerDict,DictType,LvlOrAmn,introTxt):
    if PlayerDict[DictType] < LvlOrAmn:
        Fert.SubCol = (100, 0, 0)
    else:
        Fert.SubCol = (255, 255, 255)
    fertlilizeMain = py.text.Label(f"{title}",
                                   font_name='Times New Roman',
                                   font_size=20,
                                   x=Fert.x, y=Fert.y,
                                   anchor_x='center', anchor_y='bottom', color=Fert.Col)
    fertlilizeSub = py.text.Label(f"{introTxt} {LvlOrAmn}/{PlayerDict[DictType]}",
                                  font_name='Times New Roman',
                                  font_size=10,
                                  x=Fert.x - 5, y=Fert.y - 15,
                                  anchor_x='center', anchor_y='bottom', color=Fert.SubCol)
    textArt.blit(Fert.x + 25, Fert.y - 13)
    fertlilizeMain.draw()
    fertlilizeSub.draw()
@CON.event
def on_draw():
    GLO_clear()
    CON.clear()
    #con page 0
    if CON_CLASS.page == 0:
        ConText("Fertilize",Fertil,art.FertilizerINV,Player.materials,"Fertilizer",1,"Uses")
        if Player.workStations["Blacksmith"] < 1:
            ConText("Blacksmith",Smith, art.INV_Smiles, Player.tools, "Free", 0, "Free")

    py.text.Label(f"Page: {CON_CLASS.page+1}/{CON_CLASS.MaxPage}",
                                   font_name='Times New Roman',
                                   font_size=10,
                                   x=var.CON_WIDTH-10, y=0,
                                   anchor_x='right', anchor_y='bottom', color=(255,255,255)).draw()
    if CON_CLASS.page < CON_CLASS.MaxPage-1:
        pyglet.shapes.Triangle(var.CON_WIDTH-5, var.CON_HEIGHT/2, var.CON_WIDTH-20, var.CON_HEIGHT/2+15, var.CON_WIDTH-20, var.CON_HEIGHT/2-15,color=(245, 245, 245)).draw()
    if CON_CLASS.page > 0:
        pyglet.shapes.Triangle(5, var.CON_HEIGHT/2, 20, var.CON_HEIGHT/2+15, 20, var.CON_HEIGHT/2-15,color=(245, 245, 245)).draw()
    # print(CON.get_location())


# --------------------------------------------------------
# MAIN WINDOW HANDLERS
# --------------------------------------------------------
def M50(n):
    return math.floor(n / 50) * 50


@WIN.event
def on_mouse_press(x, y, button, modifiers):
    if button == py.window.mouse.LEFT:
        if Fertil.build is True:
            for i in range(len(GRID)):
                if GRID[i].crop is True:
                    if GRID[i].fertile is False and GRID[i].ripe is False and M50(x) == GRID[i].x and M50(y) == GRID[i].y \
                            and Player.materials["Fertilizer"] > 0:
                        print("fertile")
                        GRID[i].fertile = True
                        Player.materials["Fertilizer"] -= 1
        elif Smith.build is True:
            for i in range(len(GRID)):
                if Player.workStations["Blacksmith"]<1 and M50(x) == GRID[i].x and M50(y) == GRID[i].y:
                    GRID[i].crop = False
                    GRID[i].state = 3
                    Player.workStations["Blacksmith"]=1
                    sound.CONSTRUCTION_SOUND.play()
                    print(f"Smith {i}, {GRID[i].state}")
        else:
            Player.target = True
            if modifiers == py.window.key.MOD_SHIFT:
                print("Shift")
                Player.targetX.append(M50(x))
                Player.targetY.append(M50(y))
                print(Player.targetX)
            else:
                Player.targetX[0] = M50(x)
                Player.targetY[0] = M50(y)


@WIN.event
def on_show():
 aksndajsd = 5


@WIN.event()
def on_key_press(symbol, modifiers):
    GLO_key(symbol)


@WIN.event
def on_draw():
    GLO_clear()
    glEnable(GL_BLEND)
    # Background
    for i in range(len(GRID)):
        GRID[i].draw()
        #print(f"GRID[{i}].state is {GRID[i].state}")
        if GRID[i].crop is True:
            if GRID[i].ripe is True and Player.x == GRID[i].x and Player.y == GRID[i].y:
                GRID[i].ripe = False
                if GRID[i].cropType == 0:
                    if random.randint(0, 4) == 1:
                        Player.materials["Krovavik Berries (Corrupted)"] += 1
                    else:
                        Player.materials["Krovavik Berries"] += 1
        # print(f"Drew {i} Blocks")
    # Draw stuff here, after background you idiot, this is like the fifth time you've drawn it above the clear function
    glBlendFunc(GL_SRC_ALPHA, GL_ONE_MINUS_SRC_ALPHA)
    Player.draw()

def main_start():
    # Run the application
    grid_setup()
    py.app.run()
main_start()
