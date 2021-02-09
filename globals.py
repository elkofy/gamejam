WIDTH = 1024
HEIGHT = 768
GAME_WIDTH = 30
GAME_HEIGHT = GAME_WIDTH
OBJECT_WIDTH = 64
OBJECT_HEIGHT = OBJECT_WIDTH
PLAYER_SCALE = 0.85
PLAYER_WIDTH = OBJECT_WIDTH - 2 * int((1 - PLAYER_SCALE)/2 * OBJECT_WIDTH)
PLAYER_HEIGHT = OBJECT_HEIGHT - 2 * int((1 - PLAYER_SCALE)/2 * OBJECT_HEIGHT)
marginTop = None
marginLeft = None
WIN = None
LVL = None
MAX_ENERGY = 10
blind = False
#pixel_font = pygame.font.Font("assets/pixel_font.ttf", 26)

def calcX(x):
    return OBJECT_WIDTH * x

def calcY(y):
    return OBJECT_HEIGHT * y

def isWall(x, y):
    if x < 0 or x > GAME_WIDTH - 1 or y < 0 or y > GAME_HEIGHT - 1 or LVL[y][x] == "@":
        return True
    else:
        return False

def changeView(x, y):
    global marginLeft
    global marginTop
    marginLeft = calcX(x) - (WIDTH / 2) + OBJECT_WIDTH / 2
    marginTop = calcY(y) - (HEIGHT / 2) + OBJECT_HEIGHT / 2