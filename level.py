import json
import random
import globals
import pygame
import tile
import mobs

chars = tile.chars

def create(num):
    if globals.LOGS:
        print("creating map " + str(num) + ".json : ")
    
    f = open("levels/" + str(num) + ".json", "w")
    lvl = randomlvl()
    f.write(json.dumps(lvl))

    
    if globals.LOGS:
        print("created")

def load(num):
    if globals.LOGS:
        print("loading map " + str(num) + " : ", end="")

    f_levels = open("levels/" + str(num) + ".json", "r")
    data = f_levels.read()
    lvl = json.loads(data)

    if globals.LOGS:
        print("loaded")

    maxW = 0
    for line in lvl:
        if len(line) > maxW:
            maxW = len(line)

    globals.GAME_HEIGHT = len(lvl)
    globals.GAME_WIDTH = maxW
    
    return lvl

def toTileMap(lvl = globals.MAP):
    map = []
    for y in range(len(lvl)):
        map.append([])
        for x in range(len(lvl[y])):
            map[y].append(getTile(lvl[y][x], x, y))

    return map

def getSpawn(map = globals.MAP):
    for line in map:
        for t in line:
            if type(t) is tile.Spawn:
                return t


def randomlvl():
    lvl = []
    for i in range(globals.GAME_HEIGHT):
        lvl.append([])
        for j in range(globals.GAME_WIDTH):
            lvl[i].append(1 if random.randint(1, 100) > 75 else 0)
    return lvl

def show(map = globals.MAP):
    for y in range(len(map)):
        if (globals.calcY(y) - globals.marginTop + globals.OBJECT_HEIGHT > 0 and globals.calcY(y) - globals.marginTop < globals.HEIGHT):
            for x in range(len(map[y])):
                if (globals.calcX(x) - globals.marginLeft + globals.OBJECT_WIDTH > 0 and globals.calcX(x) - globals.marginLeft < globals.WIDTH):
                    map[y][x].updatePos()
                    map[y][x].draw()

def cli(lvl = globals.LVL):
    for line in lvl:
        for case in line:
            print(case + " ", end="")
        print("\n", end="")

def getTile(c, x, y):
    if (chars[c] == "empty"):
        return tile.Empty(x, y)
    elif (chars[c] == "spawn"):
        return tile.Spawn(x, y)
    elif (chars[c] == "bed"):
        return tile.Bed(x, y)
    elif (chars[c] == "wall"):
        return tile.Wall(x, y)
    elif (chars[c] == "tomato"):
        if globals.Jour :
            return tile.Fruits(x, y, "tomato", 6)
        else:
            return mobs.Mob(x, y, "tomato", "d", 54)
    elif (chars[c] == "kiwi"):
        if globals.Jour :
            return tile.Fruits(x, y, "kiwi", 7)
        else:
            return mobs.Mob(x, y, "kiwi", "d", 44)
    