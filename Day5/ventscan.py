"""Scan the ocean floor for hydrothermal vents"""
import numpy as np

with open('input', encoding='utf-8') as file:
    data = file.readlines()

data = [line.rstrip().split('->') for line in data]

hori = []
vert = []
diag = []
for i, line in enumerate(data):
    line = [list(map(int, x.split(','))) for x in line]
    if line[0][0] == line[1][0]:
        vert.append(line)
    elif line[0][1] == line[1][1]:
        hori.append(line)
    else:
        diag.append(line)

seaFloor = np.zeros((1000,1000), dtype='int')

for line in hori:
    y = line[0][1]
    if line[0][0] < line[1][0]:
        scan = range(line[0][0],line[1][0]+1)
    else:
        scan = range(line[1][0],line[0][0]+1)
    for num in scan:
        seaFloor[num][y] += 1

for line in vert:
    x = line[0][0]
    if line[0][1] < line[1][1]:
        scan = range(line[0][1],line[1][1]+1)
    else:
        scan = range(line[1][1],line[0][1]+1)
    for num in scan:
        seaFloor[x][num] += 1

overlaps = len(np.where(seaFloor > 1)[0])
print("~~~Part One~~~")
print(f"# of overlaps: {overlaps}")

for line in diag:
    x1 = line[0][0]
    x2 = line[1][0]
    y1 = line[0][1]
    y2 = line[1][1]
    #this is extremely hacky but i'm stupid right now
    if x1 < x2:
        #forwards positive slope
        if y1 < y2:
            scan = range(x1,x2+1)
            for num in scan:
                seaFloor[num][y1] += 1
                y1 += 1
        #forwards negative slope
        elif y1 > y2:
            scan = range(x1,x2+1)
            for num in scan:
                seaFloor[num][y1] += 1
                y1 -= 1
    if x1 > x2:
        #backwards negative slope
        if y1 < y2:
            scan = range(x2,x1+1)
            for num in scan:
                seaFloor[num][y2] += 1
                y2 -= 1
        #backwards positive slope
        elif y1 > y2:
            scan = range(x2,x1+1)
            for num in scan:
                seaFloor[num][y2] += 1
                y2 += 1

overlaps = len(np.where(seaFloor > 1)[0])
print("~~~Part Two~~~")
print(f"# of overlaps: {overlaps}")
