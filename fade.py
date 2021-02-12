import pygame
import globals
import colors

def fade():
    if globals.LOGS:
        print("fade")
    s = pygame.Surface((globals.WIDTH,globals.HEIGHT)) 
    for i in range(0, 180): # the size of your rect
        if globals.LOGS:
            print("fade", i)
        s.set_alpha(round(i/2))                # alpha level
        s.fill(colors.BLACK)           # this fills the entire surface
        globals.WIN.blit(s, (0,0))
        pygame.display.update() # show