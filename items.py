# key = Item name | value = item statistics(Hp,Stamina,Sweet)they can be negative or positive 
from time import sleep
import characters as c
import random

cat_items = {"Blueberry":(2,0,0), "Catnip":(1,2,0),"Swamp herb": (-1,2,0),"Fur oil":(0,1,1),"Bow":(0,0,2),"Treats":(1,1,0), 'Toy':(0,0,1), 'Milk':(1,1,0)}
 
dog_items = {"Bone":(1,1,0), "Sausage":(2,0,0),
"Treats":(1,0,0), "DentaStix":(1,1,1), "Brush":(0,0,2),
"Swamp herb": (-1,2,0)}

Monkey_items = {"Bird eggs":(2,0,0), "Banana":(2,1,0), "Larva":(1,0,0),
"Swamp herb": (-1,2,0), "Fur oil":(0,1,1),"Bow":(0,0,2)}

hiden_item = {"Glass":(-1,-1,0),"Rat poison":(-2,-1,-2),"Soap":(-1,0,0),"Nettle":(-1,0,0), "Toadstool":(-2,-1,0)}

# key = disase name | value = item or action what makes you sick
diseases = {"Toadstool":"Stomach ache","Glass":"Bleeding",
"Swamp herb":"Addiction","Nettle":"Burn"}

# key = medicines name | value = disase name

medicines = {"Digestive medicine":"Stomach ache", "Bandage":"Bleeding",
"Addiction medicine":"Addiction", "Aloe":"Burn"}


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

def add_items(player):
  inventory = chose_inventory(player['name'])
  for item in player['inventory']:
    if item in diseases:
      if diseases[item] not in player["sickness"]:
        player["sickness"].append(diseases[item])
    if item in chose_inventory(player["name"]):
      add_player_statistic(player,inventory,item)

def create_random_position(board):
    random_y = random.randint(1, len(board)-1)
    random_x = random.randint(1, len(board[0])-1)
    return {'y':random_y, 'x': random_x}

def create_hidden_item(board):
  list_of_hidden_items = []
  for _ in range(20):
    hidden_item ={}
    while True:
      position = create_random_position(board)
      if position not in list_of_hidden_items and board [position['y']][position['x']] == ' ':
        hidden_item['y'] = position['y']  
        hidden_item['x'] = position['x']  
        break
    list_of_hidden_items.append(hidden_item)
  return list_of_hidden_items
  

def put_medicines_to_map(board):
    for _ in range(15):
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
      print('You are healed !')

def loot_sickness(player):
  sickness = conver_dict(hiden_item)
  sick = random.choice(sickness)
  if sick in ['Glass', 'Nettle',"Toadstool"]:
    player['inventory'].append(sick)
    player["sickness"].append(diseases[sick])
  add_player_statistic(player,hiden_item,sick,)
  print(f"Oh no, you just stood on {sick}")
  sleep(2)

def add_player_statistic(player,inventory,item):
  player["health"] += inventory[item][0]
  player['sweetness'] += inventory[item][1]
  player['stamina'] += inventory[item][2]
