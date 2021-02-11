import pygame
import globals
import score
import sprites

#globals.WIN = pygame.display.set_mode((globals.WIDTH, globals.HEIGHT));
def end_screen():
  globals.WIN = pygame.display.set_mode((globals.WIDTH, globals.HEIGHT))
  pygame.display.flip()
  alive= True

  globals.SCORE.add(globals.NB_MORTS)
  while alive:
    
    for event in pygame.event.get():
      if event.type == pygame.QUIT:
        alive = False
      globals.WIN.fill((255,255,255))
      globals.WIN.blit(sprites.sl["end_screen"],(0,0))
      pygame.display.flip()


  pygame.quit()