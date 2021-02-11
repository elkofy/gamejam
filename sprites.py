import pygame
import globals

sl = {}

toLoad = {
    "bg_tile" : "decors/sol.png",
    "spawn" : "start.png",
    "bed" : "bed.png",
    "m_tomato" : "mobs/tomato.gif",
    "m_kiwi" : "mobs/kiwi.gif",
    "light_day" : "decors/light_day.png",
    "light_night" : "decors/light_night.png",
    "vine" : "decors/vine.png",
}

def loadSprite(name, f, w = globals.OBJECT_WIDTH, h = globals.OBJECT_HEIGHT):
    global sprites
    
    if globals.LOGS:
        print("loading assets/" + f + " : ", end="")
    img = pygame.image.load("assets/" + f)
    img = pygame.transform.scale(img, (w, h))
    img.convert()
    sl[name] = img
    
    if globals.LOGS:
        print("loaded")

def loadWall():
    global wallSprites
    for i in range(29):
        loadSprite("wall_" + str(i), "wall/" + str(i) + ".png")

def loadPlayer():
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

def loadFruits():
    fruits = {
        "kiwi" : 7,
        "tomato" : 6
    }

    for f in fruits:
        for i in range(fruits[f]):
            loadSprite("f_" + f + "_" + str(i), "fruits/" + f + "/" + str(i) + ".png")

def load():
    loadSprite("blind", "blind.png", globals.WIDTH, globals.HEIGHT)

    loadWall()
    loadPlayer()
    loadFruits()

    for spr in toLoad:
        loadSprite(spr, toLoad[spr])