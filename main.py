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
import draw

pygame.display.set_caption("Organic Future");
clock = pygame.time.Clock()
pygame.font.init()
player = Player()
globals.PLAYER = player
#m_tomato = mobs.Mob();


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
    #m_tomato.load(20, 14)
    while run:
        #clock.tick(60)
        draw.drawAll()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
        player.move()
        #m_tomato.move()
        #m_tomato.draw()
        if not player.energie >= 0:
            pass
            #todo Home Screen / Level Screen / Game Over Screen
    pygame.quit()



