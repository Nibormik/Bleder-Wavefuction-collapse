import json
Cells = []
while True:
    Name = input("Name: ")
    N = eval(input("N: "))
    S = eval(input("S: "))
    E = eval(input("E: "))
    W = eval(input("W: "))
    Mesh = None
    Cells.append({  "Name":Name,
                    "key":[N,E,S,W]})
    if input("add another cell?: ")=="n":
        break
with open("Cells.json", "w") as outfile:
    json.dump(Cells, outfile,indent = 4)