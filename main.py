import math
import random
import sys

import pyglet as py
from pyglet.gl import *

import variables as var
from spriteClasses import background, player, menuWindows as inv
from sprites import artCache as art

# main window
WIN = py.window.Window(width=var.WIN_WIDTH, height=var.WIN_HEIGHT, caption="The Hermit")
WIN.set_icon(art.ChemIcon)
# inventory Window
INV_CLASS = inv.menu()
INV = py.window.Window(width=var.INV_WIDTH, height=var.INV_HEIGHT, caption="Inventory")

# build window
CON_CLASS = inv.menu()
CON = py.window.Window(width=var.CON_WIDTH, height=var.CON_HEIGHT, caption="Build Menu")
CON.set_location(var.WIN_WIDTH * (5 / 8) + 50, var.WIN_HEIGHT)

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
    if symbol == py.window.key.I:
        INV_CLASS.show()
    INV.set_visible(INV_CLASS.is_shown())
    if symbol == py.window.key.C:
        CON_CLASS.show()
    CON.set_visible(CON_CLASS.is_shown())
    if symbol == py.window.key.EQUAL:
        #Player.materials["Krovavik Berries"] += 1
        print(Player.materials)
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
    def __init__(self):
        self.x = 60
        self.y = var.CON_HEIGHT - 40
        self.Col = (255, 255, 255)
        self.build = False


Fert = fert()


@CON.event
def on_mouse_press(x, y, button, modifiers):
    if button == pyglet.window.mouse.LEFT:
        if x > Fert.x - 50 and x < Fert.x + 50 and y > Fert.y - 50 and y < Fert.y + 50:
            if Fert.build == False:
                Fert.Col = (100, 0, 0)
                Fert.build = True
            elif Fert.build == True:
                Fert.Col = (255, 255, 255)
                Fert.build = False


@CON.event
def on_draw():
    GLO_clear()
    CON.clear()
    if Player.materials["Fertilizer"] < 1:
        color = (100, 0, 0)
    else:
        color = (255, 255, 255)
    fertlilizeMain = py.text.Label(f"Fertilize",
                                   font_name='Times New Roman',
                                   font_size=20,
                                   x=Fert.x, y=Fert.y,
                                   anchor_x='center', anchor_y='bottom', color=Fert.Col)
    fertlilizeSub = py.text.Label(f"Uses 1/{Player.materials['Fertilizer']}",
                                  font_name='Times New Roman',
                                  font_size=10,
                                  x=Fert.x - 5, y=Fert.y - 15,
                                  anchor_x='center', anchor_y='bottom', color=color)
    art.FertilizerINV.blit(Fert.x + 25, Fert.y - 13)
    fertlilizeMain.draw()
    fertlilizeSub.draw()
    # print(CON.get_location())


# --------------------------------------------------------
# MAIN WINDOW HANDLERS
# --------------------------------------------------------
def M50(n):
    return math.floor(n / 50) * 50


@WIN.event
def on_mouse_press(x, y, button, modifiers):
    if button == pyglet.window.mouse.LEFT and Fert.build == True:
        for i in range(len(GRID)):
            print(i)
            if GRID[i].crop == True:
                print("tis crop")
                if GRID[i].fertile == False and M50(x) == GRID[i].x and M50(y) == GRID[i].y and Player.materials[
                    "Fertilizer"] > 0:
                    print("fertile")
                    GRID[i].fertile = True
                    Player.materials["Fertilizer"] -= 1
    elif button == pyglet.window.mouse.LEFT and Fert.build == False:
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
    grid_setup()


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
        if GRID[i].crop == True:
            if GRID[i].ripe == True and Player.x == GRID[i].x and Player.y == GRID[i].y:
                GRID[i].ripe = False
                if GRID[i].cropType == 0:
                    if random.randint(0,4) == 1:
                        Player.materials["Krovavik Berries (Corrupted)"] += 1
                    else:
                        Player.materials["Krovavik Berries"] += 1
        # print(f"Drew {i} Blocks")
    # Draw stuff here, after background you idiot, this is like the fifth time you've drew it above the clear function
    glBlendFunc(GL_SRC_ALPHA, GL_ONE_MINUS_SRC_ALPHA)
    Player.draw()


# Run the application
py.app.run()
