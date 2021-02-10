import json
import random
import globals
import pygame
import tile

def create(num):
    print("creating map " + str(num) + ".json : ")
    
    f = open("levels/" + str(num) + ".json", "w")
    lvl = randomlvl()
    f.write(json.dumps(lvl))

    print("created")

def load(num):
    print("loading map " + str(num) + " : ", end="")

    f_levels = open("levels/" + str(num) + ".json", "r")
    data = f_levels.read()
    lvl = json.loads(data)

    print("loaded")

    return lvl

def toTileMap(lvl = globals.MAP):
    map = []
    for y in range(len(lvl)):
        map.append([])
        for x in range(len(lvl[y])):
            map[y].append(tile.getTile(lvl[y][x], x, y))

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