import gamelogic
import players 
import engine




def main():
    player = players.create_player(players.ipnut_player())
    position_player = players.Position_player("‧̫‧")
    board = engine.create_board_from_file("board.txt")
    gamelogic.play(board,position_player,player)
    




if __name__ == '__main__':
    main()
