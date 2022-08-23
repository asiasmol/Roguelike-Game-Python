def ipnut_player():
    kind_player = input("Choose a character: 1-dog, 2-cat, 3-platypus:")
    return kind_player

def create_player(kind_player):
    dog = {"health": 10, "sweetness": 15, "stamina": 10, "sickness": [], "level": 0}
    cat = {"health": 7, "sweetness": 20, "stamina": 15, "sickness": [], "level": 0}
    platypus = {"health": 5, "sweetness": 10, "stamina": 8, "sickness": [], "level": 0}
    
    while True:
        if kind_player == "1":
            return dog
        elif kind_player == '2':
            return cat
        elif kind_player == "3":
            return platypus
        else:
            print("Invalid input!!")

def Position_player():
    return {
        'icon': '@',
        'y': 3,
        'x': 3}