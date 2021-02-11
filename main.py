import pygame
import globals
globals.WIN = pygame.display.set_mode((globals.WIDTH, globals.HEIGHT));
import colors
from pygame.locals import*
from globals import *
import level
import mobs
import hud
import sprites
sprites.load()
import player
from player import *
import fonts
import score

pygame.init()
pygame.display.set_caption("Organic Future");
clock = pygame.time.Clock()
pygame.font.init()
player = Player()
globals.PLAYER = player
globals.SCORE = score.Score(globals.NAME)

def main():
    globals.NB_MORTS = globals.SCORE.get()
    lvl = globals.NUM_LVL
    run = True
    load_lvl(lvl)
    fonts.font_init()
    while run:
        clock.tick(60)
        if globals.LVL_CHANGED:
            load_lvl(globals.NUM_LVL)
        globals.WIN.fill(colors.GREY) # background
        level.show(globals.MAP) # tiles
        globals.PLAYER.draw() # player
        if not globals.Jour: # day
            rect = pygame.Rect(0, 0, globals.WIDTH, globals.HEIGHT)
            globals.WIN.blit(sprites.sl["blind"], rect)
        hud.draw_bar(globals.PLAYER.energie)
        hud.draw_lvl()
        hud.draw_deaths()
        pygame.display.flip() # show

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                globals.SCORE.add(globals.NB_MORTS)
        
        player.move()
        for i in mobs.mobs:
            i.move()

    pygame.quit()


def load_lvl(num_lvl):
    mobs.mobs = []
    globals.LVL = level.load(num_lvl)
    globals.MAP = level.toTileMap(globals.LVL)
    spawnTile = level.getSpawn(globals.MAP)
    spawnX = spawnTile.x
    spawnY = spawnTile.y
    globals.changeView(spawnX, spawnY)
    player.load(spawnX, spawnY)
    globals.LVL_CHANGED = False

