import time

def removal_statistic(player, add_info):
    sick = {"Ból brzucha": 1, "Krwawienie": 2, "Uzależnienie": 2, "Poparzenie": 1}
    if "Ból brzucha" in player["sickness"]:
        player['stamina'] -= sick["Ból brzucha"]
        add_info["add_inf"] = "Your tummy hurts !! stamina -2"
        add_info["start"] = time.time()
    if "Krwawienie" in player["sickness"]:
        player['health'] -= sick["Krwawienie"]
        add_info["add_inf"] = "You're bleeding !! health -2"
        add_info["start"] = time.time()
    if "Uzależnienie" in player["sickness"]:
        player["sweetness"] -= sick["Uzależnienie"]
        add_info["add_inf"] = "You're addicted !! sweetness -2"
        add_info["start"] = time.time()
    if "Poparzenie" in player["sickness"]:
        player['health'] -= sick["Poparzenie"]
        add_info["add_inf"] = "You are burned!! health -1"
        add_info["start"] = time.time()

