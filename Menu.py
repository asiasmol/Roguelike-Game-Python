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
    print("Here are game rules:\n")
    print("""Welcome to the 'Get out of animal shelter' game !
You wake up and you are trapped in the shelter. You can not remember how you got there.
The aim of the game is to either escape from the shelter or to get adopted. 
How to make it happen ? 
Move around the shelter, fight with your enemies, collect powerful items and level up your vitals.
At the end either open doors with collected keys or prepare yourself for the final round to defeat shelter boss.

Hint: There is one hidden room on games' board. Once you find it, you can open shelter doors and immediately set yourself free.

Choose your character and direct your animal with commands of 'w', 'a', 's', 'd' to find your happy ending.
Your adventure begins now ! Good luck !\n""")
    input('Press Enter to continue')
