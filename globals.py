WIDTH = 1024
HEIGHT = 728
GAME_WIDTH = 30
GAME_HEIGHT = 20
OBJECT_WIDTH = int(WIDTH / GAME_WIDTH)
OBJECT_HEIGHT = int(HEIGHT / GAME_HEIGHT)
ZOOM = 40 # en %
WIN = None
LVL = None
MAX_ENERGY = 10
#pixel_font = pygame.font.Font("assets/pixel_font.ttf", 26)

def calcX(x):
    return OBJECT_WIDTH * x

def calcY(y):
    return OBJECT_HEIGHT * y

def isWall(x, y):
    if x < 0 or x > GAME_WIDTH - 1 or y < 0 or y > GAME_HEIGHT - 1 or LVL[y][x] == 1:
        return True
    else:
        return False