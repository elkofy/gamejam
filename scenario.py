import pygame
import globals
import fonts
import dialogue
import colors

clock = pygame.time.Clock()

pygame.init()

def lvl1():
    msg1 = dialogue.Dialogue(fonts.pixel_font_24, "87?:Vous vous demandez ce que vous faites là ?", (200, 650))
    msg1.len()
    msg1.draw(globals.WIN)
    
    
    msg1.draw(globals.WIN)
    pygame.time.delay(3000)
    globals.WIN.fill(colors.GREY)
