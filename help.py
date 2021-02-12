import pygame
import globals
import sprites

def help():
  globals.WIN = pygame.display.set_mode((globals.WIDTH, globals.HEIGHT));
  alive= True
  while alive:
    
    for event in pygame.event.get():
      if event.type == pygame.QUIT:
        alive = False
        
    rect = pygame.Rect(0, 0, globals.WIDTH, globals.HEIGHT)
    globals.WIN.blit(pygame.image.load("assets/help.png"), rect)

    pygame.display.flip()