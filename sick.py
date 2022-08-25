import time

def removal_statistic(player, add_info):
    info = ''
    use_item = []
    for item in player["sickness"]:
        if item not in use_item:
            use_item.append(item)
            if item == "Stomach ache":
                info += "Your tummy hurts !! stamina -2\n"
            if item == "Bleeding":
                info += "You're bleeding !! health -2\n"
            if item == "Addiction":
                info += "You're addicted !! sweetness -2\n"
            if item == "Burn":
                info += "You are burned!! health -1\n"

    sick = {"Stomach ache": 1, "Bleeding": 2, "Addiction": 2, "Burn": 1}
    if "Stomach ache" in player["sickness"]:
        player['stamina'] -= sick["Stomach ache"]
    if "Bleeding" in player["sickness"]:
        player['health'] -= sick["Bleeding"]
    if "Addiction" in player["sickness"]:
        player["sweetness"] -= sick["Addiction"]
    if "Burn" in player["sickness"]:
        player['health'] -= sick["Burn"]

    add_info["add_inf"] = info
    add_info["start"] = time.time()

