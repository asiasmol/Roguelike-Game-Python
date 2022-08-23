from operator import le
from turtle import down


def display_board(board,position):
    left = 21
    right = 21
    up = 10
    down = 10
    if position['x'] < 21:
        left = 21-(21-position["x"])
    if position['x']+21 > len(board[0]):
        right = len(board[0]) - position["x"]
    if position['y'] < 10:
        up = 10-(10-position["y"])
    if position['y']+10 > len(board):
        down = len(board)-position["y"]
    
    for width in range(-up,down):
        line = ""
        for height in range(-left,right):
            line += board[position['y']+width][position['x']+height]
        print(line)
