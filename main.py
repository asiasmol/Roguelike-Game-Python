import util
import engine
import ui
import characters

# PLAYER_ICON = '@'
# PLAYER_START_X = 3
# PLAYER_START_Y = 3

BOARD_WIDTH = 30
BOARD_HEIGHT = 20


def create_player():
    '''
    Creates a 'player' dictionary for storing all player related informations - i.e. player icon, player position.
    Fell free to extend this dictionary!

    Returns:
    dictionary
    '''
    return {
        'icon': '@',
        'y': 3,
        'x': 3}

def main():
    player = create_player()
    board = engine.create_board(BOARD_WIDTH, BOARD_HEIGHT)
    fox = characters.create_fox()
    shelter_worker = characters.create_shelter_worker()
    security_guard = characters.create_security_guard()

    util.clear_screen()
    is_running = True
    characters.put_fox_on_board(board, fox)
    characters.put_shelter_worker_on_board(board, shelter_worker)
    characters.put_security_guard_on_board(board, security_guard)
    while is_running:
        engine.put_player_on_board(board, player)
        ui.display_board(board)
        engine.remove_player_from_board(board, player)
        key = util.key_pressed()
        if key == 'q':
            is_running = False
        elif key =='w':
            player['y']-=1
        elif key =='s':
            player['y']+=1
        elif key =='a':
            player['x']-=1
        elif key =='d':
            player['x']+=1
        else:
            pass
        util.clear_screen()
        if player['x'] == fox['x'] and player['y'] == fox['y']:
            characters.fight_with_fox()
        elif player['x'] == shelter_worker['x'] and player['y'] == shelter_worker['y']:
            characters.fight_with_shelter_worker()
        elif player['x'] == security_guard['x'] and player['y'] == security_guard['y']:
            characters.fight_with_security_guard()
        else:
            pass


if __name__ == '__main__':
    main()
