import pygame
from pygame.locals import *
import sys
import os
import time

from WFC import *

pygame.init()

SIZE = (32,64)
CELL_SET = "./Cells_image.json"
CELL_SIZE = 15
DISPLAY_SIZE = (SIZE[1]*CELL_SIZE,SIZE[0]*CELL_SIZE)
flags= []
DISPLAY = pygame.display.set_mode(DISPLAY_SIZE,pygame.SCALED)
DRAW_SURFACE = pygame.display.set_mode(DISPLAY_SIZE,pygame.SCALED)
DRAW_SURFACE = pygame.transform.rotate(DRAW_SURFACE,90)
DONE = False
ITER = 0
SAVED = False
iterate = 0
it_psec = 0
draw = 0

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

def draw_image(pos_X,pos_Y,size):
    posX = pos_X * size
    posY = pos_Y * size
    if WFC.cell_grid[pos_X][pos_Y].Cell:
        imp = pygame.image.load(WFC.cell_grid[pos_X][pos_Y].Cell["image"]).convert()
        imp = pygame.transform.rotate(imp,90)
        DRAW_SURFACE.blit(imp, (posX, posY))


tot_time = time.monotonic()
while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    if not DONE:
        ITER += 1
        cells_left = 0
        Tick_speed = time.monotonic()
        DONE = WFC.tick()
        Tick_speed = time.monotonic() - Tick_speed


    else:
        if not SAVED:
            pygame.image.save(DISPLAY,'Output.png')
    if time.monotonic() - draw > 1:

        for x,v in enumerate(WFC.cell_grid):
            for y,v in enumerate(v):
                if v.Cell == None:
                    cells_left += 1
                draw_image(x,y,CELL_SIZE)


        DISPLAY.blit(pygame.transform.rotate(DRAW_SURFACE,-90),(0,0))
        pygame.display.update()
        draw = time.monotonic()

        it_psec = ITER - iterate
        iterate = ITER

        os.system("cls")
        print("Collapsing Cells")
        print(f"Iterations: {ITER}, Iterations p/s: {it_psec} ,Iteration time: {Tick_speed}")
        print(f"Cells left: {cells_left}, Tot time {time.monotonic()-tot_time}")