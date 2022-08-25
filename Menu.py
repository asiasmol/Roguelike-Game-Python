import util
import gamelogic
from time import sleep 

def Menu():
    Choise = input("Menu:\nPlay\nRules\nExit\n").capitalize()
    while True:
        if Choise in ["Play","Rules","Exit"]:
            if Choise == "Play":
                #introduction()
                return gamelogic.get_player()
            elif Choise == "Rules":
                Rules()
                return True
            elif Choise == "Exit":
                return False

def introduction():
    print("Welcome to the 'Get out of animal shelter' game !")
    sleep(1)
    print("You wake up and you are trapped in the shelter. You can not remember how you got there.")
    sleep(1)
    print("The aim of the game is to either escape from the shelter or to get adopted." ) 
    sleep(1)
    print("How to make it happen ? ")
    sleep(1)
    print("Move around the shelter, fight with your enemies, collect powerful items and level up your vitals.")
    sleep(1)
    print("At the end either open doors with collected keys or prepare yourself for the final round to defeat shelter boss.")
    sleep(1)
    print("Hint: There is one hidden room on games' board. Once you find it, you can open shelter doors and immediately set yourself free.\nChoose your character and direct your animal with commands of 'w', 'a', 's', 'd' to find your happy ending.Your adventure begins now ! Good luck !\n")
    input('Press Enter to continue')

def Rules():
    util.clear_screen()
    print("Here are game rules:\n")

