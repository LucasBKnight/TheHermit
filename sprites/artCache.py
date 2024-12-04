import pyglet as py
import main

ChemIcon = py.image.load("venv/assets/Icons/TheHermitIcon.PNG")
GrassTile1 = py.image.load("venv/assets/tiles/Grass1/GrassTile1.png")
CorruptGrassTile1 = py.image.load("venv/assets/tiles/Grass1/Grasstile1Corrupt.png")
WallTile1 = py.image.load("venv/assets/tiles/Wall1/WallTile1.png")
#change smithy texture (UPDATED: changed it but still not happy)
SmithyLVL1 = py.image.load("venv/assets/Constructables/SmithyLVL1.png")

#Placeholders
TILE_PLACEHOLDER = py.image.load("venv/assets/PLACEHOLDERS/50x50_PLACEHOLDER.png")
GUI_PLACEHOLDER = py.image.load("venv/assets/PLACEHOLDERS/125x125_GUI_PLACEHOLDER.png")

#PlayerFaces/Bases
PlayerBase = ["venv/assets/playerbases/PlayerBase.png",
              "venv/assets/playerbases/PlayerBase+UL.png",
              "venv/assets/playerbases/PlayerBase+UR.png",
              "venv/assets/playerbases/PlayerBase+D.png",
              "venv/assets/playerbases/PlayerBase+DL.png",
              "venv/assets/playerbases/PlayerBase+DR.png",
              "venv/assets/playerbases/PlayerBase+L.png",
              "venv/assets/playerbases/PlayerBase+R.png"]
PlayerBaseA = []
for i in range(len(PlayerBase)):
    PlayerBaseA.append(py.image.load(PlayerBase[i]))

#PlayerBaseU = py.image.load("venv/assets/playerbases/PlayerBase.png")              0 U
#PlayerBaseUL = py.image.load("venv/assets/playerbases/PlayerBase+UL.png")          1
#PlayerBaseUR = py.image.load("venv/assets/playerbases/PlayerBase+UR.png")          2
#PlayerBaseD = py.image.load("venv/assets/playerbases/PlayerBase+D.png")            3 D
#PlayerBaseDL = py.image.load("venv/assets/playerbases/PlayerBase+DL.png")          4
#PlayerBaseDR = py.image.load("venv/assets/playerbases/PlayerBase+DR.png")          5
#PlayerBaseL = py.image.load("venv/assets/playerbases/PlayerBase+L.png")            6 L
#PlayerBaseR = py.image.load("venv/assets/playerbases/PlayerBase+R.png")            7 R