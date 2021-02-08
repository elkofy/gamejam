import pygame

WIN = pygame.display.set_mode((900, 900));
pygame.display.set_caption("new game");

def main():
    run = True
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
        WIN.fill((155, 155, 155))
        pygame.display.update()
    pygame.quit()
if __name__ == "__main__" :
    main()