import pygame
from pygame.locals import *
import sys
import os
import time
import json

from WFC import *


SIZE = (32,32)
CELL_SIZE = 15
DISPLAY_SIZE = (SIZE[1]*CELL_SIZE,SIZE[0]*CELL_SIZE)
flags= []
DONE = False
ITER = 0
SAVED = False
iterate = 0
it_psec = 0
draw = 0

CELL_LOC = "./Cells_image.json"
with open("./Cells.json", 'r') as Cell_list_f:
    CELL_SET = json.load(Cell_list_f)
CELL_SET = cell_layout

print("Generating Grid")
WFC = Grid(10,10,cells=CELL_SET)


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
while not DONE:
    ITER += 1
    cells_left = 0
    Tick_speed = time.monotonic()
    DONE = WFC.tick()
    Tick_speed = time.monotonic() - Tick_speed

    if time.monotonic() - draw > 0.1:
        draw = time.monotonic()

        it_psec = ITER - iterate
        iterate = ITER

        os.system("cls")
        print("Collapsing Cells")
        print(f"Iterations: {ITER}, Iterations p/s: {it_psec} ,Iteration time: {Tick_speed}")
        print(f"Cells left: {cells_left}, Tot time {time.monotonic()-tot_time}")


os.system("cls")
print("Collapsing Cells")
print(f"Iterations: {ITER}, Iterations p/s: {it_psec} ,Iteration time: {Tick_speed}")
print(f"Cells left: {cells_left}, Tot time {time.monotonic()-tot_time}")

pygame.init()
DISPLAY = pygame.display.set_mode(DISPLAY_SIZE,pygame.SCALED)
DRAW_SURFACE = pygame.display.set_mode(DISPLAY_SIZE,pygame.SCALED)
DRAW_SURFACE = pygame.transform.rotate(DRAW_SURFACE,90)
        
while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
    for i,v in enumerate(WFC.grid):
        draw_image(i,CELL_SIZE)
    DISPLAY.blit(pygame.transform.rotate(DRAW_SURFACE,-90),(0,0))
    pygame.display.update()
    if not SAVED:
        pygame.image.save(DISPLAY,'Output.png')
        SAVED = True