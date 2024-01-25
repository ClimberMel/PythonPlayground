"""Please write a function named chessboard, which prints out a chessboard made out of ones and zeroes. 
The function takes an integer argument, which specifies the length of the side of the board. 
See the example below:

chessboard(6)

101010
010101
101010
010101
101010
010101
"""

def chessboard(size):
    i = 0
    while i < size:
        if i % 2 == 0:
            row = "10"*size
        else:
            row = "01"*size
        # Remove extra characters at the end of the row
        print(row[0:size])
        i += 1

chessboard(8)
