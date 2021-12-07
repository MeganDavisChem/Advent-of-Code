"""Align crab submarines"""

INP = 'input'
with open(INP, encoding='utf-8') as file:
    crabs = list(map(int, file.read().rstrip().split(',')))

#set up stuff for loops
largest = max(crabs)
smallest = min(crabs)
crabRange = range(smallest,largest+1)
#we're doing this the dumb way and checking every possible horizontal position
fuels = [0 for num in list(crabRange)]

for pos in range(smallest,largest+1):
    #calculate distance for each crab to new position
    for crab in crabs:
        fuels[pos] += abs(pos - crab)

#find minimum fuel usage
minFuel = min(fuels)
print(f"Least fuel is {minFuel}")

#part two. Only difference is using a formula for sum of + integers less than
#current integer
fuels = [0 for num in list(crabRange)]
for pos in range(smallest,largest+1):
    #calculate distance for each crab to new position
    for crab in crabs:
        step = abs(pos - crab)
        fuels[pos] += step + (step)*(step-1)//2
minFuel = min(fuels)
print(f"Least fuel is {minFuel}")
