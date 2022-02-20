#Soduko Solver
import random
board = [[' ',' ',' ',7,9,' ',' ',5,' '],
         [3,5,2,' ',' ',8,' ',4,' '],
         [' ',' ',' ',' ',' ',' ',' ',8,' '],
         [' ',1,' ',' ',7,' ',' ',' ',4],
         [6,' ',' ',3,' ',1,' ',' ',8],
         [9,' ',' ',' ',8,' ',' ',1,' '],
         [' ',2,' ',' ',' ',' ',' ',' ',' '],
         [' ',4,' ',5,' ',' ',8,9,1],
         [' ',8,' ',' ',3,7,' ',' ',' ']]

def printBoard(board):
    for a in board:
        print('[{}|{}|{}][{}|{}|{}][{}|{}|{}|]'.format(a[0],a[1],a[2],
                                                       a[3],a[4],a[5],
                                                       a[6],a[7],a[8]))
class Squares:
    def __init__(self,square,row,col,block):
        self.value = square
        self.row = row
        self.col = col
        self.block = block

def populateBoardDict(board):
    boardDict = {'rows':{},'cols':{},'blocks':{}}
    for i,row in enumerate(board):
        boardDict['rows'][i] = [r for r in row]
        boardDict['blocks'][i] = []
    for i,col in enumerate(list(zip(*board))):
        boardDict['cols'][i] = [c for c in col]
    return boardDict
boardAttr = populateBoardDict(board)
def instantiateSquares(board):
    squareObjects = []
    block = int()
    for row in board:
        for i,square in enumerate(row):
            if board.index(row) <= 2:
                if i <= 2:
                    block = 0
                elif i > 2 and i <= 5:
                    block = 1
                else:
                    block = 2
            elif board.index(row) > 2 and board.index(row) <= 5:
                if i <= 2:
                    block = 3
                elif i > 2 and i <= 5:
                    block = 4
                else:
                    block = 5
            else:
                if i <= 2:
                    block = 6
                elif i > 2 and i <= 5:
                    block = 7
                else:
                    block = 8
            boardAttr['blocks'][block].append(square)
            squareObjects.append(Squares(square,board.index(row),i,block))
    return squareObjects
squareAttr = instantiateSquares(board)
possibilityMatrix = {}
for square in squareAttr:
    for a in range(1,10):
        if a != square.value:
            if a not in boardAttr['rows'][square.row] and a not in boardAttr['cols'][square.col] and a not in boardAttr['blocks'][square.block]:
                if (square.row,square.col,square.block) not in possibilityMatrix:
                    possibilityMatrix[(square.row,square.col,square.block)] = []
                possibilityMatrix[(square.row,square.col,square.block)].append(a)

print(possibilityMatrix)
