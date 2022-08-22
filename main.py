from player import create_player
import util
import engine
import ui



BOARD_WIDTH = 20
BOARD_HEIGHT = 20


def player():
    return {
        'icon': '@',
        'y': 3,
        'x': 3}


def main():
    position_player = create_player()
    board = engine.create_board_from_file("board.txt")
    is_running = True
    while is_running:
        engine.put_position_player_on_board(board, position_player)
        ui.display_board(board,position_player)
        engine.remove_position_player_on_board(board, position_player)
        key = util.key_pressed()
        if engine.position_player_is_free(board,position_player,key):
            if key == 'q':
                is_running = False
            elif key == 'w':
                position_player["y"] -= 1
            elif key == 's':
                position_player["y"] += 1
            elif key == 'a':
                position_player["x"] -= 1
            elif key == 'd':
                position_player["x"] += 1
            elif key == 'i':
                print("open inventory")
            else:
                pass
        util.clear_screen()
                


if __name__ == '__main__':
    main()
