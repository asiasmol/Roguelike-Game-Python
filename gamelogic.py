import util
import engine
import ui
import inventory as inv
import characters


def play(board,position_player,player):
    is_running = True
    characters.create_mob(board, characters.choose_mob('fox'))
    while is_running:
        engine.put_position_player_on_board(board, position_player)
        ui.display_board(board,position_player)
        engine.remove_position_player_on_board(board, position_player)
        key = util.key_pressed()
        if key == 'q':
            is_running = False
        elif key == 'i':
            print(inv.display_inventory(player["inventory"]))
            util.key_pressed()
        if engine.position_player_is_free(board,position_player,key):
            position_player = engine.move(key,position_player)
        util.clear_screen()