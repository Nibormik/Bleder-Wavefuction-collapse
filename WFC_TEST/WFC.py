import json
import random
from PIL import Image
import os

class cell:
    def __init__(self,Cell_list,pos):
        self.pos = pos
        self.Cell_list = Cell_list
        self.Cell = None

    def update(self,size,grid):
        Acell_list = self.get_adjacent(size,grid)
        if self.Cell:
            return []
        Ocell = self.Cell_list
        for i,Acell in enumerate(Acell_list):
            if Acell ==None:
                continue
            new_cells = []
            index = i + 2
            if index > 3: index -= 4
            if index < 0: index += 4
            for C in Acell.Cell_list:
                    for v in self.Cell_list:
                        if C["key"][i] == v["key"][index]:
                            if new_cells.count(v) == 0:
                                new_cells.append(v)

            self.Cell_list = new_cells
        if len(Ocell) != len(self.Cell_list):
            return Acell_list
        if len(self.Cell_list) == 1:
            self.Cell = self.Cell_list[0]
        return []
            

    def get_adjacent(self,size,grid):
        size_x ,size_y = size
        Acells = []
        x,y = self.pos
        Apos_list = [(x+1,y),(x,y+1),(x-1,y),(x,y-1)]
        for Apos in Apos_list:
            x,y = Apos
            if x > size_x-1 or  x < 0:
                Acells.append(None)
                continue
            if y > size_y-1 or  y < 0:
                Acells.append(None)
                continue
            Acells.append(grid[x][y])
        return Acells
    
class grid:
    def __init__(self,file,size) -> None:
        self.cell_grid = []
        self.update_chain = []
        with open(file, 'r') as Cell_list_f:
            Cell_list = json.load(Cell_list_f)

        if type(size) == "tuple": self.size = size
        else: self.size = (size,size)
        sizex,sizey = self.size

        for x in range(sizex):
            gx = []
            for y in range(sizey):
                gx.append(cell(Cell_list,(x,y)))
            self.cell_grid.append(gx)
            
    def __str__ (self):
        out = ""
        for gx in self.cell_grid:
            for gy in gx:
                if gy.Cell:
                    out += "|"+gy.Cell["Name"]
                else:
                    out += "|0"
            out += "|"+"\n"
        return out
    def collapse(self,RCell_list):
        SCell = RCell_list[random.randint(0,len(RCell_list)-1)]
        SCell.Cell = SCell.Cell_list[random.randint(0,len(SCell.Cell_list)-1)]
        SCell.Cell_list = [SCell.Cell]
        Start = SCell.get_adjacent(self.size,self.cell_grid)

        for v in Start:
                if v == None:
                    continue
                self.update_chain.insert(0,v)

        while self.update_chain:
            Cell = self.update_chain.pop(0)
            update_list =  Cell.update(self.size,self.cell_grid)
            if len(update_list):
                for v in update_list:
                    if v == None:
                        continue
                    self.update_chain.insert(0,v)


def draw_pixel(img,pos_X,pos_Y,size):
    posX = pos_X * size
    posY = pos_Y * size
    for x in range(0,size):
        for y in range(0,size):
            colors = WFC.cell_grid[pos_X][pos_Y].Cell["color"]
            img[posX+x,posY-y+2] = tuple(colors[x][y])

print("Generating Grid")
collapsed = False
WFC = grid('./Cells2.json',32)

Wave = Image.new("RGB",(WFC.size[0]*3,WFC.size[0]*3),(0))
Wave_cells = Wave.load()

iterations = 0

print("Starting Cell Collapsing")
while not collapsed:
    iterations += 1
    Random_cell = []
    for x in WFC.cell_grid:
        for C in x:
            if C.Cell:
                continue
            if not len(Random_cell):
                Random_cell.append(C)
            else:
                if len(C.Cell_list) < len(Random_cell[0].Cell_list):
                    Random_cell = [C]
                if len(C.Cell_list) == len(Random_cell[0].Cell_list):
                    Random_cell.append(C)  
    if len(Random_cell):
        WFC.collapse(Random_cell)
    else:
        collapsed = True
    os.system("cls")
    print("Collapsing Cells")
    print(f"Iterations {iterations}")

print("Generating image")

for x,v in enumerate(WFC.cell_grid):
    for y,V in enumerate(v):
        draw_pixel(Wave_cells,x,y,3)
Wave.save("wave.png")
print("done")