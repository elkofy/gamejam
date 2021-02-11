import pygame
import globals
globals.WIN = pygame.display.set_mode((globals.WIDTH, globals.HEIGHT));
import colors
from pygame.locals import*
from globals import *
import level
import mobs
import save as s
import hud
import sprites
sprites.load()
import player
import scenario
import dialogue
from player import *
import fonts
import pygame_menu
import score 
import dialogue

pygame.init()
pygame.display.set_caption("Organic Future");
pygame.display.set_icon(sprites.sl['pl_d_s'])
clock = pygame.time.Clock()
pygame.font.init()

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


iconIT = 0

def gameIcon():
    global iconIT
    iconIT = iconIT % (7 if globals.Jour else 44)
    pygame.display.set_icon(sprites.sl[("f_kiwi_" if globals.Jour else "icon_") + str(iconIT)])
    iconIT += 1
def main():
    #pygame.mixer.music.load('assets/sounds/theme_1.wav')
    #pygame.mixer.music.play(-1)
    player = Player()
    globals.PLAYER = player
    globals.NAME = globals.NAME.get_value()
    globals.SCORE = score.Score(globals.NAME)
    save = s.Save()
    globals.NB_MORTS = globals.SCORE.get()
    print("NB_morts", globals.NB_MORTS)
    globals.NUM_LVL = save.get_lvl(globals.NAME)
    lvl = globals.NUM_LVL
    run = True
    load_lvl(lvl)
    fonts.font_init()
    while run:
        globals.LT = clock.tick(60)
        gameIcon()

        if globals.LVL_CHANGED:
            load_lvl(globals.NUM_LVL)
        
        globals.WIN.fill(colors.GREY) # background
       
        scenario.lvl1()
       
        level.show(globals.MAP) # tiles
        for m in mobs.mobs:
            m.drawMob()
        globals.PLAYER.draw() # player
        if globals.Jour: # day
            hud.draw_bar(globals.PLAYER.energie)
        else:# night
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
    globals.PLAYER.load(spawnX, spawnY)
    globals.LVL_CHANGED = False
    if globals.LOGS:
        level.cli(globals.LVL)