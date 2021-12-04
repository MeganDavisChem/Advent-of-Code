"""Emergency protocol for cheating at bingo in case of obstinate aqueous enemies"""
import numpy as np

#define functions
def pos_check(array, num):
    """checks if a number is in a board and returns its position"""
    return [int(ps) for ps in np.where(array == num)]

def get_score(bingoboard, scoreboard, call):
    """Gets score for a given board"""
    score_zeroes = np.where(scoreboard == 0)
    zeroes_coords = []
    score = 0
    for num in range(len(score_zeroes[0])):
        zeroes_coords.append([coord[num] for coord in score_zeroes])
    for coord in zeroes_coords:
        score += bingoboard[coord[0]][coord[1]]
    score *= call
    return score

#open file
with open('input', encoding='utf-8') as file:
    rawData = file.read()

#Split based on double lines to separate callouts and boards
data = rawData.split('\n\n')
callouts = data[0]
boards = data[1:]

#process callouts and boards into useful data structures
callouts = [int(num) for num in callouts.split(',')]
boards = [line.split('\n') for line in boards]
boards[-1].remove('')

#convert boards to numpy arrays, and make corresponding boardScores matrix, will flip 0
#to 1 for each number that is called out
boardScores = []
for i,board in enumerate(boards):
    boards[i] = np.array([line.split() for line in board], dtype='int')
    boardScores.append(np.zeros((5, 5), dtype=int))

#Part Two logic: we tweak things slightly: Put score checking inside of the if
#callout statement, and then make a running list of goodBoards and remove them
#from the iterative count, and find the scores for every board til we get to the
#last one

#Loop over callouts and boards
goodBoards = []
lastCalls = []
for callout in callouts:
    for i,board in enumerate(boards):
        if callout in board and i not in goodBoards:
            pos = pos_check(board, callout)
            #flip score bit for current board
            boardScores[i][pos[0]][pos[1]] = 1
            #now we need a check for when a board has won.
            scores = boardScores[i].sum(axis=0).tolist() +\
            boardScores[i].sum(axis=1).tolist()
            #append winning board to running list
            if 5 in scores:
                lastCalls.append(callout)
                goodBoards.append(i)
        #break nested loop when we get to the last board
        if len(goodBoards) == len(boards):
            break
    else:
        continue
    break

#winners and losers
winningBoard = boards[goodBoards[0]]
winningScore = boardScores[goodBoards[0]]
winningCall = lastCalls[0]
winScore = get_score(winningBoard, winningScore, winningCall)

losingBoard = boards[goodBoards[-1]]
losingScore = boardScores[goodBoards[-1]]
losingCall = lastCalls[-1]
loseScore = get_score(losingBoard, losingScore, losingCall)

#Print stuff
print(f"""~~~Winning Board~~~
The final score is: {winScore}
Final callout was:      {winningCall}

Winning Board:
{winningBoard}

Marked numbers:
{winningScore}
""")

print(f"""~~~Losing Board~~~
The final score is: {loseScore}
Final callout was:      {lastCalls[-1]}

Losing Board:
{losingBoard}

Marked numbers:
{losingScore}
""")
