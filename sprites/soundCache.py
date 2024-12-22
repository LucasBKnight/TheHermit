import pyglet as py
placeholder = py.media.load("sprites/sound/PLACEHOLDER_SOUND.mp3")
CONSTRUCTION_SOUND = py.media.load("sprites/sound/build.mp3")
click = py.media.load("sprites/sound/halfclicktrim.mp3")
harvest1 = py.media.load("sprites/sound/harvest1.mp3")
harvest1.volume = 1.0
step1 = py.media.load("sprites/sound/step1.mp3")
step1.volume = 1.0
step2 = py.media.load("sprites/sound/step2.mp3")
step2.volume = 1.0
step3 = py.media.load("sprites/sound/step2.mp3")
step3.volume = 1.0

class MediaPlayer:
    def __init__(self):
        self.cycler = []
    def addSound(self,sound):
        check = True
        for i in self.cycler:
            if sound == i:
                check = False
                if i.playing:
                    check = True
                    i.pop()
        if check is True:
            self.cycler.append(sound)
        else:
            print("Sound Already Queued")
    def play(self):
        for i in self.cycler:
            i.play()
mediaPlayer = MediaPlayer()