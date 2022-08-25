import random
import items
# Display inventory to console
def display_inventory(inventory):
    inventory_to_print = {}
    for item in inventory:
        if item in inventory_to_print:
            inventory_to_print[item] += 1
        else:
            inventory_to_print[item] = 1
    for k,i in inventory_to_print.items():
        print(k,i)

#Picking items from mobs
def picking_items():
    pass
#Add items to inventory
def adding_items():
    pass
#Adds random items from mob
def loot_mobs(player, inventory, mob):
    mob_loot = {"Fox":1, "Shelter_worker":2, "Security_guard":3, "BOSS":3}

    for _ in range(mob_loot[mob]):
        if random.randint(0,10) > 4:
            if player == "Cat":    
                inventory.append(random.choice(items.conver_dict(items.cat_items)))
            elif player == "Dog":
                inventory.append(random.choice(items.conver_dict(items.dog_items)))
            else:
                inventory.append(random.choice(items.conver_dict(items.Monkey_items)))
