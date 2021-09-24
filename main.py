from pprint import pprint as pprint

map = '''
jcp                     j
 |                      |
mt---momst---s---ts---ymh
             |
         c--nk
         |
         a
'''

#Hello
state = {}


def get_command(question):
  answer = input(question).lower().strip()
  return answer.split()

do_intro = False
if do_intro:
  print("Hi am Annabelle")
  print("Annabelle: Whats your name?")
  name = input()
  print("Annabelle: Hi nice to meet you",name)
  print("Annabelle: You've been hired to be a spy. You need to get in and out of this building without seting any alarms off. you are going there because theres a very dengerus weapon, it can be more dangerous then a nuclear bomb... it depends on the size... were not sure when will it blow up ")
  print ("Annabelle: are you ready")
  while True:
    cmd = get_command("<say yes or no> ")
    if cmd[0] in ['yes','ok','sure','yeah','nice']:
      print("Annabelle: Alright lets go!")
      break
    elif cmd[0] in ['no','never','bye','nah']:
      print("Annabelle: WHAT ARE YOU WAITING FOR, GO!!!")
      print("you: ok ok")
      break
    else:
      print("<not a command>")
    
  print ("Annabelle: The weapon is in las vegas street: Fremont Street, somewhere under ground")
  print ("You:  ok lets go")
  print ("GAME:Two days later, you are in the contry and in the city, next you have to find the street,so you look at your phone go to google maps AND THEN YOU RELEASE YOU ARE 30KM AWAY FROM IT AHHHHHHHHHHHHHHHHHHHHHHHH ")




# cmd = get_command("What will you do? <action object> or walk a direction <e w n s>")



items = {}
items['key']= { 'd':'A rusty silver key' }
items['rock']= { 'd':'A small shiny sharp rock' }



places = {}

places['Moes Tavern']={ 'moves':{'e':'momst','n':'john cenas place' },
    'd':"An old fashioned bar with a bartender who looks like a middle aged man in debt.", 'room_items': ['rock'] }

places['momst']={'moves': {'w':'Moes Tavern','e':'subway'},
  'd':"Mom Street is a long street.", 'room_items':[]}

places['subway']={'moves': {'w': 'momst', 'e': 'Toy Shop', 's': 'North Korea'},
  'd':"A dark tunnel under the street level...", 'room_items':[]}

places['Toy Shop']={ 'moves':{'w':'subway', 'e': 'your moms house' }, 
    'd':"A colorful shop filled with toys", 'room_items':[]}


places['your moms house']={ 'moves':{'n':'jupiter', 'w':'toy shop' },
    'd':"what can I say? It's your mom's house ", 'room_items':[]}

places['jupiter']={ 'moves':{'s':'your moms house', },
  'd':"how did we get here? were on jupiter?!", 'room_items':[]}

    
places['john cenas place']={'moves': {'s':'Moes Tavern','e':'subway'}, 'd':"John Cena's Place is awesome", 'room_items':[] }

places ['North Korea']={'moves':{'n':'subway', 
'w':'canada'},
  'd':"North Korea, officially the Democratic People's Republic of Korea, is a country in East Asia, constituting the northern part of the Korea", 'room_items':[]}

places['canada']={'moves': {'s':'america','e':'North Korea',}, 'd':"it's canada what did you think it didint exist?" , 'room_items':[]}

places['america']={'moves': {'n':'canada',}, 'd':"americans are weird they think canada dos'nt exist", 'room_items':[] }

current_place='Moes Tavern'

itemsininv = ['key',]



while True:
  print('Your location: ',current_place)

  # tells you the description of the current place that you're in
  print(places[current_place]['d'])
 
  print(places[current_place]['room_items'])
  
  valid_moves = ', '.join(list(places[current_place]['moves'].keys()))
  print("You can move: ",  valid_moves)

  # get the move and parse it
  move_raw = input("Your move: ").lower().strip()
  move_parts = move_raw.split(' ')
  move = move_parts[0]
  obj = None
  if len( move_parts ) > 1:
    obj = move_parts[1]
  #print("You moved ", move)

  # navigation move?
  if move in ['e','w','s','n']:

    if move not in places[current_place]['moves']:
      print("Cant move there")
      continue
    next_place = places[current_place]['moves'][move]
    current_place=next_place

  elif move in ['inv']:
    print(itemsininv) 

  elif move in ['map']:
    print(map) 

  elif move in ['help']:
    print('''
Commands:

e w n s   Nagivation
inv       Show inventory
map       Show map
quit      Exit the game
    ''')


  elif move in ['quit']:
    exit()

  # TODO: next time!
  elif move in ['pick up',item]:
    exit()

  elif move in ['drop',item]:
    exit()

  else:
    print("Not a real move")
    print("-______-")
    continue

  print()
#print("dis is gonna be an inventory")
