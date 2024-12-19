import pyglet as py
class menu:
    def __init__(self):
        self.shown = True

    def show(self):
        self.shown = not self.shown
        # print(f"Shown is {self.shown}")

    def is_shown(self):
        return self.shown

class conmenu:
    def __init__(self):
        self.shown = True
        self.page = 0
        self.MaxPage = 3

    def show(self):
        self.shown = not self.shown
        # print(f"Shown is {self.shown}")

    def is_shown(self):
        return self.shown