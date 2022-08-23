from time import sleep
import gamelogic
import players 
import engine
import fontawesome as fa




def main():
    player = players.create_player(players.ipnut_player())
    position_player = players.Position_player(player['icon'])
    board = engine.create_board_from_file("board.sty")
    gamelogic.play(board,position_player)




if __name__ == '__main__':
    main()
