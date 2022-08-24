# key = Item name | value = item statistics(Hp,Stamina,Sweet)they can be negative or positive 


cat_items = {"Muchomor":(-2,-1,0)}#"Jagody":(2,0,0), "Kocimiętka":(1,2,0),
 #"Bagienne ziele": (-1,2,0), "Muchomor":(-2,-1,0)
#  ,"Olejek do futerka":(0,1,1),
 # "Kokardka":(0,0,2)}
 
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
    if item in medicines:
      player["sickness"].remove(medicines[item])
    player["health"] += inventory[item][0]
    player['sweetness'] += inventory[item][1]
    player['stamina'] += inventory[item][2]

    

