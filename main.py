import pygame
import globals
globals.WIN = pygame.display.set_mode((globals.WIDTH, globals.HEIGHT));
import colors
from pygame.locals import*
from globals import *
import objects
objects.loadSprites()
import player
from player import *
import level
import energy_bar
pygame.display.set_caption("Game Jam 2021");
clock = pygame.time.Clock()
player = Player()
    
pygame.font.init()


def main():
    run = True
    globals.changeView(16, 18)
    globals.LVL = level.load(2)
    # level.cli(globals.lvl)
    player.load(16, 18)
    while run:
        #clock.tick(60)
        objects.drawBG()
        level.show(globals.LVL)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
        player.move()
        player.draw()
        if blind:
            rect = pygame.Rect(0, 0, globals.WIDTH, globals.HEIGHT)
            globals.WIN.blit(objects.sprites["blind"], rect)
        energy_bar.draw_bar(player.energie)
        pygame.display.flip()
    pygame.quit()


if __name__ == "__main__":
    main()
