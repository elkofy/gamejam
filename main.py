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
import save as s
import pygame_menu

pygame.init()
pygame.display.set_caption("Organic Future");
clock = pygame.time.Clock()
pygame.font.init()
player = Player()
globals.PLAYER = player
globals.SCORE = score.Score(globals.NAME)


halfWidth = globals.WIDTH / 2
haldHeight = globals.HEIGHT / 2
blindPoints = [
    (0, 0),
    (halfWidth, 0),
    (halfWidth, haldHeight - BLIND_RADIUS),
    (halfWidth - BLIND_RADIUS/4*3, haldHeight - BLIND_RADIUS/4*3),
    (halfWidth - BLIND_RADIUS, haldHeight),
    (halfWidth - BLIND_RADIUS/4*3, haldHeight + BLIND_RADIUS/4*3),
    (halfWidth, haldHeight + BLIND_RADIUS),
    (halfWidth + BLIND_RADIUS/4*3, haldHeight + BLIND_RADIUS/4*3),
    (halfWidth + BLIND_RADIUS, haldHeight),
    (halfWidth + BLIND_RADIUS/4*3, haldHeight - BLIND_RADIUS/4*3),
    (halfWidth, haldHeight - BLIND_RADIUS),
    (halfWidth, 0),
    (globals.WIDTH, 0),
    (globals.WIDTH, globals.HEIGHT),
    (0, globals.HEIGHT),
]

def main():
    globals.NAME = globals.NAME.get_value()
    save = s.Save()
    globals.NB_MORTS = globals.SCORE.get()
    globals.NUM_LVL = save.get_lvl(globals.NAME)
    lvl = globals.NUM_LVL
    run = True
    load_lvl(lvl)
    fonts.font_init()
    blindFilter = pygame.Rect(0, 0, globals.WIDTH, globals.HEIGHT)
    while run:
        globals.LT = clock.tick(60)
        if globals.LVL_CHANGED:
            load_lvl(globals.NUM_LVL)
        globals.WIN.fill(colors.GREY) # background
        level.show(globals.MAP) # tiles
        globals.PLAYER.draw() # player
        if not globals.Jour: # day
            #globals.WIN.blit(sprites.sl["blind"], blindFilter)
            pygame.draw.polygon(globals.WIN, colors.BLACK, blindPoints)
        hud.draw_bar(globals.PLAYER.energie)
        hud.draw_lvl()
        hud.draw_deaths()
        pygame.display.flip() # show

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                globals.SCORE.add(globals.NB_MORTS)
                save.add(globals.NAME, globals.NUM_LVL)
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
    if globals.LOGS:
        level.cli(globals.LVL)