from time import sleep
import util
import engine
import ui
import inventory as inv
import characters
import players
import keys
import test
import items


def play():
    add_info = {}
    player = players.create_player(players.ipnut_player())
    position_player = players.Position_player(player['icon'])
    number_board,board, hiden_board = ui.choosing_a_board()
    items.put_medicines_to_map(hiden_board)
    test.start_thread(player,add_info)
    items_list = items.create_hidden_item(board)
    is_running = True
    check = "no"
    while is_running:
        function_board(hiden_board,board,position_player,check, add_info)
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
            if board[position_player['y']] [position_player['x']] == "H":
                hiden_board = board
            if position_player['y'] == 0:
                util.clear_screen()
                print("congratulation you escepe")
                util.key_pressed()
                return False
        check = check_play(hiden_board,position_player,board,player,items_list,number_board)
        util.clear_screen()


def function_board(hiden_board,board,position_player,check, add_info):
        if check != "Run":
            engine.put_position_player_on_board(hiden_board, position_player)
            engine.put_position_player_on_board(board, position_player)
            ui.display_board(hiden_board,position_player, add_info)
            engine.remove_position_player_on_board(hiden_board, position_player)
            engine.remove_position_player_on_board(board, position_player)
        else:
            ui.display_board(hiden_board,position_player)

def check_play(hiden_board,position_player,board,player,items_list,number_board):
            if hiden_board[position_player['y']] [position_player['x']] == "i":
                items.loot_medicine(player)
            if {"y":position_player['y'],"x": position_player['x']} in items_list:
                items.loot_sickness(player)
                items_list.remove({"y":position_player['y'],"x": position_player['x']})
            if board[position_player['y']] [position_player['x']] in ["¶","."]:
                keys.open_door(number_board,hiden_board,position_player)
                keys.open_door(number_board,board,position_player)
            if board[position_player['y']] [position_player['x']] == "B":
                characters.fight_with_boss(player, characters.choose_mob(board[position_player['y']] [position_player['x']]), board, position_player)
            if board[position_player['y']] [position_player['x']] in ["G","S","F"]:
                return characters.fight_with_mob(characters.choose_mob(board[position_player['y']] [position_player['x']]), player)