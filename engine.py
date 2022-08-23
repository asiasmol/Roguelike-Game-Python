def create_board(width, height):
    '''
    Creates a new game board based on input parameters.

    Args:
    int: The width of the board
    int: The height of the board

    Returns:
    list: Game board
    '''
    return [[' ' for x in range(width)] for y in range(height)]


def put_player_on_board(board, player):
    '''
    Modifies the game board by placing the player icon at its coordinates.

    Args:
    list: The game board
    dictionary: The player information containing the icon and coordinates

    Returns:
    Nothing
    '''
    board[player['y']][player['x']] = player['icon']


def remove_player_from_board(board, player):
    board[player['y']][player['x']] = ' '
    