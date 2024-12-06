class menu:
    def __init__(self):
        self.shown = True

    def show(self):
        self.shown = not self.shown
        # print(f"Shown is {self.shown}")

    def is_shown(self):
        return self.shown
