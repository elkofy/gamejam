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
import mobs

pygame.display.set_caption("Organic future");
clock = pygame.time.Clock()
player = Player()
pygame.font.init()

m_tomato = mobs.Mob();

def main():
    run = True
    globals.changeView(16, 18)
    globals.LVL = level.load(2)
    # level.cli(globals.lvl)
    player.load(16, 18)
    m_tomato.load(20, 14)
    while run:
        #clock.tick(60)
        objects.drawBG()
        level.show(globals.LVL)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
        player.move()
        player.draw()
        m_tomato.move()
        m_tomato.draw()
        energy_bar.draw_bar(player.energie)
        pygame.display.flip()
        if not player.energie >= 0:
            pass
            #todo Home Screen / Level Screen / Game Over Screen
    pygame.quit()


if __name__ == "__main__":
    main()
