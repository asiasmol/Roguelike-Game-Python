import random

list_of = []
def create_fox(board):
    return {
        'icon': 'F', 'x':random.randint(1, 10), 'y':random.randint(1, 10),'health':6}

def create_shelter_worker():
    return {
        'icon': 'S', 'x':random.randint(1, 10), 'y':random.randint(1, 10), 'health':10 }
def create_security_guard():
    return {
        'icon': 'G','x':random.randint(1, 10), 'y':random.randint(1, 10),'health':15}

def put_fox_on_board(board, fox):
    board[fox['y']][fox['x']]= fox['icon']

def put_shelter_worker_on_board(board, shelter_worker):
    board[shelter_worker['y']][shelter_worker['x']] = shelter_worker['icon']

def put_security_guard_on_board(board, security_guard):
    board[security_guard['y']][security_guard['x']] = security_guard['icon']

def fight_with_fox():
    print(f'Your fight with the fox begins!')
    round = 1 
    print(f'Round {round} !')

def fight_with_shelter_worker():
    print('Your fight with the shelter worker begins!')
    round = 1 
    print(f'Round {round} !')

def fight_with_security_guard():
    print('Your fight with the security guard begins!')
    round = 1 
    print(f'Round {round} !')



