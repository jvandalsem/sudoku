#Soduko Solver
import random
board = [[' ', ' ', ' ', ' ', ' ', ' ', ' ', 2, 8],
         [' ', 6, ' ', ' ', ' ', ' ', ' ', ' ', 7],
         [' ', ' ', ' ', 4, ' ', 1, ' ', ' ', ' '],
         [5, ' ', ' ', 9, 7, ' ', 3, ' ', ' '],
         [2, ' ', 4, ' ', ' ', 8, ' ', ' ', ' '],
         [3, ' ', ' ', ' ', ' ', 4, 5, ' ', ' '],
         [1, 3, ' ', ' ', 9, ' ', ' ', ' ', ' '],
         [' ', 5, 7, ' ', ' ', ' ', ' ', 9, ' '],
         [' ', ' ', 8, 3, 1, 7, ' ', ' ', ' ']]

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

def getData(board):
    squareObjects = []
    block = int()
    boardDict = {'rows':{},'cols':{},'blocks':{}}
    for i,row in enumerate(board):
        boardDict['rows'][i] = [r for r in row]
        boardDict['blocks'][i] = []
    for i,col in enumerate(list(zip(*board))):
        boardDict['cols'][i] = [c for c in col]
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
            boardDict['blocks'][block].append(square)
            squareObjects.append(Squares(square,board.index(row),i,block))
    return squareObjects, boardDict

def solve(board,squares,boardData):
    possibilityArray = {}
    inverseBlock = dict()
    for square in squares:
        for a in range(1,10):
            if square.value == ' ':
                if a not in boardData['rows'][square.row] \
                and a not in boardData['cols'][square.col] \
                and a not in boardData['blocks'][square.block]:
                    if (square.row,square.col,square.block) not in possibilityArray:
                        possibilityArray[(square.row,square.col,square.block)] = []
                    possibilityArray[(square.row,square.col,square.block)].append(a)
    for coord,vals in possibilityArray.items():
        for val in vals:
            if (str(coord[2])+','+str(val)) not in inverseBlock:
                inverseBlock[(str(coord[2])+','+str(val))] = []
            inverseBlock[(str(coord[2])+','+str(val))].append(coord)

    for coord in possibilityArray:
        if len(possibilityArray[coord])==1:
            board[coord[0]][coord[1]] = possibilityArray[coord][0]
    for combo in inverseBlock:
        if len(inverseBlock[combo]) == 1:
            board[inverseBlock[combo][0][0]][inverseBlock[combo][0][1]] = int(combo[2])

    squareDataRec,boardDataRec = getData(board)
    print('------------------------')
    printBoard(board)
    while any(' ' in row for row in board):
        solve(board,squareDataRec,boardDataRec)

squareAttr,boardAttr = getData(board)
solve(board,squareAttr,boardAttr)
