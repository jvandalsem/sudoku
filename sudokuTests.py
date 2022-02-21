#Tests
import sudoku
board = sudoku.board
squareObj,boardD = sudoku.instantiateSquares(sudoku.board)
def testA(board,squares,boardData):
    sudoku.printBoard(board)
    for r in range(3):
        possibilityArray = dict()
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
                print('block',combo,inverseBlock[combo])
                board[inverseBlock[combo][0][0]][inverseBlock[combo][0][1]] = int(combo[2])
        print('----------------------')
        sudoku.printBoard(board)
        print()
        print('----------------------')
testA(board,squareObj,boardD)
