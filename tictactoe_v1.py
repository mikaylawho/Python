#!/usr/bin/env python
#Tic-Tac-Toe 1 - print board

board = [ 'O', 'X', ' ', 'O', ' ', 'X', 'O', 'X', 'X' ]
def printBoard():
    print
    for square in range(0,9):
        print board[square],
        if square == 2 or square == 5 :
            print
    print

if __name__ == '__main__':
    printBoard()
