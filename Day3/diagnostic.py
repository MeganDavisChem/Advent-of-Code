"""Calculate gamma rate and epsilon rate"""
#pylint: disable=C0103
import numpy as np

def commonNums(array, minMax):
    """Returns most common numbers"""
    if minMax == "max":
        common = [np.bincount(row).argmax() for row in array]
    else:
        common = [np.bincount(row).argmin() for row in array]
    return common

def binToInt(array):
    """converts binary array to base 10 int"""
    num = ''
    for element in array:
        num += str(element)
    num = int(num, 2)
    return num
#Read in file, strip newline characters, store as numpy int array, transpose
#I probably should have made this code clear instead of nesting like five
#different things
with open('input',encoding='utf-8') as f:
    data = np.array([list(line.rstrip()) for line in f],
            dtype='int').transpose()

#Find most frequent numbers for each column

#gamma = [np.bincount(row).argmax() for row in data]
gamma = commonNums(data, 'max')
epsilon = commonNums(data, 'min')

#Concatenate into string
#gammaBin = ''
#epsilonBin = ''
#
#for i in gamma:
#    gammaBin += str(i)
#for j in epsilon:
#    epsilonBin += str(j)
#
##Convert string from binary into base 10 int, multiply and print result
#gammaBin = int(gammaBin, 2)
#epsilonBin = int(epsilonBin, 2)
#let's see if the funciton works

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


#Part two

#Find most common bit of row 1

#Discard all numbers that don't have that bit for data[0][number]

#Repeat until all rows have been looped through or until there is only one
#number remaining. Could do a while loop or use if len(data) == 1 break

#for i,line in enumerate(data):
#    mostCommon = commonNums(data, 'max')
#    print(mostCommon[i])
#    for bit in mostCommon:
#        pass

#Let's try while loop structure. Loop until one value remains
#dataO2 = dataCO2 = data

#turn dataO2 into the original form of the data which it should have been in the
#first place
dataO2 = data.transpose()

#iterate over indices
for i in range(len(gamma)):
    #Calculate commonNums for current index
    mostCommon = commonNums(dataO2.transpose(), 'max')
    tempData = []
    #iterate through transpose and append correct numbers to a new list
    for line in dataO2:
        if mostCommon[i] == line[i]:
            tempData.append(line.tolist())
    dataO2 = np.array(tempData)
    if len(dataO2) == 1:
        break

#convert number from binary
O2 = ''
for i in dataO2[0]:
    O2 += str(i)
O2 = int(O2, 2)
#This logic works!
#Now I just need to write a function that converts from an array in binary to a
#single number
#Then I need to write a function that does the iteration but switches with a max
#min flag
#actually wait I can just do that here. Actually yeah I'll do a function that'll
#make more sense
