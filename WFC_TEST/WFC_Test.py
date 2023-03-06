import json,random
from PIL import Image
Size_x = 10
Size_Y = 10

class Cell:
    def __init__(self,Cells):
        self.Pos = None,None
        self.cell = Cells

    def update(self):
        x,y = self.Pos
        adjasent = [(x+1,y),(x,y+1),(x-1,y),(x,y-1)]
        for i,v in enumerate(adjasent):
            x,y = v
            if x > len(grid)-1 or  x < 0: continue
            if y > len(grid[0])-1 or  y < 0: continue

            new_cells = []
            index = i + 2
            if index > 3: index -= 4
            if index < 0: index += 4

            Icell = grid[x][y].cell
            for C in Icell:
                for v in self.cell:
                    if C["key"][i] == v["key"][index]:
                        if new_cells.count(v) == 0:
                            new_cells.append(v)

            Ocell = self.cell
            self.cell = new_cells
            if len(Ocell) != len(self.cell):
                self.update_adjasent()

    def update_adjasent(self):
        x,y = self.Pos
        adjasent = [(x+1,y),(x,y+1),(x-1,y),(x,y-1)]
        for i,v in enumerate(adjasent):
            if v == None:
                continue
            x,y = v
            if x > len(grid)-1 or  x < 0:
                continue
            if y > len(grid[0])-1 or  y < 0:
                continue
            grid[x][y].update()

def draw_pixel(img,pos_X,pos_Y,size):
    posX = pos_X * size
    posY = pos_Y * size
    for x in range(0,size):
        for y in range(0,size):
            colors = grid[pos_X][pos_Y].cell[0]["color"]
            img[posX+x,posY+y] = tuple(colors[x][y])

with open('./Cells.json', 'r') as Cellsf:
    Cells = json.load(Cellsf)

collapsed = False

Wave = Image.new("RGB",(Size_x*3,Size_Y*3),(0))
Wave_cells = Wave.load()

grid = []
for i in range(0,Size_x):
    gx = []
    for o in range(0,Size_Y):
        cell = Cell(Cells)
        cell.Pos = (i,o)
        gx.append(cell)
    grid.append(gx)

while not collapsed:
    Random_cell = []
    for x in grid:
        for C in x:
            if len(C.cell) > 1:
                if len(Random_cell) == 0:
                    Random_cell.append(C)
                else:
                    if len(C.cell) < len(Random_cell[0].cell):
                        Random_cell = [C]
                    if len(C.cell) == len(Random_cell[0].cell):
                        Random_cell.append(C)
    if len(Random_cell) == 0:
        collapsed = True
        break
    Sel_Cell = Random_cell[random.randint(0,len(Random_cell)-1)]
    Sel_Cell_cell = Sel_Cell.cell[random.randint(0,len(Sel_Cell.cell)-1)]
    Sel_Cell.cell = [Sel_Cell_cell]
    Sel_Cell.update_adjasent()

for x,v in enumerate(grid):
    for y,V in enumerate(v):
        draw_pixel(Wave_cells,x,y,3)
Wave.save("wave.png")


