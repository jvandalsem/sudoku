#Soduko Solver
import random
board = [[[' ',' ',' '],[7,9,' '],[' ',5,' ']],
         [[3,5,2],[' ',' ',8],[' ',4,' ']],
         [[' ',' ',' '],[' ',' ',' '],[' ',8,' ']],
         [[' ',1,' '],[' ',7,' '],[' ',' ',4]],
         [[6,' ',' '],[3,' ',1],[' ',' ',8]],
         [[9,' ',' '],[' ',8,' '],[' ',1,' ']],
         [[' ',2,' '],[' ',' ',' '],[' ',' ',' ']],
         [[' ',4,' '],[5,' ',' '],[8,9,1]],
         [[' ',8,' '],[' ',3,7],[' ',' ',' ']]]

def printBoard(board):
    for a in board:
        print('[{}|{}|{}][{}|{}|{}][{}|{}|{}|]'.format(a[0][0],a[0][1],a[0][2],
                                                       a[1][0],a[1][1],a[1][2],
                                                       a[2][0],a[2][1],a[2][2]))
printBoard(board)
