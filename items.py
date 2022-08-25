# key = Item name | value = item statistics(Hp,Stamina,Sweet)they can be negative or positive 
from time import sleep
import characters as c
import random

cat_items = {"Jagody":(2,0,0), "Kocimiętka":(1,2,0),
 "Bagienne ziele": (-1,2,0), "Muchomor":(-2,-1,0)
  ,"Olejek do futerka":(0,1,1),
  "Kokardka":(0,0,2)}
 
dog_items = {"Kość":(1,1,0), "Kiełbasa":(2,0,0),
"Chrupki":(1,0,0), "DentaStix":(1,1,1), "Szczotka do sierści":(0,0,2),
"Bagienne ziele": (-1,2,0), "Muchomor":(-2,-1,0)}

Monkey_items = {"Ptasie Jaja":(2,0,0), "Bannan":(2,1,0), "Larwa":(1,0,0),
"Bagienne ziele": (-1,2,0), "Muchomor":(-2,-1,0), "Olejek do futerka":(0,1,1),
  "Kokardka":(0,0,2)}

hiden_item = {"Szkło":(-1,-1,0),"trutka na szczury":(-2,-1,-2),"mydło":(-1,0,0),"Pokrzywa":(-1,0,0)}

# key = disase name | value = item or action what makes you sick
diseases = {"Muchomor":"Ból brzucha","Szkło":"Krwawienie",
"Bagienne ziele":"Uzależnienie","Pokrzywa":"Poparzenie"}

# key = medicines name | value = disase name

medicines = {"Lek na trawienie":"Ból brzucha", "Bandaż":"Krwawienie",
"Plasterek na uzależnienia":"Uzależnienie", "Aloes":"Poparzenie"}


def conver_dict(dictionary):
    return [keys for keys in dictionary.keys()]

def conver_dict_item(dictionary):
    return [choise for keys,choise in dictionary.items()]

def chose_inventory(name):
  if name == "Cat":
    return cat_items
  if name == "Dog":
    return dog_items
  if name == "Monkey":
    return Monkey_items

def add_statistic(player):
  inventory = chose_inventory(player['name'])
  for item in player['inventory']:
    if item in diseases:
      if diseases[item] not in player["sickness"]:
        player["sickness"].append(diseases[item])
    if item in chose_inventory(player["name"]):
      player["health"] += inventory[item][0]
      player['sweetness'] += inventory[item][1]
      player['stamina'] += inventory[item][2]

def create_random_position(board):
    random_y = random.randint(1, len(board)-1)
    random_x = random.randint(1, len(board[0])-1)
    return {'y':random_y, 'x': random_x}

def create_hidden_item(board):
  list_of_hidden_items = []
  for _ in range(10):
    hidden_item ={}
    while True:
      position = create_random_position(board)
      if position not in list_of_hidden_items and board[position['y'][position['x']]] == ' ':
        hidden_item['y'] = position['y']  
        hidden_item['x'] = position['x']  
        break
    list_of_hidden_items.append(hidden_item)
  return list_of_hidden_items
  

def put_medicines_to_map(board):
    for _ in range(10):
        c.create_mob(board,{"icon":"i"})

def loot_medicine(player):
  player['inventory'].append(random.choice(conver_dict(medicines)))
  heal_player(player)

def heal_player(player):
  for item in player['inventory']:
    if item in conver_dict(medicines) and medicines[item] in player["sickness"] :
      for keys,ite in diseases.items():
        if diseases[keys] == medicines[item]:
          player['inventory'].remove(keys)
      player["sickness"].remove(medicines[item])
      player['inventory'].remove(item)
      print('you heal ')
