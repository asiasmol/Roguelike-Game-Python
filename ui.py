from operator import le
from turtle import down


def display_board(board,position):
    left = 14
    right = 14
    up = 7
    down = 7
    if position['x'] < 14:
        left = 14-(14-position["x"])
    if position['x']+14 > len(board[0]):
        right = len(board[0]) - position["x"]
    if position['y'] < 7:
        up = 7-(7-position["y"])
    if position['y']+7 > len(board):
        down = len(board)-position["y"]
    for width in range(-up,down):
        line = ""
        for height in range(-left,right):
            line += board[position['y']+width][position['x']+height]
        print(line)
