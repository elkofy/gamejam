import levelLoader
import pygame
import objects
import globals

def show(num):
    level = levelLoader.loadLevel(num)
    
    objH = 728 / len(level)

    for y in range(len(level)):
        print("\n " + str(y), end='')
        for x in range(len(level[y])):
            objW = 1024 / len(level[y])
            obj = objects.objArr[level[y][x]]
            rect = pygame.Rect(objW * x, objH * y, objW, objH)
            if (level[y][x]):
                pygame.draw.rect(globals.WIN, obj.color, rect)
                print("@", end='')
            else :
                print(" ", end='')