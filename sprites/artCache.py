import pyglet as py

ChemIcon = py.image.load("venv/art/Icons/TheHermitIcon.PNG")
GrassTile1 = py.image.load("venv/art/tiles/Grass/GrassTile1.png")
CorruptGrassTile1 = py.image.load("venv/art/tiles/Grass/Grasstile1Corrupt.png")
WallTile1 = py.image.load("venv/art/tiles/Wall/WallTile1.png")
# change smithy texture (UPDATED: changed it but still not happy)
SmithyLVL1 = py.image.load("venv/art/tiles/Smithy/SmithyLVL1.png")

# Placeholders
TILE_PLACEHOLDER = py.image.load("venv/art/PLACEHOLDERS/50x50_PLACEHOLDER.png")
GUI_PLACEHOLDER = py.image.load("venv/art/PLACEHOLDERS/125x125_GUI_PLACEHOLDER.png")

# INV assests
KrakovikBerryINV = py.image.load("venv/art/inventoryIcons/KrovavikBerryINV.png")
KrakovikBerryCOR = py.image.load("venv/art/inventoryIcons/KrovavikCOR_INV.png")
FertilizerINV = py.image.load("venv/art/inventoryIcons/FertilizerIconINV.png")

# markers
# replace this with a darker green kinda shit rn ngl
RipeMarker = py.image.load("venv/art/markers/RipeMarker.png")
FertileMarker = py.image.load("venv/art/markers/FertileMarker.png")

# PlayerFaces/Bases
PlayerBase = ["venv/art/playerbases/PlayerBase.png",
              "venv/art/playerbases/PlayerBase+UL.png",
              "venv/art/playerbases/PlayerBase+UR.png",
              "venv/art/playerbases/PlayerBase+D.png",
              "venv/art/playerbases/PlayerBase+DL.png",
              "venv/art/playerbases/PlayerBase+DR.png",
              "venv/art/playerbases/PlayerBase+L.png",
              "venv/art/playerbases/PlayerBase+R.png"]
PlayerBaseA = []
for i in range(len(PlayerBase)):
    PlayerBaseA.append(py.image.load(PlayerBase[i]))

# PlayerBaseU = py.image.load("venv/assets/playerbases/PlayerBase.png")              0 U
# PlayerBaseUL = py.image.load("venv/assets/playerbases/PlayerBase+UL.png")          1
# PlayerBaseUR = py.image.load("venv/assets/playerbases/PlayerBase+UR.png")          2
# PlayerBaseD = py.image.load("venv/assets/playerbases/PlayerBase+D.png")            3 D
# PlayerBaseDL = py.image.load("venv/assets/playerbases/PlayerBase+DL.png")          4
# PlayerBaseDR = py.image.load("venv/assets/playerbases/PlayerBase+DR.png")          5
# PlayerBaseL = py.image.load("venv/assets/playerbases/PlayerBase+L.png")            6 L
# PlayerBaseR = py.image.load("venv/assets/playerbases/PlayerBase+R.png")            7 R
