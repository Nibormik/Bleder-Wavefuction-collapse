import json


class cell:
    def __init__(self,Cell_list,pos):
        self.pos = pos
        self.Cell_list = Cell_list
        self.Cell = Cell_list[0]

    def update(self,Acells):
        
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
        self.size = size
        with open(file, 'r') as Cell_list_f:
            Cell_list = json.load(Cell_list_f)

        if type(size) == "tuple": sizex,sizey=size
        else: sizex,sizey = (size,size)

        for x in range(sizex):
            gx = []
            for y in range(sizey):
                gx.append(cell(Cell_list,(x,y)))
            self.cell_grid.append(gx)
            
    def __str__ (self):
        out = ""
        for gx in self.cell_grid:
            for gy in gx:
                out += "|"+gy.Cell_list[0]["Name"]
            out += "|"+"\n"
        return out


WFC = grid('./Cells.json',10)
print(WFC)
