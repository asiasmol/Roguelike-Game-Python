import util
import engine
import ui

PLAYER_ICON = '@'
PLAYER_START_X = 3
PLAYER_START_Y = 3

BOARD_WIDTH = 30
BOARD_HEIGHT = 20

def ipnut_player():
    kind_player = input("Choose a character: 1-dog, 2-cat, 3-platypus:")
    return kind_player

def create_player(kind_player):
    dog = {"health": 10, "sweetness": 15, "stamina": 10, "sickness": [], "level": 0}
    cat = {"health": 7, "sweetness": 20, "stamina": 15, "sickness": [], "level": 0}
    platypus = {"health": 5, "sweetness": 10, "stamina": 8, "sickness": [], "level": 0}
    
    while True:
        if kind_player == "1":
            return dog, {'icon': '@','y': 3,'x': 3}
        elif kind_player == '2':
            return cat
        elif kind_player == "3":
            return platypus
        else:
            print("Invalid input!!")

def main():
    player = create_player()
    board = engine.create_board(BOARD_WIDTH, BOARD_HEIGHT)

    util.clear_screen()
    is_running = True
    while is_running:
        engine.put_player_on_board(board, player)
        ui.display_board(board)

        key = util.key_pressed()
        if key == 'q':
            is_running = False
        else:
            pass
        util.clear_screen()


if __name__ == '__main__':
    main()
