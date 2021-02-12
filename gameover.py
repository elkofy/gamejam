import pygame
import globals
import score
import sprites
import leaderboard
import save

#globals.WIN = pygame.display.set_mode((globals.WIDTH, globals.HEIGHT));
def end_screen():
  s = save.Save()
  s.add(globals.NAME, 1)
  globals.WIN = pygame.display.set_mode((globals.WIDTH, globals.HEIGHT))
  pygame.display.flip()
  alive= True
  globals.SCORE.add(globals.NB_MORTS)
  print(globals.SCORE.score)
  while alive:
    
    for event in pygame.event.get():
      if event.type == pygame.QUIT:
        alive = False
      globals.WIN.fill((255,255,255))
      globals.WIN.blit(sprites.sl["end_screen"],(0,0))
      leaderboard.show_leaderboard()
      pygame.display.flip()


  pygame.quit()