import pygame
from pygame.locals import *
import sys
import os

from WFC import *

pygame.init()

SIZE = (128,128)
DISPLAY_SIZE = (SIZE[0]*3,SIZE[1]*3)
flags= []
DISPLAY = pygame.display.set_mode(DISPLAY_SIZE,pygame.SCALED)

DONE = False
ITER = 0

print(str(type(SIZE)))
print("Generating Grid")
WFC = grid('./Cells3.json',SIZE)


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
            draw_pixel(x,y,3)
        
    pygame.display.update()



def draw_pixel(img,pos_X,pos_Y,size):
    posX = pos_X * size
    posY = pos_Y * size
    for x in range(0,size):
        for y in range(0,size):
            colors = WFC.cell_grid[pos_X][pos_Y].Cell["color"]
            surface.set_at((posX+x,posY-y+2), tuple(colors[x][y]))

print("Generating Grid")
collapsed = False
WFC = grid('./Cells2.json',256)

Wave = Image.new("RGB",(WFC.size[0]*3,WFC.size[0]*3),(0))
Wave_cells = Wave.load()

iterations = 0

print("Starting Cell Collapsing")
while not collapsed:
    iterations += 1
    collapsed = WFC.tick()
    os.system("cls")
    print("Collapsing Cells")
    print(f"Iterations {iterations}")

print("Generating image")

for x,v in enumerate(WFC.cell_grid):
    for y,V in enumerate(v):
        draw_pixel(Wave_cells,x,y,3)
Wave.save("wave.png")
print("done")