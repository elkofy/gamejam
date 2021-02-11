import globals
from globals import *
import tile
from tile import *
from enum import Enum
mobs = []
class Directions(Enum):
    Up = 0
    Down = 1
    Left = 2
    Right = 3
class Mob(tile.Tile):        
    dirX = 0
    dirY = 0
    sort = None
    speed = 30
    walking = False

    def __init__(self, x, y, sort, dir):
        global mobs
        Tile.__init__(self, x, y)
        self.sort = sort
        self.setDir(dir)
        mobs.append(self)
        print(sort + str(globals.Jour))


    def draw(self):
        Tile.draw(self)
        globals.WIN.blit(sl["m_" + self.sort], self.rect)

    def move(self):
        self.speed += 1
        if self.speed >= 30 and self.walking and not globals.isWall(self.x + self.dirX, self.y + self.dirY):
                globals.MAP[self.y][self.x] = tile.Tile(self.x, self.y)
                self.x += self.dirX
                self.y += self.dirY
                globals.MAP[self.y][self.x] = self
                self.speed = 0
        if self.isPlayerVisible():
            self.walking = True
        
        if self.x == globals.PLAYER.x and self.y == globals.PLAYER.y:
            globals.PLAYER.death()
            

    def setDir(self, dir):
        if dir == 2:
            self.dirX = -1
            self.dirY = 0
        if dir == 3:
            self.dirX = 1
            self.dirY = 0
        if dir == 0:
            self.dirX = 0
            self.dirY = -1
        if dir == 1:
            self.dirX = 0
            self.dirY = 1
    
    def isPlayerVisible(self):
        x = self.x + self.dirX
        y = self.y + self.dirY
        
        while not globals.isWall(x, y):
            if x == globals.PLAYER.x and y == globals.PLAYER.y:
                return True
            else:
                x = x + self.dirX
                y = y + self.dirY

        return False
        

