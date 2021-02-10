import pygame
import globals

sl = {}

toLoad = {
    "spawn" : "start.png",
    "bg_tile" : "decors/sol.png",
    "bed" : "bed_temp.png",
    "f_tomato" : "fruits/tomato.gif",
    "m_tomato" : "mobs/tomato.gif",
    "f_kiwi" : "fruits/kiwi.gif",
    "m_kiwi" : "mobs/kiwi.gif"
}

def loadSprite(name, f, w = globals.OBJECT_WIDTH, h = globals.OBJECT_HEIGHT):
    global sprites
    print("loading " + f + " : ", end="")
    img = pygame.image.load("assets/" + f)
    img = pygame.transform.scale(img, (w, h))
    img.convert()
    sl[name] = img
    print("loaded")

def loadWallSprites():
    global wallSprites
    for i in range(29):
        loadSprite("wall_" + str(i), "wall/" + str(i) + ".png")

def loadPlayerSprites():
    dirr = {
        "up" : "u",
        "left" : "l",
        "right" : "r",
        "down" : "d"
    }

    for d in dirr:
        loadSprite("pl_" + dirr[d] + "_s", "player/" + d + "/static.png", globals.PLAYER_WIDTH, globals.PLAYER_HEIGHT)

        for i in range(16):
            loadSprite("pl_" + dirr[d] + "_m_" + str(i), "player/" + d + "/move_" + str(i+1) + ".png", globals.PLAYER_WIDTH, globals.PLAYER_HEIGHT)

def load():
    loadSprite("blind", "blind.png", globals.WIDTH, globals.HEIGHT)

    loadWallSprites()
    loadPlayerSprites()

    for spr in toLoad:
        loadSprite(spr, toLoad[spr])