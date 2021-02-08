import main
import levelLoader
import pygame
import colors

def show(num):
    level = levelLoader.loadLevel(num)
    
    objH = 728 / len(level)

    for y in range(len(level)):
        print("\n " + str(y), end='')
        for x in range(len(level[y])):
            objW = 1024 / len(level[y])
            rect = pygame.Rect(objW * x, objH * y, objW, objH)
            if (level[y][x]):
                pygame.draw.rect(main.WIN, colors.CYAN, rect)
                print("@", end='')
            else :
                print(" ", end='')