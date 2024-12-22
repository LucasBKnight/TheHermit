import pyglet as py

ChemIcon = py.image.load("sprites/art/Icons/TheHermitIcon.PNG")
#replace Tilled Grass artwork, it is literal garbage
TilledGrass = py.image.load("sprites/art/tiles/Grass/TilledGrass.png")
GrassTile1 = py.image.load("sprites/art/tiles/Grass/GrassTile1.png")
CorruptGrassTile1 = py.image.load("sprites/art/tiles/Grass/Grasstile1Corrupt.png")
WallTile1 = py.image.load("sprites/art/tiles/Wall/WallTile1.png")
# change smithy texture (UPDATED: changed it but still not happy)
SmithyLVL1 = py.image.load("sprites/art/tiles/Smithy/SmithyLVL1.png")

# Placeholders
TILE_PLACEHOLDER = py.image.load("sprites/art/PLACEHOLDERS/50x50_PLACEHOLDER.png")
GUI_PLACEHOLDER = py.image.load("sprites/art/PLACEHOLDERS/125x125_GUI_PLACEHOLDER.png")
INV_Smiles = py.image.load("sprites/art/PLACEHOLDERS/INVsmiles.png")
Village = py.image.load("sprites/art/PLACEHOLDERS/VillageBackround.png")
# INV assests
KrakovikBerryINV = py.image.load("sprites/art/inventoryIcons/KrovavikBerryINV.png")
KrakovikBerryCOR = py.image.load("sprites/art/inventoryIcons/KrovavikCOR_INV.png")
FertilizerINV = py.image.load("sprites/art/inventoryIcons/FertilizerIconINV.png")
CoinINV = py.image.load("sprites/art/inventoryIcons/coin.png")
DirtINV = py.image.load("sprites/art/inventoryIcons/dirtclump.png")

def INV_sorter(text):
    if text == "Krovavik Berries":
        return KrakovikBerryINV
    else:
        return INV_Smiles
#Krovavik Bush
KrovavikTile = py.image.load("sprites/art/tiles/KrovavikBush/KrovavikBush.png")
KrovavikTill = py.image.load("sprites/art/PLACEHOLDERS/50x50_PLACEHOLDER.png")
# markers
RipeMarker = py.image.load("sprites/art/markers/RipeMarker.png")
FertileMarker = py.image.load("sprites/art/markers/FertileMarker.png")

# PlayerFaces/Bases
PlayerBase = ["sprites/art/playerbases/PlayerBase.png",
              "sprites/art/playerbases/PlayerBase+UL.png",
              "sprites/art/playerbases/PlayerBase+UR.png",
              "sprites/art/playerbases/PlayerBase+D.png",
              "sprites/art/playerbases/PlayerBase+DL.png",
              "sprites/art/playerbases/PlayerBase+DR.png",
              "sprites/art/playerbases/PlayerBase+L.png",
              "sprites/art/playerbases/PlayerBase+R.png"]
PlayerBaseA = []
for i in range(len(PlayerBase)):
    PlayerBaseA.append(py.image.load(PlayerBase[i]))

# PlayerBaseU = py.image.load("sprites/assets/playerbases/PlayerBase.png")              0 U
# PlayerBaseUL = py.image.load("sprites/assets/playerbases/PlayerBase+UL.png")          1
# PlayerBaseUR = py.image.load("sprites/assets/playerbases/PlayerBase+UR.png")          2
# PlayerBaseD = py.image.load("sprites/assets/playerbases/PlayerBase+D.png")            3 D
# PlayerBaseDL = py.image.load("sprites/assets/playerbases/PlayerBase+DL.png")          4
# PlayerBaseDR = py.image.load("sprites/assets/playerbases/PlayerBase+DR.png")          5
# PlayerBaseL = py.image.load("sprites/assets/playerbases/PlayerBase+L.png")            6 L
# PlayerBaseR = py.image.load("sprites/assets/playerbases/PlayerBase+R.png")            7 R
