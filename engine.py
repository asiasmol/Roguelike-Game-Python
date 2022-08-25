

def create_board(width, height):
    return [[" " for i in range(width)] for j in range(height)]


def put_position_player_on_board(board, player):
    board[player['y']][player['x']] = player['icon']
    
    

def remove_position_player_on_board(board, player):
    board[player['y']][player['x']] = ' '

def position_player_is_free(board, player,key):
    mobs = ["G","S","F","B","¶",".","H","i"]
    if key == 'w':
        if board[player['y']-1][player['x']] in mobs:
            return True
        return board[player['y']-1][player['x']] ==' '
    elif key == 's':
        if board[player['y']+1][player['x']] in mobs:
            return True
        return board[player['y']+1][player['x']] ==' '
    elif key == 'a':
        if board[player['y']][player['x']-1] in mobs:
            return True
        return board[player['y']][player['x']-1] ==' '
    elif key == 'd':
        if (board[player['y']][player['x']+1] in mobs):
            return True
        return board[player['y']][player['x']+1] ==' ' 


def create_board_from_file(filename):
    with open(filename, "r", encoding="utf-8") as f:
        board = []
        for line in f:
            board_to_board = []
            for element in line:
                if element !="\n":
                    board_to_board.append(element)
            board.append(board_to_board)
    return board


def move (key,position_player):
    if key == 'w':
        position_player["y"] -= 1
    elif key == 's':
        position_player["y"] += 1
    elif key == 'a':
        position_player["x"] -= 1
    elif key == 'd':
        position_player["x"] += 1
    return position_player
        