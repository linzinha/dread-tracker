import json

# load the json
f = open("data.json", "r")
data = json.load(f)

# define the json variables
zone = data["zones"]
forest_boss = data["bosses"]["Forest"]
village_boss = data["bosses"]["Village"]
castle_boss = data["bosses"]["Castle"]
boss_item = data["boss items"]
component = data["components"]
boss_banish = data["boss banishes"]
boss_strategy = data["boss strategy"]
boss_item_map = data["boss item map"]

selected_bosses = []
selected_boss_items = []
selected_components_list = []
player_sub_zones = {
    "Cabin": None,
    "Tallest Tree": None,
    "Burrows": None,
    "Village Square": None,
    "Skid Row": None,
    "Old Duke's Estate": None,
    "Tower": None,
    "Great Hall": None,
    "Dungeons": None
}


# select bosses to fight on Hard mode
def select_bosses(zone):
    choice_number = 1
    for option in zone:
        print(f"{choice_number}: {option}")
        choice_number += 1

    choice = int(input()) - 1
    print(zone[choice])
    selected_bosses.append(zone[choice])


select_bosses(forest_boss)
select_bosses(village_boss)
select_bosses(castle_boss)


print(f"selected_bosses: {selected_bosses}")
for boss in selected_bosses:
    selected_boss_items.append(boss_item_map[boss])

print(f"selected_boss_items: {selected_boss_items}")

for item in selected_boss_items:
    selected_components_list.append(boss_item[item])

print(f"selected_components_list: {selected_components_list}")


def one_bosskiller():
    for selected_boss_item in selected_boss_items:
        boss_item_location = component[selected_boss_item]["location"]
        if player_sub_zones[boss_item_location] is None:
            player_sub_zones[boss_item_location] = selected_boss_item
    print(player_sub_zones)
    for component_items in selected_components_list:
        for component_item in component_items:
            component_item_location = component[component_item]["location"]
            if player_sub_zones[component_item_location] is None:
                player_sub_zones[component_item_location] = component_item
            else:
                print(f"Another player needed for {component_item}")
    print(player_sub_zones)
    for selected_boss in selected_bosses:
        location1, location2 = boss_banish[selected_boss]["location"]
        if player_sub_zones[location1] is None:
            player_sub_zones[location1] = f"banish {boss_banish[selected_boss]["banish"]}"
        else:
            print(f"Another player needed to banish {boss_banish[selected_boss]["banish"]} in {location1}")




one_bosskiller()
