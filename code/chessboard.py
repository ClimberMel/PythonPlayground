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

def chessboard(length):
    row1 = ""
    row2 = ""
    i = 1
    while len(row1) < length:
        if len(row1) % 2 == 0:
            row1 +="1"
        else:
            row1 += "0"
    while len(row2) < length:
        if len(row2) % 2 == 0:
            row2 += "0"
        else:
            row2 += "1"
    while i <= length:
        if i % 2 != 0:
            print(row1)
            i += 1
        else:
            print(row2)
            i += 1

chessboard(9)
