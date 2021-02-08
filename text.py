import pygame
from pygame import *



def draw_text(text,size, x, y):
    pixel_font = pygame.font.Font("assets/pixel_font.ttf")
    img = pixel_font.render('chalkduster.ttf',True, BLUE)