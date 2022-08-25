import util
import gamelogic

def Menu():
    Choise = input("Menu:\nPlay\nRules\nExit\n").capitalize()
    if Choise in ["Play","Rules","Exit"]:
        if Choise == "Play":
            gamelogic.play()
        elif Choise == "Rules":
            Rules()
            return True
        elif Choise == "Exit":
            return False


def Rules():
    util.clear_screen()
    print("rules")
    input('Press Enter to continue')
