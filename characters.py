import random
from time import sleep
import inventory
import items
import util

def create_random_position(board):
    random_y = random.randint(1, len(board)-1)
    random_x = random.randint(1, len(board[0])-1)
    return {'y':random_y, 'x': random_x}

def create_mob(board, mob):
    while True:
        position = create_random_position(board)
        if board[position['y']][position['x']] ==' ':
            mob['y'] = position['y']  
            mob['x'] = position ['x']
            board[mob['y']][mob['x']] = mob['icon']
            return mob

def choose_mob(mob):
    if mob == 'fox' or mob =="F":
        return{"name":"Fox","icon":"F","health": 3, "stamina": 3, "items":['random_item']}
    if mob == 'shelter_worker'or mob =="S":
        return{"name":"Shelter_worker","icon":"S","health": 4, "stamina": 4, "items":['random_item']} 
    if mob == 'security_guard'or mob =="G":
        return{"name":"Security_guard","icon":"G","health": 5, "stamina": 5, "items":['random_item']}       

def fight_with_mob(mob, player):
    kill_mob = mob['health']
    player_stamina = player['stamina']
    player_skills = {'Attack':2, 'Increase stamina':1, 'Heal':1,"Run":0}
    print('Your fight with the ,',mob['name'] ,'begins!')
    round = 1 
    while kill_mob >0 and player_stamina>0:
        util.clear_screen()
        print(f'Round {round} !')
        if round %2 ==0:
            print('Mob turn')
            player['health'] -= mob['stamina'] * (random.randint(1,10)/10)
            print(f'You have ', player['health'])
        player_choice = input('Choose which skill would you like to use \nAttack\nIncrease stamina\nHeal\nRun\n ').capitalize()
        if player_choice in player_skills:
            if player_choice == 'Attack':
                kill_mob -= player_stamina * (random.randint(1,10)/10)
                print(f'Mob have ', kill_mob)
            if player_choice == 'Heal':
                player['health'] +=1
                print(f'You gained one hp more.')
            if player_choice == 'Increase stamina':
                player_stamina +=1
                print(f'You gained one stamina. ')
            if player_choice == 'Run':
                return("Run")
            round +=1
        else:
            print('Invalid input')
    if kill_mob <0:
        print("Nice you kill",mob['name'])
        inventory.loot_mobs(player['name'],player['inventory'],mob['name'])
        items.add_items(player)
        items.heal_player(player)
    elif player["health"] <0:
        print("You lose game sory ")
    else:
        print("Run away you little shit")
    sleep(2)


def put_mob_to_map(board,fox = 2,shelter_worker = 2,security_guard = 2):
    mobs = [fox,shelter_worker,security_guard]
    for mob in ("fox","shelter_worker","security_guard"):
        for _ in mobs:
            create_mob(board,choose_mob(mob))
    
