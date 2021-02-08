import json
import random
import globals
import pygame
import objects

def create(num):
    print("Creation du fichier " + str(num) + ".json")
    
    f = open("levels/" + str(num) + ".json", "w")
    lvl = random()
    f.write(json.dumps(lvl))

def load(num):
    print("Chargement du monde " + str(num))

    f_levels = open("levels/" + str(num) + ".json", "r")
    data = f_levels.read()
    lvl = json.loads(data)

    return lvl

def random():
    lvl = []
    for i in range(globals.GAME_HEIGHT):
        arr.append([])
        for j in range(globals.GAME_WIDTH):
            arr[i].append(random.randint(0, len(objects.objArr + 1)))
    return lvl

def show(lvl):
    for y in range(len(lvl)):
        for x in range(len(lvl[y])):
            if (lvl[y][x]):
                obj = objects.objArr[lvl[y][x] - 1]
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