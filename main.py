from array import array
from pprint import pprint as pprint
import json
from pdb import set_trace as st

import utils as u

## load vars
places : dict = u.load_data("places")
items : dict = u.load_data("items")
craft_items : dict = u.load_data("craft_items")
npcs : dict = u.load_data("npcs")
entities : dict = u.load_data("entities")
use_items : dict = u.load_data("use_items")

plot_moves : dict = u.load_data("plot_moves")

state = {}

#run_mode = "HUMAN"
run_mode="TEST"

scripts = { 
  'win': ['e', 'e', 'n', 'e', 'e', 'e', 'n', 'grab talkin_rattlesnake', 'craft nns', 's', 'w', 'w', 'w', 's', 'w', 'w','secret_place', 'use nns'],
  'spunnge': ['e', 'e', 'n', 'e', 'e', 'e', 'n', 'grab talkin_rattlesnake', 'craft nns', 's', 'w', 'w', 'w', 's', 'w', 'w','secret_place', 'grab spunnge', 'use spunnge'],
  'attack': ['grab rock', 'attack moe rock', 'attack moe rock'], 
  'airport': ['e','e','e'],
  'lose2': ['w',],
  'map': ['e','n','s','e','n','n','s','e','s','n','e','s','n','e','n','s','e','w','s','n'],  # try to visit every room
=======
"""



}
#use_script='win'
#use_script='map'
#use_script='attack'
use_script='airport'
def get_command(question):

    '''
  Ask the user a question
  Return the answer as an array of words, in lower case, with whitespace(spaces or newlines or tabs) before and after removed.
  '''
    answer = input(question).lower().strip()

    return answer.split()

NYC = '''
    cp
     |
 ts-ap
'''

map = u.load_text("map")

current_place = 'Moes Tavern'

## Keep track of whether or not the loop should break. Set this to True instead of using break in the helper functions
loop_should_break = False

# items in players inventory
itemsininv : array = []

script_index = 0  # keep track of which index we are on in the the script



def intro() -> None:
    intro : str = u.load_text("intro")
    for line in intro:
        print(line)


if run_mode == Run_Mode.HUMAN:
    while True:
        do_intro = input('Want to do the intro? ').lower()
        if do_intro[0].lower() == 'y':
            do_intro = True
            intro()
            break
        else:
            break


# main game loop

## HELPER FUNCTIONS FROM HERE UNTIL LINE 174


## Couldn't put these in their own file because they reference globals too much. @pathway think you can solve this? I think it's just a matter of adding more arguments.

def helper_move(move: str, current_place: str) -> None:
#    if move == "e" and current_place == "Luxor Casino" and plot_moves["health"] == 0:
#        print("you manage to get out")
#        print("but not without getting scratched")
#        plot_moves["health"] = 2
#    if move == "w" and current_place == "Lion Cage" and plot_moves["health"] == 2:
#        print("you got eaten by the lion")
#        ## break
#    if    move == "e" and current_place == "Luxor Casino" and plot_moves["health"] == 1:
#        print("you just barely manage to get out with your life")
#        print("you are extreamly close to death")
#    
    if move not in places[current_place]["moves"]:
        print("Can't move there")
        return
    next_place = places[current_place]["moves"][move]
    current_place = next_place

def helper_craft(craft: str) -> None:
    craft_obj = craft
    # use craft_items dictionary
    # craft_items["spear"]= ["rock","rope","stick"]
    if craft_obj not in craft_items.keys():
        print("That item can not be crafted")
    else:
        got_all_the_items = True
        items_needed = craft_items[craft_obj]
        #["rock","rope","stick"]
        # check if you have the items needed to craft it
        for item in items_needed:
            if item not in itemsininv:
                print("dont have ", item)
                got_all_the_items = False
        # if you have all the items, remove all ingredients
        if got_all_the_items == True:
            for item in items_needed:
                if item in itemsininv:
                    itemsininv.remove(item)
            # add the new crafted item into our inventory
            itemsininv.append(craft_obj)
            print("you crafted a ", craft_obj)
        else:
            print("Dont have all the items for that!")

def helper_talk(npc: str) -> None:
    if npc in places[current_place]["room_npcs"]:
        print(npc + " says: " + npcs[npc])

def helper_attack(entity: str, item: str) -> None:
    entity_name = entity
    item_name = item
    alive = entities[entity_name][ "life" ]
    hits = entities[entity_name][ "hits" ]
    hw = entities[entity_name][ "HW" ]
    entity_details = entities[ entity_name ]
    entity_damage = entities[entity_name][ "damage" ]
    item_damage = items[item_name][ "damage" ]
    if entity_name in places[current_place]["room_entities"]:
        if entities[entity_name]["life"] == 0:
            if hits == 0: print(entity_details["responce"][0])
            if hits == 1: print(entity_details["responce"][1])
            if hits == 2: print(entity_details["responce"][2])
            entity_details["health"] -= item_damage
            entities[entity_name][ "hits" ] += 1
            print(hits)
            if hits >= hw: loop_should_break = True## break

def helper_use(item: str, current_place: str) -> None:
    if item in use_items:
        current_item : dict = use_items[item]
        if current_place in current_item["use_place"]:
            print(current_item["use_place"]["string"])
            exec(current_item["use_place"]["execs"])
        else:
            print("%s does nothing." %item)
    else:
        print("You can't use that")

def helper_grab(item: str) -> None:
    if item == "rock": ## best way to handle special case I'm too tired to be clever anymore.
        print("Under the rock you found a secretthing!")
        itemsininv.append("secretthing")
        return
    if item in places[current_place]["room_items"]:
        itemsininv.append(item)
        places[current_place]["room_items"].remove(item)
    else:
        print(item, "is not an item or is not here")


## END OF HELPER FUNCTIONS

## Main loop

while True:
    print('Your location: ', current_place)

    # tells you the description of the current place that you're in
    print(places[current_place]['d'])


    room_items = places[current_place]['room_items']
    if room_items:
        print("You see", ", ".join(room_items))
        # # removes "there_is_items" variable because it literally only existed in this line. What's the point of a variable if you never use it anywhere else?
        ## DECLARE VARIABLES AS YOU NEED THEM


    room_npcs = None
    if 'room_npcs' in places[current_place]:
        room_npcs = places[current_place]['room_npcs']
    if room_npcs:
        print("Also in this room:", str(room_npcs).replace("[", "").replace("]", "").replace("'", "")) ##replace to get rid of extra stuff

    valid_moves : str = ", ".join(list(places[current_place]["moves"].keys()))
    print("You can move: ", valid_moves)


    if run_mode == "TEST":
          # did we run out of script commands? then switch to human mode
        if ( len(scripts[use_script]) <= script_index ):
          run_mode= "HUMAN"
        else:
          move_raw = scripts[use_script][script_index]
          script_index = script_index + 1
          print("TEST move: ", move_raw)

    if run_mode == "HUMAN":
        move_raw = input("Your move: ").lower().strip()
        print("---")

    # break up the command into parts
    move_parts = move_raw.split(' ')

    # get the verb which is the first part
    move = move_parts[0]

    #print("  # move_raw",move_raw)
    #print("  # move_parts",move_parts)
    #print("  # move",move)

    obj = None
    if len(move_parts) > 1:
        obj = move_parts[1]
    #print("You moved ", move)
    '''
  Special plot moves BEFORE regular moves
  '''

    # navigation move?
    if move in ['e', 'w', 's', 'n']:
        helper_move(move, current_place)

    elif move in ['inv']:
        print("Inventory")
        print("---------")
        print(itemsininv)

    #elif move in ['recipes']:
    #    print(craft_items)
    #    print("---------")

    elif move in ['map']:
        print(map)

    elif move in ['secret_place']:
        #places[current_place] = 'place'
        if current_place == 'Moes Tavern':
          current_place = 'moes hidden room'


    elif move in ['craft']:
        helper_craft(move_parts[1])

    elif move in ['help']:
        print(u.load_text("commands")
#rickroll  rickroll

    elif move in ['quit']:
        exit()

    elif move in ['attack']:
       helper_attack(move_parts[1], move_parts[2])
          
    #elif move in ['secret_room']:
    #set [current_place] 'place'

    elif move in ['talk']:
        helper_talk(move_parts[1])

    elif move in ['grab']:
        helper_grab(move_parts[1])

    elif move in ['drop']:
        item = move_parts[1]
        if item in itemsininv:
            # remove the item from inventory
            itemsininv.remove(item)

            # add the item to the place
            places[current_place]['room_items'].append(item)
        else:
            continue
            print("Not a real move  -______-")
        continue

    elif move in ['look']:
        item = move_parts[1]
        if item in places[current_place]['room_items'] or item in itemsininv:
            print(items[item]['d'])
        else:
            print("you cant see it")


    elif move in ['rick', 'rickroll', 'r', 'rr', 'RR']:
        print(u.load_text("strings/nevergonnagiveyouup"))

    elif move == "use":
        helper_use(move_parts[1])
    else:
        print("Not a real move")
        print("-______-")
        continue

    '''
    Special plot moves AFTER the move
    '''
    if move == 'grab' and obj == 'rock':
        print("Under the rock you found a secretthing!")
        itemsininv.append("secretthing")
    if move == 'e' and current_place == 'The Paris Hotel' and "winner" == 0: print("you can't go there yet") and current_place == 'The Paris hotel'

    if  move == 'e' and current_place == "Luxor Casino" and plot_moves['health'] == 0:
      print("you manage to get out")
      print("but not without getting scratched")

      plot_moves['health'] = 2
    '''
  for later idc about it rn
    if move == 'talk' and npc == 'dog' and current_place == "Allyway" and "dog" == 0:
      "dog" == 1
    '''

    if move == 'w' and current_place == "Lion Cage" and plot_moves['health'] == 2:
      print("you got eaten by the lion")
      break

    if  move == 'e' and current_place == "Luxor Casino" and plot_moves['health'] == 1:
      print("you just barely manage to get out with your life")
      print("you are extreamly close to death")

        print("Invalid move")
    if loop_should_break == True:
        loop_should_break = False
        break

    # WIN CONDITION
    if plot_moves['diffused_bomb'] == 1:
        # TODO: Write a fancy ending
        print("congratulations you win")
        print("you can keep playing")
        "winner" == 1

    print()
#print("dis is gonna be an inventory")r