import json
Cells = []
while True:
    Name = input("Name: ")
    Image = input("Type Image name: ")
    Cells.append({  "Name":Name,
                    "key":list(Name),
                    "image":"./Tiles/"+Image+".png"})
    
    if input("add another cell?: ")=="n":
        break
with open("Cells_image.json", "w") as outfile:
    json.dump(Cells, outfile,indent = 4)