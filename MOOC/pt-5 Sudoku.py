'''
def row_correct(sudoku: list):
    for row_no in range(9):
        rowcheck = []
        for square in sudoku[row_no]:
            if square > 0 and square not in rowcheck:
                rowcheck.append(square)
            elif square in rowcheck:
                return False
    return True

def column_correct(sudoku: list):
    for column_no in range(9):
        colcheck = []
        for row in sudoku:
            if row[column_no] > 0 and row[column_no] not in colcheck:
                colcheck.append(row[column_no])
            elif row[column_no] in colcheck:
                return False
    return True

def block_correct(sudoku: list):
    coordinates = [[0,0],[0,3],[0,6],[3,0],[3,3],[3,6],[6,0],[6,3],[6,6]]
    for pair in coordinates:
        row_no = pair[0]
        column_no = pair[1]
        blockcheck = []
        for row in sudoku[row_no : row_no +3]:
            for square in row[column_no : column_no + 3]:
                if square > 0 and square not in blockcheck:
                    blockcheck.append(square)
                elif square in blockcheck:
                    return False
    return True

def sudoku_grid_correct(sudoku: list):
    if row_correct(sudoku) == True and row_correct(sudoku) == column_correct(sudoku) == block_correct(sudoku):
        return(True)
    return(False)

    '''