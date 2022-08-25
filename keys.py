def key_map_1(board,position):
    if position['y'] == 12 and position['x'] == 89:
        for i in range(3):
            board[49][72+i] = " "
    if position['y'] == 24 and position['x'] == 29:
        for i in range(3):
            board[57][87+i] = " "
    if position['y'] == 41 and position['x'] == 18:
        for i in range(3):
            board[58][87+i] = " "
    if position['y'] == 65 and position['x'] == 83:
        for i in range(3):
            board[63][82+i] = " "
    if position['y'] == 75 and position['x'] == 27:
        for i in range(3):
            board[64][82+i] = " "
    if position['y'] == 99 and position['x'] == 10:
        for i in range(3):
            board[99][55+i] = " "
    if position['y'] == 100 and position['x'] == 82:
        for i in range(3):
            board[116][48+i] = " "
    if position['y'] == 118 and position['x'] == 82:
        for i in range(3):
            board[115][48+i] = " "
    if position['y'] == 4 and position['x'] == 2:
        for i in range(2):
            board[0][18+i] = " "
            board[1][18+i] = " "
    if position['y'] == 52 and position['x'] == 91:
        for i in range(2):
            board[0][18+i] = " "
    if position['y'] == 123 and position['x'] == 86:
        for i in range(2):
            board[1][18+i] = " "

def key_map_2(board,position):
    if position['y'] == 15 and position['x'] == 27:
        for i in range(2):
            board[32][68+i] = " "
    if position['y'] == 39 and position['x'] == 21:
        for i in range(2):
            board[55][74+i] = " "
    if position['y'] == 89 and position['x'] == 86:
        for i in range(2):
            board[105][33+i] = " "
    if position['y'] == 144 and position['x'] == 6:
            board[162][70] = " "
    if position['y'] == 145 and position['x'] == 85:
        for i in range(2):
            board[189][41+1] = " "
    if position['y'] == 45 and position['x'] == 20:
        for i in range(2):
            board[191][41+1] = " "
    if position['y'] == 133 and position['x'] == 74:
            board[1][47] = " "
    if position['y'] == 162 and position['x'] == 85:
            board[0][47] = " "
    if position['y'] == 119 and position['x'] == 77:
            board[133][67] = " "



def key_map_3(board,position):
    pass

def open_door(number_board,board,position):
    if number_board == 1:
        key_map_1(board,position)
    if number_board == 2:
        key_map_2(board,position)
    if number_board == 3:
        key_map_3(board,position)

