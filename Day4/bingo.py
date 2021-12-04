"""Emergency protocol for cheating at bingo in case of obstinate aqueous enemies"""
import numpy as np

def pos_check(array, num):
    """checks if a number is in a board and returns its position"""
    return [int(ps) for ps in np.where(array == num)]

with open('input', encoding='utf-8') as file:
    rawData = file.read()

def get_score(bingoboard, scoreboard):
    """Gets score for a given board"""
    score_zeroes = np.where(scoreboard == 0)
    zeroes_coords = []
    score = 0
    for num in range(len(score_zeroes[0])):
        zeroes_coords.append([coord[num] for coord in score_zeroes])
    for coord in zeroes_coords:
        score += bingoboard[coord[0]][coord[1]]
    score *= finalCall
    return score

#Split based on double lines to separate callouts and boards
data = rawData.split('\n\n')

#yank out callouts and boards
callouts = data[0]
boards = data[1:]

#process callouts into a list of ints
#it's probably time to learn pandas so I don't have to do so much of this
#manually every time
callouts = [int(num) for num in callouts.split(',')]

#process boards into numpy array
boards = [line.split('\n') for line in boards]
#remove final whitespace this is probably hacky af
boards[-1].remove('')
#convert to numpy arrays, and make corresponding boardScores matrix, will flip 0
#to 1 for each number that is called out
boardScores = []
for i,board in enumerate(boards):
    boards[i] = np.array([line.split() for line in board], dtype='int')
    boardScores.append(np.zeros((5, 5), dtype=int))

#Data processing step finished!
for callout in callouts:
    for i,board in enumerate(boards):
        if callout in board:
            #will turn this into a function
#            pos = [int(ps) for ps in np.where(board == callout)]
            pos = pos_check(board, callout)
            #flip score bit for current board
            boardScores[i][pos[0]][pos[1]] = 1
            #so far so good!
        #now we need a check for when a board has won.
        scores = boardScores[i].sum(axis=0).tolist() +\
        boardScores[i].sum(axis=1).tolist()
        #this may be unpythonic and/or dumb, but basically this is a structure
        #that breaks out of the nested loop if we get to a winning board
        if 5 in scores:
            winningBoard = board
            winningScore = boardScores[i]
            finalCall = callout
            break
    else:
        continue
    break

winScore = get_score(winningBoard, winningScore)
print(f"""~~~Results~~~
The final score is: {winScore}
Final callout was:      {finalCall}

Winning Board:
{winningBoard}

Marked numbers:
{winningScore}
""")


#Part Two logic: we tweak things slightly: Put score checking inside of the if
#callout statement, and then make a running list of goodBoards and remove them
#from the iterative count, and find the scores for every board til we get to the
#last one
goodBoards = []
for callout in callouts:
    for i,board in enumerate(boards):
        if callout in board and i not in goodBoards:
            #will turn this into a function
#            pos = [int(ps) for ps in np.where(board == callout)]
            pos = pos_check(board, callout)
            #flip score bit for current board
            boardScores[i][pos[0]][pos[1]] = 1
            #so far so good!
        #now we need a check for when a board has won.
            scores = boardScores[i].sum(axis=0).tolist() +\
            boardScores[i].sum(axis=1).tolist()
        #this may be unpythonic and/or dumb, but basically this is a structure
        #that breaks out of the nested loop if we get to a winning board
            if 5 in scores:
                winningBoard = board
                winningScore = boardScores[i]
                finalCall = callout
                goodBoards.append(i)
        #break when we get to the last board
        if len(goodBoards) == len(boards):
            break
    else:
        continue
    break

winScore = get_score(winningBoard, winningScore)
print(f"""~~~Results~~~
The final score is: {winScore}
Final callout was:      {finalCall}

Winning Board:
{winningBoard}

Marked numbers:
{winningScore}
""")
