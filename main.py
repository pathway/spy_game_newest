from pprint import pprint as pp
import json
from pdb import set_trace as st
import utils
#import actions

'''
notes.

'''


class GameState:

  def __init__(self):
    self.places = {}
    self.items = {}
    self.craft_items = {}
    self.npcs = {}
    self.entities = {}
    self.state = {}
    self.current_place = 'Moes Tavern'

    self.plot_moves = {
      'diffused_bomb': 0,
      'room': 0,
      'lion_health': 0,
      'PH': 10,
      'dog': 0,
      'winner': 0,
      'shuddup': 0,
    }

    # items in players inventory
    self.itemsininv = []

  def reset(self):
    self.places = utils.load_json("places")
    self.items = utils.load_json("items")
    self.craft_items = utils.load_json("craft_items")
    self.npcs = utils.load_json("npcs")
    self.entities = utils.load_json("entities")

  def load(self, location):
    # load a saved game
    pass

  def save(self, location):
    # saved game
    pass



gs = GameState()
gs.reset()
game_state=gs
pp(gs)
#exit(0)


script_index = 0  # keep track of which index we are on in the the script




#run_mode = "HUMAN"
run_mode="TEST"

scripts = { 
  'win': ['e', 'e', 'n', 'e', 'e', 'e', 'n', 'grab talkin_rattlesnake', 'craft nns', 's', 'w', 'w', 'w', 's', 'w', 'w','secret_place', 'use nns'],
  'spunnge': ['e', 'e', 'n', 'e', 'e', 'e', 'n', 'grab talkin_rattlesnake', 'craft nns', 's', 'w', 'w', 'w', 's', 'w', 'w','secret_place', 'grab spunnge', 'use spunnge'],
  'airport': ['e', 'e', 'e'],
  'attack': ['grab rock', 'attack moe rock', 'attack moe rock'], 
  'lose2': ['w',],
  'map': ['e','n','s','e','n','n','s','e','s','n','e','s','n','e','n','s','e','w','s','n'],  # try to visit every room
}
#use_script='win'
#use_script='map'
use_script='attack'
#use_script='airport'

def get_command(question):
    '''
  Ask the user a question
  Return the answer as an array of words, in lower case, with whitespace(spaces or newlines or tabs) before and after removed.
  '''
    answer = input(question).lower().strip()
    return answer.split()

NYC = '''
      

  ts-tx-ap
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



def intro():
    print(utils.load_text("intro"))
    pass


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

    #game_step( game_state, )
  
    # --- Get the observation

    print('Your location: ', game_state.current_place)

    # tells you the description of the current place that you're in
    print(game_state.places[game_state.current_place]['d'])

    room_items = game_state.places[game_state.current_place]['room_items']
    if room_items:
        print('You see', ', '.join(room_items))
        there_is_items = True
    else:
        there_is_items = False

    room_npcs = None
    if 'room_npcs' in game_state.places[game_state.current_place]:
        room_npcs = game_state.places[game_state.current_place]['room_npcs']
    if room_npcs:
        print('Also in this room:', room_npcs)

    # --- Determine valid moves
  
    valid_moves = ', '.join(list(game_state.places[game_state.current_place]['moves'].keys()))
    print("You can move: ", valid_moves)


    # --- Enter the move

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

      
    # --- Process the move
      
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
    if move == 'e' and game_state.current_place == 'The Paris Hotel' and "winner" == 0: print("you can't go there") and game_state.current_place == 'The Paris Hotel'
    # navigation move?
    if move in ['e', 'w', 's', 'n']:

        if move not in game_state.places[game_state.current_place]['moves']:
            print("Cant move there")
            continue
        next_place = game_state.places[game_state.current_place]['moves'][move]
        game_state.current_place = next_place

    elif move in ['inv']:
        print("Inventory")
        print("---------")
        print(game_state.itemsininv)

    #elif move in ['recipes']:
    #    print(craft_items)
    #    print("---------")

    elif move in ['map']:
        print(map)

    elif move in ['secret_place']:
        #game_state.places[game_state.current_place] = 'place'
        if game_state.current_place == 'Moes Tavern':
          game_state.current_place = 'moes hidden room'


    elif move in ['craft']:
        craft_obj = move_parts[1]

        # use craft_items dictionary
        # craft_items['spear']= ['rock','rope','stick']

        if craft_obj not in game_state.craft_items.keys():
            print("That item can not be crafted")
        else:

            got_all_the_items = True

            items_needed = game_state.craft_items[craft_obj]
            #['rock','rope','stick']

            # check if you have the items needed to craft it
            for item in items_needed:
                if item not in game_state.itemsininv:
                    print('dont have ', item)
                    got_all_the_items = False

            # if you have all the items, remove all ingredients
            if got_all_the_items == True:
                for item in items_needed:
                    if item in game_state.itemsininv:
                        game_state.itemsininv.remove(item)

                # add the new crafted item into our inventory
                game_state.itemsininv.append(craft_obj)
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
      

    elif move in ['NYC']:
      if game_state.current_place == "LV Airport":
        game_state.current_place == "NYC Airport"
        

    elif move in ['attack']:
       entity_name = move_parts[1]
       item_name = move_parts[2]
       alive = game_state.entities[entity_name][ "life" ]
       hits = game_state.entities[entity_name][ "hits" ]
       hw = game_state.entities[entity_name][ "HW" ]
       entity_details = game_state.entities[ entity_name ]
       entity_damage = game_state.entities[entity_name][ "damage" ]
       item_damage = game_state.items[item_name][ "damage" ]
       if entity_name in game_state.places[game_state.current_place]['room_entities']:
          if game_state.entities[entity_name]["life"] == 0:
            if hits == 0: print(entity_details["responce"][0])
            if hits == 1: print(entity_details["responce"][1])
            if hits == 2: print(entity_details["responce"][2])
          entity_details["health"] -= item_damage
          game_state.entities[entity_name][ "hits" ] += 1
          
          if hits >= hw:
            game_state.plot_moves['PH'] -= game_state.entities[entity_name]["damage"]
          print (game_state.plot_moves['PH'])
          



    #elif move in ['secret_room']:
    #set [game_state.current_place] 'place'

    elif move in ['talk']:
        npc = move_parts[1]
        if npc in game_state.places[game_state.current_place]['room_npcs']:
            say = npc + " says: " + game_state.npcs[npc]
            print(say)

    elif move in ['grab']:
        item = move_parts[1]
        if item in game_state.places[game_state.current_place]['room_items']:

            # add the item from inventory
            game_state.itemsininv.append(item)

            # remove the item to the place
            game_state.places[game_state.current_place]['room_items'].remove(item)

        else:
            print(item, "is not an item or is not here")
            continue

    elif move in ['drop']:
        item = move_parts[1]
        if item in game_state.itemsininv:
            # remove the item from inventory
            game_state.itemsininv.remove(item)

            # add the item to the place
            game_state.places[game_state.current_place]['room_items'].append(item)
        else:
            continue
            print("Not a real move  -______-")
        continue

    elif move in ['look']:
        item = move_parts[1]
        if item in game_state.places[game_state.current_place]['room_items'] or item in game_state.itemsininv:
            print(game_state.items[item]['d'])
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
            if game_state.current_place == "moes hidden room":
                print("Ok you use the nns")
                print("And it stops the bomb!")

                game_state.plot_moves['diffused_bomb'] = 1

            else:
                print("You cant use that here")
        pass
        if item == "spunnge":
              print("you are the dumbest person ever on earth!")
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
        game_state.itemsininv.append("secretthing")
    if game_state.plot_moves['PH'] <= 0: 
      print("you died")
      break

    # WIN CONDITION
    if game_state.plot_moves['diffused_bomb'] == 1 and "shuddup" == 0:
        # TODO: Write a fancy ending
        print("congratulations you win")
        print("you can keep playing")
        "winner" == 1
        "shuddup" == 1

    print()
#print("dis is gonna be an inventory")r
'''hi
'''