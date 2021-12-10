from pprint import pprint as pprint
import json

'''
notes

'''


state = {}

run_mode="HUMAN"
#run_mode="TEST"

win = ['e','s','e','grab talkin_rattlesnake','craft nns', 'use nns']


def intro():
  print("The year is 1995, you were a renouned actor. But unfortunately you gambeled all the money you had in a casino, and because of that you couldn't pay back the the massive debt you owed. But it's all going to change...")

  print("_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-")

  print("Present day.")

  print("It's 1997 it's been 2 years since you lost all your money. You wake up at 7:00am, thinking how to get your money back, due to huge press no one is hiring you for movies the only thing you're thinking of is how to get back on your feet.")
  print("-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_")
  print("you go for a walk thinking what to do, the first thing that comes to your mind is to get a new job but who wants to hire you?... you go buy some food, you buy: milk, bread, cheese, butter, soda, and some cookies. you tread back home but suddenly you bump into someone, it's a blond woman with long flowing hair she turned around and hands you a white card, you say what is this and who are you? she responds, it's a job, you interested? you take the card and look at it, the first thing it says is, go to a closed area and read the back... you look confused, and then you go home.")
  print("_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-")

  print("You get home and you look at the card, you go to the bathroom and you close everything the door, windows, you sit on the toilet and you look nervous, you look at the back and it says: a phone number: 702 007 2415... suddenly your phone starts ringing when you pick it up you hear the woman you met say staticly: stop the bomb... stop the spunnge. meet me at the cosino... you flinch, you put on your jacket and you get out of the apartment and you lock it and then youre on your way...")

  print("-_-_-_-_-_-_-_-_-_-_-_-_-_-_-")


if run_mode=="HUMAN":
  while True:
      do_intro = input('Want to do the intro? ').lower()
      if do_intro == 'yes':
          do_intro = True
          intro()
      else:
          do_intro = False
          break


def get_command(question):
    '''
  Ask the user a question
  Return the answer as an array of words, in lower case, with whitespace(spaces or newlines or tabs) before and after removed.
  '''
    answer = input(question).lower().strip()
    return answer.split()



# master dictionary of items
items = {}
###
craft_items = {}
craft_items['spear'] = ['rock', 'rope', 'stick']
craft_items['sheild'] = ['metalplate', 'leather', 'nails']
craft_items['metalplate'] = ['scrap']
craft_items['nns'] = ['talkin_rattlesnake']

# master dictionary of npcs
npcs = {}
npcs['moe'] = "what are youse doing in my bar without buying a drink"
npcs['Creepy_Bob'] = "myy names bob"
npcs['liam'] = "the amongus boss is comming"
npcs['crazy_guy'] = "I did see a talkin' rattlesnake"
npcs['homer_simpson'] = "no beer and no tv make homer go crazy"
npcs['talkin_rattlesnake'] = "They expirimented on me, tortured me because they knew that in my flesh held the key to creating the spoong and my flesh still holds the key to stop it. so I say to you stop the spoong and use my flesh."


map = '''
          fc
          |
          wp--tx
          |
     lc   |   
     |    |   
mt---fs---ph--
     |
     bs


'''
# master dictionary of places
places = {}
with open("data/places.json") as file:
  places = json.load(file)
print(places)

current_place = 'Moes Tavern'

# items in players inventory
itemsininv = [
]

plot_moves = {
  'diffused_bomb':0,
}

script_index=0  # keep track of which index we are on in the the script


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

  room_npcs=None
  if 'room_npcs' in places[current_place]:
    room_npcs = places[current_place]['room_npcs']
  if room_npcs:
    print('Also in this room:', room_npcs)

  valid_moves = ', '.join(list(places[current_place]['moves'].keys()))
  print("You can move: ", valid_moves)

  if run_mode=="HUMAN":
    move_raw = input("Your move: ").lower().strip()
    print("---")
  else:
    move_raw = win[ script_index ]
    script_index = script_index + 1


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

  elif move in ['place']:
    #places[current_place] = 'place'
    current_place= move_parts[1]
    

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

  #elif move in ['secret_room']:
    #set [current_place] 'place'

  elif move in ['talk']:
    npc = move_parts[1]
    if npc in places[current_place] ['room_npcs']:
      say =  npc + " says: " + npcs[ npc ]
      print( say )
      
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
    if item=="nns":
      if current_place=="Moes Tavern":
        print("Ok you use the nns")
        print("And it stops the bomb!")

        plot_moves['diffused_bomb']=1

      else:
        print("You cant use that here")
    else:
      print("You cant use that")
    pass

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


  # WIN CONDITION
  if plot_moves['diffused_bomb'] == 1:
    # TODO: Write a fancy ending
    print("YOU WIN!!!")
    print("GAME OVER")
    break

  print()
#print("dis is gonna be an inventory")r


