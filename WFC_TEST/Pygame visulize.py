import pygame
from pygame.locals import *
import sys
import os

from WFC import *

pygame.init()

SIZE = (32,32)
CELL_SET = "./Cells3.json"
CELL_SIZE = 3
DISPLAY_SIZE = (SIZE[0]*CELL_SIZE,SIZE[1]*CELL_SIZE)
flags= []
DISPLAY = pygame.display.set_mode(DISPLAY_SIZE,pygame.SCALED)

DONE = False
ITER = 0

print(str(type(SIZE)))
print("Generating Grid")
WFC = grid(CELL_SET,SIZE)


def draw_pixel(pos_X,pos_Y,size):
    posX = pos_X * size
    posY = pos_Y * size
    for x in range(0,size):
        for y in range(0,size):
            if WFC.cell_grid[pos_X][pos_Y].Cell:
                colors = WFC.cell_grid[pos_X][pos_Y].Cell["color"]
                DISPLAY.set_at((posX+x,posY-y+2), tuple(colors[x][y]))
            else:
                DISPLAY.set_at((posX+x,posY-y+2), (0,0,0))

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    if not DONE:
        ITER += 1
        DONE = WFC.tick()
        os.system("cls")
        print("Collapsing Cells")
        print(f"Iterations {ITER}")

    for x,v in enumerate(WFC.cell_grid):
        for y,V in enumerate(v):
            draw_pixel(x,y,CELL_SIZE)
        
    pygame.display.update()