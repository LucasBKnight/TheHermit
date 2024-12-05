import pyglet as py
import variables as var
from spriteClasses import background,player
# Create a window
WIN = py.window.Window(width=var.WIN_WIDTH, height=var.WIN_HEIGHT, caption="My Pyglet Window")
GRID = []
Player = player.Player()
def grid_setup():
    for i in range(int(var.WIN_HEIGHT/var.GRID_SIZE)):
        for ii in range(int(var.WIN_WIDTH/var.GRID_SIZE)):
            GRID.append(background.GridClass(ii*var.GRID_SIZE,i*var.GRID_SIZE))
            print(f"Created Tile @({ii*var.GRID_SIZE},{i*var.GRID_SIZE})")
    print(GRID)

@WIN.event
def on_key_press(symbol, modifiers):
    Player.key(symbol,WIN)

@WIN.event
def on_show():
        grid_setup()


@WIN.event
def on_draw():
    WIN.clear()
    #Background
    for i in range(len(GRID)):
        GRID[i].draw()
        #print(f"Drew {i} Blocks")
    #Draw stuff here, after background you idiot, this is like the fifth time you've drew it above the clear function
    Player.draw()
# Run the application
py.app.run()