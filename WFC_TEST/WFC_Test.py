import json
class Cell:
    def __init__(self,Cells):
        self.Pos = None,None
        self.cell = Cells

    def update(self,index,icell):
        new_cells = []
        Oindex = index
        index += 2
        if index > 3: index -= 4
        if index < 0: index += 4
        for C in icell:
            for v in self.cell:
                if C["key"][Oindex] == v["key"][index]:
                    if new_cells.count(v) == 0:
                        new_cells.append(v)
        Ocell = self.cell
        self.cell = list(new_cells)
        if Ocell != self.cell:
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
            grid[x][y].update(i,self.cell)

with open('./Cells.json', 'r') as Cellsf:
    Cells = json.load(Cellsf)


grid = []
for i in range(0,3):
    gx = []
    for o in range(0,3):
        cell = Cell(Cells)
        cell.Pos = (i,o)
        gx.append(cell)
    grid.append(gx)

cell = grid[1][1]
cell.cell = [Cells[0]]
cell.update_adjasent()
for x in grid:
    l = ""
    for y in x:
        if len(y.cell):
            l += y.cell[0]["Name"]
        else:
            l += "0"
    print(l)
