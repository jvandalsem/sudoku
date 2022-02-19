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
printBoard(board)
class Squares:
    def __init__(self,square,row,col,block):
        self.value = square
        self.row = row
        self.col = col
        self.block = block

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
        squareObjects.append(Squares(square,board.index(row),i,block))
for a in squareObjects:
    print(a.value,a.row,a.col,a.block)
