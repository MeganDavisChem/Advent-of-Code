"""Perform power and life support diagnostics for the Elves' Submarine"""
#pylint: disable=C0103
import numpy as np

def commonNums(array, minMax):
    """Returns if one or zero is the most common number for each index in
    transposed array"""
    if minMax == "max":
        common = [np.bincount(row).argmax() for row in array]
    else:
        common = [np.bincount(row).argmin() for row in array]
    return common


def numCounts(array):
    """Returns total count for 1 and 0,  needed for ratingModule, aka I wish I
    had had more foresight"""
    common = [np.bincount(row) for row in array]
    return common


def binToInt(array):
    """converts binary array to base 10 int"""
    num = ''
    for element in array:
        num += str(element)
    num = int(num, 2)
    return num

def ratingModule(array, mol):
    """Generate O2 or CO2 metric"""
    #array needs to be in original format so we can iterate over each binary
    #number and choose which ones to keep
    array = array.transpose()
    for i in range(len(array[0])):
        #Calculate numCounts for current index
        mostCommon = numCounts(array.transpose())

        #Spaghetti code to pick 1 or 0 based on O2 or CO2 mode
        if mostCommon[i][0] == mostCommon[i][1]:
            if mol == 'O2':
                com = 1
            else:
                com = 0
        elif mol == 'O2':
            com = mostCommon[i].argmax()
        else:
            com = mostCommon[i].argmin()
        tempData = []
        #iterate through array and append matching numbers for current bit to
        #list
        for line in array:
            if com == line[i]:
                tempData.append(line.tolist())
        #store matching numbers as array, and we do it again
        array = np.array(tempData)
        #stop when we get to the value. Might not be necessary?
        if len(array) == 1:
            break
    #return a one dimensional array instead of [[]]
    return array[0]

#Read in file, strip newline characters, store as numpy int array, transpose
#I probably should have made this code clear instead of nesting like five
#different things
with open('input',encoding='utf-8') as f:
    data = np.array([list(line.rstrip()) for line in f],
            dtype='int').transpose()

#Find most frequent nums
gamma = commonNums(data, 'max')
epsilon = commonNums(data, 'min')

#convert from binary array to int and get power
gammaBin = binToInt(gamma)
epsilonBin = binToInt(epsilon)
power = gammaBin * epsilonBin

#Print for part one
print(f"""
~~~Submarine Power Consumption~~
Gamma rate:             {gammaBin}
Epsilon rate:           {epsilonBin}
Net power consumption:  {power}
""")

#Get O2 and CO2 metrics using the ratingModule
dataO2 = ratingModule(data, 'O2')
dataCO2 = ratingModule(data, 'CO2')

#convert to base 10, generate life support
O2 = binToInt(dataO2)
CO2 = binToInt(dataCO2)
lifeSupport = O2 * CO2

#print for Part 2
print(f"""
~~~Life Support Diagonistics~~~
Oxygen generator rating: {O2}
CO2 scrubber rating:     {CO2}
Life support rating:     {lifeSupport}
""")
