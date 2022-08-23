import gamelogic
import players 
import engine




def main():
    position_player = players.Position_player("@")
    board = engine.create_board_from_file("board.txt")
    gamelogic.play(board,position_player)




if __name__ == '__main__':
    main()
