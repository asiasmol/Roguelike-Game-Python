import time, traceback
import time

def every(delay, task, player):
    next_time = time.time() + delay
    while True:
        time.sleep(max(0, next_time - time.time()))
        try:
            task(player)
        except Exception:
            traceback.print_exc()
        next_time += (time.time() - next_time) // delay * delay + delay


def removal_statistic(player):
    sick = {"Ból brzucha": 1, "Krwawienie": 2, "Uzależnienie": 2, "Poparzenie": 1}
    if "Ból brzucha" in player["sickness"]:
        player['stamina'] -= sick["Ból brzucha"]
        time.sleep(5)
        print("Boli Cię brzuszek stamina -1")
    if "Krwawienie" in player["sickness"]:
        player['health'] -= sick["Krwawienie"]
        print("Boli Cię brzuszek health -2")
    if "Uzależnienie" in player["sickness"]:
        player["sweetness"] -= sick["Uzależnienie"]
        print("Boli Cię brzuszek sweetness -2")
    if "Poparzenie" in player["sickness"]:
        player['health'] -= sick["Poparzenie"]
        print("Boli Cię brzuszek health -1")

