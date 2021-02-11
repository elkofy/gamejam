import pygame
import globals
globals.WIN = pygame.display.set_mode((globals.WIDTH, globals.HEIGHT));
import colors
from pygame.locals import*
from globals import *
import level
import mobs
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
    lvl = globals.NUM_LVL
    run = True
    load_lvl(lvl)
    while run:
        globals.LT = clock.tick(60)
        if globals.LVL_CHANGED:
            load_lvl(globals.NUM_LVL)
        globals.WIN.fill(colors.GREY) # background
        level.show(globals.MAP) # tiles
        for m in mobs.mobs:
            m.drawMob()
        globals.PLAYER.draw() # player
        if globals.Jour: # day
            energy_bar.draw_bar(globals.PLAYER.energie)
        else:# night
            pygame.draw.polygon(globals.WIN, colors.BLACK, blindPoints)
        pygame.display.flip() # show

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
        if not player.moving:
            player.move()
        else:
            player.moveAnim()
        player.checkState()
        for m in mobs.mobs:
            m.act()

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