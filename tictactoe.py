#!/usr/bin/env python
#Tic-Tac-Toe 3 - check for winner (page 53-54)
#edit to check GitHub

board = [ 'O', 'X', ' ', 'O', ' ', 'X', 'O', 'X', 'X' ]
wins = [[0,1,2],[3,4,5],[6,7,8],[0,3,6],[1,4,7],[2,5,8],[0,4,8],[2,4,6]]
def printBoard():
    print
    print '|', #the comma cancels the 'new line' after the print
    for square in range(0,9):
        print board[square],'|',
        #print square, '|',
        if square == 2 or square == 5 :
            print
            print '--------------'
            print '|',

def checkWin(player):
    win = False
    for test in wins :
        print test
        count = 0
        #iterate though each test case
        #see if there are 3 X's or 3 O's in any of them
        for squares in test :
            if board[squares] == player :
                count += 1
        if count == 3 :
            win = True
    return win


    
if __name__ == '__main__':
    printBoard()

    print
    print
    
    print 'checking board for X'
    if checkWin('X'):
        print 'Game over X wins'
    print 'checking board for O'
    if checkWin('O'):
        print 'Game over O wins'
    



