import pygame
import colors
import globals
import fonts
from fonts import *
#pixel_font = pygame.font.Font("assets/pixel_font.ttf", 26)


def draw_bar(energie):
    if globals.Jour:
        if energie > 0:
            length = 100*(energie/globals.MAX_ENERGY)
            rec = pygame.Rect(915 - length, 25, length , 20)
            pygame.draw.rect(globals.WIN, colors.BLUE, rec, 0)
            rec = pygame.Rect(915 - length, 25, length , 20)
            pygame.draw.rect(globals.WIN, colors.WHITE, rec, 3)
            img = fonts.pixel_font_24.render(str(energie), True, colors.BLUE)
            globals.WIN.blit(img, (930, 24))
    else:
        length = 100
        rec = pygame.Rect(915 - length, 25, length , 20)
        pygame.draw.rect(globals.WIN, colors.RED, rec, 0)
        rec = pygame.Rect(915 - length, 25, length , 20)
        pygame.draw.rect(globals.WIN, colors.WHITE, rec, 3)
        img = fonts.pixel_font_24.render("99999", True, colors.WHITE)
        globals.WIN.blit(img, (930, 24))

def draw_lvl():
    if globals.Jour:
        img = fonts.pixel_font_30.render(str(globals.NUM_LVL), True, colors.BLUE)
        
    else:
        img = fonts.pixel_font_30.render("Level: " + str(globals.NUM_LVL), True, colors.WHITE)
    
    globals.WIN.blit(img, (24, 24))

def draw_deaths():
    if globals.Jour:
        img = fonts.pixel_font_24.render("Deaths: " + str(globals.NB_MORTS), True, colors.BLUE)
        
    else:
        img = fonts.pixel_font_24.render("Deaths: " + str(globals.NB_MORTS), True, colors.WHITE)
    
    globals.WIN.blit(img, (24, 50))
