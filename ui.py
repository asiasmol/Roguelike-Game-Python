import util
import time
import engine

def display_board(board,position,add_info):
    left = 18
    right = 18
    up = 8
    down = 8
    if position['x'] < left:
        left = left-(left-position["x"])
    if position['x']+right > len(board[0]):
        right = len(board[0]) - position["x"]
    if position['y'] < up:
        up = up-(up-position["y"])
    if position['y']+down > len(board):
        down = len(board)-position["y"]

    for width in range(-up,down):
        line = ""
        for height in range(-left,right):
            line += board[position['y']+width][position['x']+height]
        print(line)
    if  "add_inf" in add_info and "start" in add_info and time.time() - add_info["start"] < 5:
        print(add_info["add_inf"])

def choosing_a_board(choice):
    while True:
        util.clear_screen()
        if choice == "1":
            return 1,engine.create_board_from_file("boards/board_1/hiden_board.sty"), engine.create_board_from_file("boards/board_1/board.sty")
        if choice == "2":
            return 2,engine.create_board_from_file("boards/board_2/hiden_board.sty"), engine.create_board_from_file("boards/board_2/board.sty")
        if choice == "3":
            return 3,engine.create_board_from_file("boards/board_3/hiden_board.sty"), engine.create_board_from_file("boards/board_3/board.sty")
