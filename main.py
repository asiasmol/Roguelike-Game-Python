import util
import Menu




def main():
    is_running = True
    while is_running:
        util.clear_screen()
        is_running = Menu.Menu()
    util.clear_screen()


if __name__ == '__main__':
    main()
