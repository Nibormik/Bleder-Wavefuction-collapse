import itertools
import json
Cells = []



def color(Key):
    if int(Key) == 1:
        return [132,255,24]
    if int(Key) == 2:
        return [98,187,255]
    if int(Key) == 3:
        return [255,5,142]
    if int(Key) == 4:
        return [233,180,78]
    if int(Key) == 5:
        return [102,65,71]
cell_types = itertools.permutations("22221111",4)
cell_types = set(cell_types)
for i,l in enumerate(list(cell_types)):
    Cells.append({  "Name":str(i),
                    "key":list(l),
                    "color": [
                        [color(5),color(l[0]),color(5)],
                        [color(l[3]),color(5),color(l[1])],
                        [color(5),color(l[2]),color(5)]
                        ]})
print(len(cell_types))
with open("Cells3.json", "w") as outfile:
    json.dump(Cells, outfile,indent = 4)
    