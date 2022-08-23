import random
import players

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
    if mob == 'fox':
        return{"icon":"F","health": 3, "stamina": 3, "items":['random_item']}
    if mob == 'shelter_worker':
        return{"icon":"S","health": 4, "stamina": 4, "items":['random_item']} 
    if mob == 'security_guard':
        return{"icon":"G","health": 5, "stamina": 5, "items":['random_item']}       

def fight_with_mob(mob, player):
    kill_mob = mob['health']
    player_stamina = player['stamina']
    player_skills = {'Attack':2, 'Increase stamina':1, 'Heal':1}
    print(f'Your fight with the {mob} begins!')
    round = 1 
    while kill_mob >0:
        print(f'Round {round} !')
        if round %2 ==0:
            print('Mob turn')
            player['health'] -= mob['stamina'] * (random.randint(1,10)/10)
            print(f'You have ', player['health'])
        player_choice = input('Choose which skill would you like to use Attack/Increase stamina/Heal: ').capitalize()
        if player_choice in player_skills and player_skills[player_choice] >0:
            if player_choice == 'Attack':
                kill_mob -= player_stamina * (random.randint(1,10)/10)
                print(f'Mob have ', kill_mob)
            if player_choice == 'Heal':
                player['health'] +=1
                print(f'You gained one hp more.')
            if player_choice == 'Increase stamina':
                player_stamina +=1
                print(f'You gained one stamina. ')
        else:
            print('Invalid input')
        round +=1
