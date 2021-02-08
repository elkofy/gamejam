import json
import random
import globals
import pygame
import objects

def create(num):
    print("Creation du fichier " + str(num) + ".json")
    
    f = open("levels/" + str(num) + ".json", "w")
    lvl = randomlvl()
    f.write(json.dumps(lvl))

def load(num):
    print("Chargement du monde " + str(num))

    f_levels = open("levels/" + str(num) + ".json", "r")
    data = f_levels.read()
    lvl = json.loads(data)

    return lvl

def randomlvl():
    lvl = []
    for i in range(globals.GAME_HEIGHT):
        lvl.append([])
        for j in range(globals.GAME_WIDTH):
            lvl[i].append(1 if random.randint(1, 100) > 75 else 0)
    return lvl

def show(lvl):
    for y in range(len(lvl)):
        for x in range(len(lvl[y])):
            if (lvl[y][x]):
                obj = objects.mur
                rect = pygame.Rect(globals.calcX(x), globals.calcY(y), globals.OBJECT_WIDTH, globals.OBJECT_HEIGHT)
                pygame.draw.rect(globals.WIN, obj.color, rect)

def cli(lvl):
    for line in lvl:
        print("\n", end="")
        for case in line:
            if (case):
                print(case, end="")
            else:
                print(" ", end="")