import random
import items
# Display inventory to console
def display_inventory(inventory):
    return {k for k in inventory}
#Picking items from mobs
def picking_items():
    pass
#Add items to inventory
def adding_items():
    pass
#Adds random items from mob
def loot_mobs(player, inventory, mob):
    mob_loot = {"Fox":1, "shelter_worker":2, "security_guard":3}
    for _ in range(mob_loot[mob]):
        if player == "Cat":    
            inventory.append(random.choice(items.conver_dict(items.cat_items)))
        elif player == "Dog":
            inventory.append(random.choice(items.dog_items.keys()))
        else:
            inventory.append(random.choice(items.platypus_items.keys()))