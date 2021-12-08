"""Finds sub position"""
#pylint: disable=C0103
with openen('input', encoding='utf-8') as f:
    data = [line.split() for line in f.readlines()]

#I want to use list comprehension even though it's probably not the best case
#case for it

#There's probably a neater way to do this?
forwards = [int(line[1]) for line in data if line[0] == 'forward']
ups = [int(line[1]) for line in data if line[0] == 'up']
downs = [int(line[1]) for line in data if line[0] == 'down']


#Part one
subPosX = sum(forwards)
subPosY = sum(downs) - sum(ups)
subMult = subPosX * subPosY

#Print stuff
print(f"""~~~Movement Results (Part One)~~~
X:          {subPosX}
Y:          {subPosY}
Multiplied: {subMult}
""")

#Part Two
#List comprehensions probably won't work here lol
subX = 0
subY = 0
aim = 0

for line in data:
    num = int(line[1])
    if line[0] == 'up':
        aim -= num
    elif line[0] == 'down':
        aim += num
    elif line[0] == 'forward':
        subX += num
        subY += num*aim
    print(f"{line}> aim: {aim} ; ({subX}, {subY})")

mult = subX * subY
print(f"""
~~~Summary~~~
Final x: {subX}
Final y: {subY}
Final mult: {mult}
""")
