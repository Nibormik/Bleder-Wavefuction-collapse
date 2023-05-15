import json
Cells = []
while True:
    Name = input("Name: ")
    weight = input("type weight: ")
    Image = input("Type Image name: ")
    Cells.append({  "Name":Name,
                    "key":list(Name),
                    "weight": weight,
                    "image":"./Tiles/"+Image+".png"})
    
    if input("add another cell?: ")=="n":
        break
with open("Cells_image.json", "w") as outfile:
    json.dump(Cells, outfile,indent = 4)