# key = Item name | value = item statistics(Hp,Stamina,Sweet)they can be negative or positive 
cat_items = {"Jagody":(2,0,0), "Kocimiętka":(1,2,0),
 "Bagienne ziele": (-1,2,0), "Muchomor":(-2,-1,0),
  "Pokrzywa":(-1,0,0), "Olejek do futerka":(0,1,1),
  "Kokardka":(0,0,2), "Szkło":(-1,-1,0)}
 
dog_items = {"Kość":(1,1,0), "Kiełbasa":(2,0,0),
"Chrupki":(1,0,0), "DentaStix":(1,1,1), "Szczotka do sierści":(0,0,2),
"Bagienne ziele": (-1,2,0), "Muchomor":(-2,-1,0), "Szkło":(-1,-1,0), "Pokrzywa":(-1,0,0)}

platypus_items = {"Krewetka":(2,0,0), "Rak":(2,1,0), "Larwa":(1,0,0),
"Bagienne ziele": (-1,2,0), "Muchomor":(-2,-1,0), "Olejek do futerka":(0,1,1),
  "Kokardka":(0,0,2),"Szkło":(-1,-1,0), "Pokrzywa":(-1,0,0)}

# key = disase name | value = item or action what makes you sick
diseases = {"Ból brzucha":"Muchomor", "Przeziębienie":"Zimno/Chłód", "Krwawienie":"Szkło",
"Uzależnienie":"3xBagienne ziele", "Poparzenie":"Pokrzywa"}

# key = medicines name | value = disase name

medicines = {"Lek na trawienie":"Ból brzucha", "Syrop":"Przeziębienie", "Bandaż":"Krwawienie",
"Plasterek na uzależnienia":"Uzależnienie", "Aloes":"Poparzenie"}

def conver_dict(dictionary):
    return [keys for keys in dictionary.keys()]
