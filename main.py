import pyglet as py
from spriteClasses import grid
# Create a window
WIN_WIDTH, WIN_HEIGHT = 1400, 800
WIN = py.window.Window(width=WIN_WIDTH, height=WIN_HEIGHT, caption="My Pyglet Window")

# Event handler for drawing
@WIN.event
def on_draw():
    WIN.clear()  # Clear the window with default black color

# Run the application
py.app.run()