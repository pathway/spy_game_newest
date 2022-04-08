from pprint import pprint as pprint
import json
from pdb import set_trace as st

'''
notes.

'''
## load vars
places = {}
items = {}
craft_items = {}
npcs = {}
entities = {}
with open("data/places.json") as file:
    places = json.load(file)
with open("data/items.json") as file:
    items = json.load(file)
with open("data/craft_items.json") as file:
    craft_items = json.load(file)
with open("data/npcs.json") as file:
    npcs = json.load(file)
with open("data/entities.json") as file:
    entities = json.load(file)

state = {}

#run_mode = "HUMAN"
run_mode="TEST"

scripts = { 
  'win': ['e', 'e', 'n', 'e', 'e', 'e', 'n', 'grab talkin_rattlesnake', 'craft nns', 's', 'w', 'w', 'w', 's', 'w', 'w','secret_place', 'use nns'],
  'spunnge': ['e', 'e', 'n', 'e', 'e', 'e', 'n', 'grab talkin_rattlesnake', 'craft nns', 's', 'w', 'w', 'w', 's', 'w', 'w','secret_place', 'grab spunnge', 'use spunnge'],
  'attack': ['grab rock', 'attack moe rock', 'attack moe rock'], 
  'lose2': ['w',],
  'map': ['e','n','s','e','n','n','s','e','s','n','e','s','n','e','n','s','e','w','s','n'],  # try to visit every room
}
#use_script='win'
#use_script='map'
use_script='attack'

def get_command(question):
    '''
  Ask the user a question
  Return the answer as an array of words, in lower case, with whitespace(spaces or newlines or tabs) before and after removed.
  '''
    answer = input(question).lower().strip()
    return answer.split()

NYC = '''
'''

map = '''
          fc          dv
          |           |
         wp--tx--gs--pb--ts
          |    |  |   |
     lc   |    cm Al  |
     |    |           hd
mt---fs---ph--ap


'''

current_place = 'Moes Tavern'

# items in players inventory
itemsininv = []

plot_moves = {
    'diffused_bomb': 0,
    'room': 0,
    'lion_health': 0,
    'PH': 10,
    'dog': 0,
    'winner': 0,
}

script_index = 0  # keep track of which index we are on in the the script


def intro():
    with open("data/intro.txt") as intro:
        for line in intro:
            print(line)


if run_mode == "HUMAN":
    while True:
        do_intro = input('Want to do the intro? ').lower()
        if do_intro[0] == 'y':
            do_intro = True
            intro()
            break
        else:
            do_intro = False
            break

while True:
    print('Your location: ', current_place)

    # tells you the description of the current place that you're in
    print(places[current_place]['d'])

    room_items = places[current_place]['room_items']
    if room_items:
        print('You see', ', '.join(room_items))
        there_is_items = True
    else:
        there_is_items = False

    room_npcs = None
    if 'room_npcs' in places[current_place]:
        room_npcs = places[current_place]['room_npcs']
    if room_npcs:
        print('Also in this room:', room_npcs)

    valid_moves = ', '.join(list(places[current_place]['moves'].keys()))
    print("You can move: ", valid_moves)


    if run_mode == "TEST":
          # did we run out of script commands? then switch to human mode
        if ( len(scripts[use_script]) <= script_index ):
          run_mode= "HUMAN"
        else:
          move_raw = scripts[use_script][script_index]
          script_index = script_index + 1
          print("TEST move: ", move_raw)

    if run_mode =="HUMAN":
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

        if move not in places[current_place]['moves']:
            print("Cant move there")
            continue
        next_place = places[current_place]['moves'][move]
        current_place = next_place

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
        craft_obj = move_parts[1]

        # use craft_items dictionary
        # craft_items['spear']= ['rock','rope','stick']

        if craft_obj not in craft_items.keys():
            print("That item can not be crafted")
        else:

            got_all_the_items = True

            items_needed = craft_items[craft_obj]
            #['rock','rope','stick']

            # check if you have the items needed to craft it
            for item in items_needed:
                if item not in itemsininv:
                    print('dont have ', item)
                    got_all_the_items = False

            # if you have all the items, remove all ingredients
            if got_all_the_items == True:
                for item in items_needed:
                    if item in itemsininv:
                        itemsininv.remove(item)

                # add the new crafted item into our inventory
                itemsininv.append(craft_obj)
                print('you crafted a ', craft_obj)
            else:
                print("Dont have all the items for that!")

    elif move in ['help']:
        print('''
Commands:

e w n s         Nagivation
inv             Show inventory
map             Show map
quit            Exit the game
grab (item)     pick up items
drop (item)     drop items
talk (name)     talk to npc
craft (item)    craft items
  ''')
#rickroll  rickroll

    elif move in ['quit']:
        exit()

    elif move in ['attack']:
       entity_name = move_parts[1]
       item_name = move_parts[2]
       alive = entities[entity_name][ "life" ]
       hits = entities[entity_name][ "hits" ]
       hw = entities[entity_name][ "HW" ]
       entity_details = entities[ entity_name ]
       entity_damage = entities[entity_name][ "damage" ]
       item_damage = items[item_name][ "damage" ]
       if entity_name in places[current_place]['room_entities']:
          if entities[entity_name]["life"] == 0:
            if hits == 0: print(entity_details["responce"][0])
            if hits == 1: print(entity_details["responce"][1])
            if hits == 2: print(entity_details["responce"][2])
          entity_details["health"] -= item_damage
          entities[entity_name][ "hits" ] += 1
          print(hits)
          if hits >= hw: break
          



    #elif move in ['secret_room']:
    #set [current_place] 'place'

    elif move in ['talk']:
        npc = move_parts[1]
        if npc in places[current_place]['room_npcs']:
            say = npc + " says: " + npcs[npc]
            print(say)

    elif move in ['grab']:
        item = move_parts[1]
        if item in places[current_place]['room_items']:

            # add the item from inventory
            itemsininv.append(item)

            # remove the item to the place
            places[current_place]['room_items'].remove(item)

        else:
            print(item, "is not an item or is not here")
            continue

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


    #elif move in ['intro']:
        do_intro = True

    #
    elif move in ['rick', 'rickroll', 'r', 'rr', 'RR']:
        print('''
We're no strangers to love
You know the rules and so do I
A full commitment's what I'm thinking of
You wouldn't get this from any other guy
I just wanna tell you how I'm feeling
Gotta make you understand
Never gonna give you up
Never gonna let you down
Never gonna run around and desert you
Never gonna make you cry
Never gonna say goodbye
Never gonna tell a lie and hurt you
  ''')

    elif move == "use":
        item = move_parts[1]
        if item == "nns":
            if current_place == "moes hidden room":
                print("Ok you use the nns")
                print("And it stops the bomb!")

                plot_moves['diffused_bomb'] = 1

        pass
        if item == "spear":
            if current_place == "Lion Cage":
              print("you stab the lion")
              print("it doesn't die but is hurt")
              print("your spear is now a damaged_spear")
              print("it claws at you")

              plot_moves['lion_health'] = 1
              plot_moves['health'] = 1
              itemsininv.remove("spear")
              itemsininv.append("damaged_spear")

        pass
        if item == "damaged_spear":
          if current_place == "Lion Cage":
            if plot_moves['lion_health'] == 1:
              print("your spearhead lodged in the lion killing it")
              print("and you take it's teeth")
              print("you see the door of the lion cage open")

              plot_moves['lion_health'] = 2
              itemsininv.append("lion teeth")
            else:
                print("You cant use that here")
        pass
        if item == "spunnge":
              print("you are the stupidest person on earth!")
              print("you killed us all!")
              break


        else:
            print("You cant use that")



    #elif move in ['resipe']:
    #    print(resipe)

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


    # WIN CONDITION
    if plot_moves['diffused_bomb'] == 1:
        # TODO: Write a fancy ending
        print("congratulations you win")
        print("you can keep playing")
        "winner" == 1

    print()
#print("dis is gonna be an inventory")r
