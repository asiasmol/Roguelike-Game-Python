import util
import fontawesome as fa
def ipnut_player():
    util.clear_screen()
    kind_player = input("Choose a character: 1-dog, 2-cat, 3-Monkey:")
    return kind_player

def create_player(kind_player):
    dog = {"name":"Dog","icon":"ࢥ","health": 10, "sweetness": 15, "stamina": 10, "sickness": [],"inventory": [ ]}
    cat = {"name":"Cat","icon":"Დ","health": 7, "sweetness": 20, "stamina": 15, "sickness": [],"inventory": [ ]}
    Monkey = {"name":"Monkey","icon":"ꚗ","health": 5, "sweetness": 10, "stamina": 8, "sickness": [],"inventory": [ ]}
    
    while True:
        if kind_player == "1":
            return dog
        elif kind_player == '2':
            return cat
        elif kind_player == "3":
            return Monkey
        else:
            print("Invalid input!!")
def Position_player(pet):
    return {
        'icon': pet,
        'y': 3,
        'x': 15}

def player_statistic(player):
    for keys,item in player.items():
        if keys not in ["icon",'inventory']:
            print(keys,item)