import pygame
import globals
globals.WIN = pygame.display.set_mode((globals.WIDTH, globals.HEIGHT));
bg= pygame.image.load('assets/wscreen.png')
pygame.init()
pygame.display.flip()
alive= True

while alive:
  
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      alive = False
    globals.WIN.fill((255,255,255))
    globals.WIN.blit(bg,(0,0))
    pygame.display.flip()


pygame.quit()    