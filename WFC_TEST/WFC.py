import json


class cell:
    def __init__(self,Cell_list,pos):
        self.pos = pos
        self.Cell_list = Cell_list
        self.Cell = Cell_list[0]
    
class grid:
    def __init__(self,file,size) -> None:
        self.cell_grid = []
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
