import time

def removal_statistic(player, add_info):
    sick = {"Stomach ache": 1, "Bleeding": 2, "Addiction": 2, "Burn": 1}
    if "Stomach ache" in player["sickness"]:
        player['stamina'] -= sick["Stomach ache"]
        add_info["add_inf"] = "Your tummy hurts !! stamina -2"
        add_info["start"] = time.time()
    if "Bleeding" in player["sickness"]:
        player['health'] -= sick["Bleeding"]
        add_info["add_inf"] = "You're bleeding !! health -2"
        add_info["start"] = time.time()
    if "Addiction" in player["sickness"]:
        player["sweetness"] -= sick["Addiction"]
        add_info["add_inf"] = "You're addicted !! sweetness -2"
        add_info["start"] = time.time()
    if "Burn" in player["sickness"]:
        player['health'] -= sick["Burn"]
        add_info["add_inf"] = "You are burned!! health -1"
        add_info["start"] = time.time()

