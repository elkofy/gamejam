import pygame

pixel_font_24 = None
pixel_font_30 = None

def font_init():
    global pixel_font_24
    pixel_font_24 = pygame.font.Font("assets/pixel_font.ttf", 24)

    global pixel_font_30
    pixel_font_30 = pygame.font.Font("assets/pixel_font.ttf", 30)