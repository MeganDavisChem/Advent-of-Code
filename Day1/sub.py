count = 0
windowCount = 0
sumB = 0

#initialize with > 0 numbers for the loop logic (this is probably really dumb)
last = 0
lint = 10000

with open('input') as f:
    depths = f.readlines()

for i, line in enumerate(depths):
    print(f"~~~Iteration {i+1}~~~")
    #update variables
    last2 = last
    last = lint
    lint = int(line)
    
    #print stuff
    if lint > last:
        count += 1
        print(f"{lint}: higher than previous")
    elif i == 0:
        print(f"{lint}: n/a")
    else:
        print(f"{lint}: lower than previous")

    #check windows and print
    if i > 1:
        sumA = sumB
        sumB = lint + last + last2
        if sumB > sumA and i >2:
            windowCount += 1
            print(f"Window sum is {sumB}: higher than previous")
        else:
            print(f"Window sum is {sumB}: lower than previous")

print("\n~~~Summary~~~")
print(f"The total higher than previous is {count}")
print(f"The total windows higher than previous is {windowCount}")
