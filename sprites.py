import pygame
import globals

c = 0

sl = {}

dirr = {
    "up" : "u",
    "left" : "l",
    "right" : "r",
    "down" : "d"
}

toLoad = {
    "bg_tile" : "decors/sol.png",
    "spawn" : "start.png",
    "bed" : "bed.png",
    "light_day" : "decors/light_day.png",
    "light_night" : "decors/light_night.png",
    "grating" : "decors/grating.png",
    "trap_on": "trap/on.png",
    "trap_off": "trap/off.png"
}

def loadSprite(name, f, w = globals.OBJECT_WIDTH, h = globals.OBJECT_HEIGHT):
    global c
    c += 1
    global sprites
    
    if globals.LOGS:
        print("loading assets/" + f + " to " + name + " : ", end="")
    img = pygame.image.load("assets/" + f)
    img = pygame.transform.scale(img, (w, h))
    img.convert()
    sl[name] = img
    
    if globals.LOGS:
        print("loaded")

def loadIcon():
    for i in range(44):
        loadSprite("icon_" + str(i), "icon/" + str(i) + ".png")

def loadWall():
    global wallSprites
    for i in range(29):
        loadSprite("wall_" + str(i), "wall/" + str(i) + ".png")

def loadPlayer():

    for d in dirr:
        loadSprite("pl_" + dirr[d] + "_s", "player/" + d + "/static.png", globals.PLAYER_WIDTH, globals.PLAYER_HEIGHT)

        for i in range(16):
            loadSprite("pl_" + dirr[d] + "_m_" + str(i), "player/" + d + "/move_" + str(i+1) + ".png", globals.PLAYER_WIDTH, globals.PLAYER_HEIGHT)

def loadFruits():
    fruits = {
        "kiwi" : 7,
        "tomato" : 6,
        "lemon" : 1
    }

    for f in fruits:
        for i in range(fruits[f]):
            loadSprite("f_" + f + "_" + str(i), "fruits/" + f + "/" + str(i) + ".png")

def loadMonsters():
    mobs = {
        "kiwi" : {
            "up" : 44,
            "left" : 41,
            "right" : 41,
            "down" : 44,
        },
        "tomato" : {
            "up" : 54,
            "left" : 54,
            "right" : 54,
            "down" : 54,
        },
        "lemon" : {
            "up" : 8,
            "left" : 8,
            "right" : 8,
            "down" : 8,
        }
    }

    for m in mobs:
        for d in dirr:
            for i in range(mobs[m][d]):
                loadSprite("m_" + m + "_" + dirr[d] + "_" + str(i), "mobs/" + m + "/" + d + "/" + str(i) + ".png")

def load():
    loadIcon()
    loadWall()
    loadPlayer()
    loadFruits()
    loadMonsters()

    loadSprite("end_screen", "wscreen.png", globals.WIDTH, globals.HEIGHT)

    for spr in toLoad:
        loadSprite(spr, toLoad[spr])
    print(c, "sprites loaded")