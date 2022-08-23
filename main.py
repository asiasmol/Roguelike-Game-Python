import player 
import util
import engine
import ui


def main():
    position_player = player.Position_player()
    board = engine.create_board_from_file("board.txt")
    is_running = True
    while is_running:
        engine.put_position_player_on_board(board, position_player)
        ui.display_board(board,position_player)
        engine.remove_position_player_on_board(board, position_player)
        key = util.key_pressed()
        if key == 'q':
            is_running = False
        elif key == 'i':
            print("open inventory")
        if engine.position_player_is_free(board,position_player,key):
            position_player = engine.move(key,position_player)
        util.clear_screen()
                


if __name__ == '__main__':
    main()
