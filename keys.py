
def open_door(board,position):
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
