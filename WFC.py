"""WFC lib v2"""
import json
import random

cell_layout = [{
    "name": "oof",
    "dir": {
        "N" : [0],
        "S" : [1],
        "E" : [0],
        "W" : [1],
        "U" : [0],
        "D" : [0]
    }
},{
    "name": "oof",
    "dir": {
        "N" : [1],
        "S" : [0],
        "E" : [1],
        "W" : [0],
        "U" : [0],
        "D" : [0]
    }
}]

class Cell:
    pos: tuple[int]
    supported_neighbours: list[str]
    posiible_cells: set[dict]
    cell: dict = {}
    
    def __init__(self,pos:tuple , cell_solutions:list) -> None:
        self.pos = pos
        self.posiible_cells = cell_solutions

class Grid:
    grid_3d:bool
    grid_size: tuple[int]
    grid: list[Cell]
    update_que: set

    def __init__(self, size_x: int, size_y: int, size_z:int=0, cells:list = [0], grid_3d = False):
        self.grid_3d = grid_3d
        self.grid_size = (size_x,size_y,size_z)
        self.grid = []
        for x in range(size_x): # loops throug x y (z) and adds starting values
            for y in range(size_y):
                if self.grid_3d: # adds 3rd dimention if grid_3d = True
                    for z in range(size_y):
                        self.grid.append(Cell((x,y,z),cells))
                else:
                    self.grid.append(Cell((x,y),cells))

    def get_index(self, x, y,z=0):
        """Gets the idex of a cell in the 3d/2d to 1d mapped list"""
        if self.grid_3d:
            return (x * self.grid_size[0] * self.grid_size[1]) + (y * self.grid_size[0]) + z
        else:
            return self.grid_size[0]*x+y

    def get_cell_neighbours(self,x,y,z=0):
            """Gets neighbors of supplied pos"""
            # self_index = self.get_index(x,y,z) #exsists to remove self values (probably not needed)
            neighbour_pos = {
                "N" : (x,y+1,z),
                "S" : (x,y-1,z),
                "E" : (x-1,y,z),
                "W" : (x+1,y,z),
                "U" : (x,y,z+1),
                "D" : (x,y,z-1)} # all possiible neighbors in 3d
            neighbour_indexes = []
            for dir in neighbour_pos:
                x,y,z = neighbour_pos[dir]
                if x>=self.grid_size[0] or x<0 or y>=self.grid_size[1] or y<0 or z >= self.grid_size[2] or z<0: continue
                neighbour_indexes.append((dir,self.grid[self.get_index(x,y,z)]))
            return neighbour_indexes
            # return [i for i in neighbour_indexes if i != self_index] # remooves values of self (probably not neccesary)
    
    def get_low_enthropy_cells(self):
        """Returns a list of low enthropy cells"""
        low_enthropy_cells = []
        for cell in self.grid:
                if cell.cell: continue
                elif len(low_enthropy_cells) == 0: low_enthropy_cells = [cell] # adds first possible value to list
                elif len(cell.posiible_cells) < len(low_enthropy_cells[0].posiible_cells): low_enthropy_cells = [cell] # replaces list with lower entropy value
                elif len(cell.posiible_cells) == len(low_enthropy_cells[0].posiible_cells): low_enthropy_cells.append(cell) # adds equal enthropy value to list
        return low_enthropy_cells
    
    def update_cell(self,cell):
        pass
    
    def run(self): # runs the WFC alg to completion
        done = False
        while not done:
            collapse_cell = random.choice(self.get_low_enthropy_cells())
            collapse_cell.cell = random.choice(collapse_cell.posiible_cells) # collapses the sell into on posibility
            collapse_cell.posiible_cells = [] # removes cell posibilities (probably redundent (might save memory but not really))

            self.update_que = self.get_cell_neighbours()
            while self.update_que:
                update_cell = self.update_que.pop(0)
                if update_cell.cell: continue





with open("./Cells.json", 'r') as Cell_list_f:
     Cell_list = json.load(Cell_list_f)
GRID = Grid(10,10,10,Cell_list,grid_3d=False)

print(GRID.grid[GRID.get_index(3,3,3)].pos)
print(GRID.get_cell_neighbours(2,2,2))
print(GRID.get_index(2,2,2))