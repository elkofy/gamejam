import levelLoader
import pygame
import objects
import globals

def show(num):
    level = levelLoader.loadLevel(num)

    for y in range(len(level)):
        print("\n " + str(y), end='')
        for x in range(len(level[y])):
            obj = objects.objArr[level[y][x]]
            rect = pygame.Rect(globals.calcX(x), globals.calcY(y), globals.OBJECT_WIDTH, globals.OBJECT_HEIGHT)
            if (level[y][x]):
                pygame.draw.rect(globals.WIN, obj.color, rect)
                print("@", end='')
            else :
                print(" ", end='')