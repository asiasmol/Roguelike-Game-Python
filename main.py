import player 
import util
import engine
import ui
import characters


def main():
    position_player = player.Position_player()
    board = engine.create_board_from_file("board.txt")
    fox = characters.create_fox()
    shelter_worker = characters.create_shelter_worker()
    security_guard = characters.create_security_guard()
    is_running = True
    characters.put_fox_on_board(board, fox)
    characters.put_shelter_worker_on_board(board, shelter_worker)
    characters.put_security_guard_on_board(board, security_guard)
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
        if position_player['x'] == fox['x'] and position_player['y'] == fox['y']:
            characters.fight_with_fox()
        elif position_player['x'] == shelter_worker['x'] and position_player['y'] == shelter_worker['y']:
            characters.fight_with_shelter_worker()
        elif position_player['x'] == security_guard['x'] and position_player['y'] == security_guard['y']:
            characters.fight_with_security_guard()
        else:
            pass


if __name__ == '__main__':
    main()
