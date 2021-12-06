"""Find population of laternfish"""
INP = 'input'
with open(INP, encoding='utf-8') as f:
    pops = list(map(int, f.read().rstrip().split(',')))

DAYS = 255
dayRange = range(0,DAYS)

#categorize based on cycle day
newPops = sortPops = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
for fish in pops:
    sortPops[fish] += 1
print(f"Initial state: {sortPops}")

#loop over each day
#this took a lot of iteration and made me feel stupid
#I also don't know why the day range is off by one whatever
for day in dayRange:
    TOTAL = 0
    #spawn new fish based on # in 0 pool on prev day
    newPops[7] += sortPops[0]
    #set yesterday's results to today
    sortPops = newPops
    #calculate new pops
    for i in range(0,9):
        newPops[i] = sortPops[i+1]
    #this has to be appended to the end to make it a closed loop
    newPops[9] = sortPops[0]
    #print
    print(f"After {day+1} days: {newPops}")
    for i in newPops:
        TOTAL += i
    print(f"There are {TOTAL} fish")
