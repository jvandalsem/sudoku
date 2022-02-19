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
    def __init__(self,square,x,y):
        self.value = square
        self.position = (x,y)

squareObjects = []
for row in board:
    for square in row:
        squareObjects.append(Squares(square,board.index(row),row.index(square)))
        # for square in tri:
        #     squareObjects.append(Squares(row,square))
for squares in squareObjects:
    print(squares.value,squares.position)
