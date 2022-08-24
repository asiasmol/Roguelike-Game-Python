import util
import engine
import ui
import inventory as inv
import characters
import players


def play():
    player = players.create_player(players.ipnut_player())
    position_player = players.Position_player(player['icon'])
    board = engine.create_board_from_file("board.sty")
    is_running = True
    characters.put_mob_to_map(board)
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
        elif key == 'p':
            players.player_statistic(player)
            util.key_pressed()
        if engine.position_player_is_free(board,position_player,key):
            position_player = engine.move(key,position_player)
            if board[position_player['y']] [position_player['x']] in ["G","S","F"]:
                characters.fight_with_mob(characters.choose_mob(board[position_player['y']] [position_player['x']]),player)
        util.clear_screen()