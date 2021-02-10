import pygame
import globals
globals.WIN = pygame.display.set_mode((globals.WIDTH, globals.HEIGHT));
import colors
from pygame.locals import*
from globals import *
import level

import energy_bar
import sprites
sprites.load()
import player
from player import *

pygame.display.set_caption("Organic Future");
clock = pygame.time.Clock()
pygame.font.init()
player = Player()
globals.PLAYER = player

def main():
    run = True
    globals.LVL = level.load(2)
    globals.MAP = level.toTileMap(globals.LVL)
    level.cli(globals.LVL)
    spawnTile = level.getSpawn(globals.MAP)
    spawnX = spawnTile.x
    spawnY = spawnTile.y
    globals.changeView(spawnX, spawnY)
    player.load(spawnX, spawnY)
    while run:
        clock.tick(30)
        globals.WIN.fill(colors.GREY) # background
        level.show(globals.MAP) # tiles
        globals.PLAYER.draw() # player
        if globals.Jour: # day
            energy_bar.draw_bar(globals.PLAYER.energie)
        else:# night 
            rect = pygame.Rect(0, 0, globals.WIDTH, globals.HEIGHT)
            globals.WIN.blit(sprites.sl["blind"], rect)
        pygame.display.flip() # show

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
        
        player.move()
        
        if not player.energie >= 0:
            pass

            #todo Home Screen / Level Screen / Game Over Screen

    pygame.quit()



