#if move in ["e", "w", "s", "n"]:
    
    # * news_inavlid * #
    # if move not in places[current_place]["moves"]:
    #     print("Cant move there")
        ## continue
    # * news * #
    # next_place = places[current_place]["moves"][move]
    # current_place = next_place
# elif move in ["inv"]:
    # * inv * #
#     print("Inventory")
#     print("---------")
#     print(itemsininv)

#elif move in ["recipes"]:
#    print(craft_items)
#    print("---------")
# elif move in ["map"]:
    # * map * #
#     print(map)
# elif move in ["secret_place"]:
    # * current_place_moes_tavern * #
#     #places[current_place] = "place"
#     if current_place == "Moes Tavern":
#         current_place = "moes hidden room"
# elif move in ["craft"]:
#     # * moved to helper function * #
#     craft_obj = move_parts[1]
#     # use craft_items dictionary
#     # craft_items["spear"]= ["rock","rope","stick"]
#     if craft_obj not in craft_items.keys():
#         print("That item can not be crafted")
#     else:
#         got_all_the_items = True
#         items_needed = craft_items[craft_obj]
#         #["rock","rope","stick"]
#         # check if you have the items needed to craft it
#         for item in items_needed:
#             if item not in itemsininv:
#                 print("dont have ", item)
#                 got_all_the_items = False
#         # if you have all the items, remove all ingredients
#         if got_all_the_items == True:
#             for item in items_needed:
#                 if item in itemsininv:
#                     itemsininv.remove(item)
#             # add the new crafted item into our inventory
#             itemsininv.append(craft_obj)
#             print("you crafted a ", craft_obj)
#         else:
#             print("Dont have all the items for that!")
# elif move in ["help"]:
#     # * help * #
#     print("""
# Commands:

# e w n s         Nagivation
# inv             Show inventory
# map             Show map
# quit            Exit the game
# grab (item)     pick up items
# drop (item)     drop items
# talk (name)     talk to npc
# craft (item)    craft items
#     """)
#rickroll    rickroll

# elif move in ["quit"]:
    # * quit * #
#     exit()
# elif move in ["attack"]:
# * moved to helper_attack function * #
    # entity_name = move_parts[1]
    # item_name = move_parts[2]
    # alive = entities[entity_name][ "life" ]
    # hits = entities[entity_name][ "hits" ]
    # hw = entities[entity_name][ "HW" ]
    # entity_details = entities[ entity_name ]
    # entity_damage = entities[entity_name][ "damage" ]
    # item_damage = items[item_name][ "damage" ]
    # if entity_name in places[current_place]["room_entities"]:
    #     if entities[entity_name]["life"] == 0:
    #         if hits == 0: print(entity_details["responce"][0])
    #         if hits == 1: print(entity_details["responce"][1])
    #         if hits == 2: print(entity_details["responce"][2])
    #         entity_details["health"] -= item_damage
    #         entities[entity_name][ "hits" ] += 1
    #         print(hits)
            #if hits >= hw: ## break
        
#elif move in ["secret_room"]:
#set [current_place] "place"
    # elif move in ["talk"]:
    # * talk * #
    #     npc = move_parts[1]
    #     if npc in places[current_place]["room_npcs"]:
    #         say = npc + " says: " + npcs[npc]
    #         print(say)
    # elif move in ["grab"]:
    #     item = move_parts[1]
    #     if item in places[current_place]["room_items"]:
    #         # add the item from inventory
    #         itemsininv.append(item)
    #         # remove the item to the place
    #         places[current_place]["room_items"].remove(item)
    #     else:
    #         print(item, "is not an item or is not here")
    #         ## continue
    # elif move in ["drop"]:
    # * drop * #
        # item = move_parts[1]
        # if item in itemsininv:
        #     # remove the item from inventory
        #     itemsininv.remove(item)
        #     # add the item to the place
        #     places[current_place]["room_items"].append(item)
        # else:
        #     ## continue
        #     print("Not a real move    -______-")
        ## continue
    # elif move in ["look"]:
    # * look * #
    #     item = move_parts[1]
    #     if item in places[current_place]["room_items"] or item in itemsininv:
    #         print(items[item]["d"])
    #     else:
    #         print("you cant see it")
    # #elif move in ["intro"]:
    #     do_intro = True
    #
    # elif move in ["rick", "rickroll", "r", "rr", "RR"]:
    # * rickroll * #
    #     print("""
    # We"re no strangers to love
    # You know the rules and so do I
    # A full commitment"s what I"m thinking of
    # You wouldn"t get this from any other guy
    # I just wanna tell you how I"m feeling
    # Gotta make you understand
    # Never gonna give you up
    # Never gonna let you down
    # Never gonna run around and desert you
    # Never gonna make you cry
    # Never gonna say goodbye
    # Never gonna tell a lie and hurt you
    # """)

    # elif move == "use":
    #     item = move_parts[1]
    #     if item == "nns":
    #         if current_place == "moes hidden room":
    #             print("Ok you use the nns")
    #             print("And it stops the bomb!")
    #             plot_moves["diffused_bomb"] = 1
    
        # * SKIPPED BECAUSE THIS SHOULD BE BATTLE SYSTEM * #
        # pass
        # if item == "spear":
        #     if current_place == "Lion Cage":
        #         print("you stab the lion")
        #         print("it doesn't die but is hurt")
        #         print("your spear is now a damaged_spear")
        #         print("it claws at you")
        #         plot_moves["lion_health"] = 1
        #         plot_moves["health"] = 1
        #         itemsininv.remove("spear")
        #         itemsininv.append("damaged_spear")
        # pass
        # if item == "damaged_spear":
        #     if current_place == "Lion Cage":
        #         if plot_moves["lion_health"] == 1:
        #             print("your spearhead lodged in the lion killing it")
        #             print("and you take its teeth")
        #             print("you see the door of the lion cage open")
        #             plot_moves["lion_health"] = 2
        #             itemsininv.append("lion teeth")
        #         else:
        #             print("You cant use that here")
        # pass
        # if item == "spunnge":
        #         print("you are the stupidest person on earth!")
        #         print("you killed us all!")
        #         ## break
        # else:
        #     print("You cant use that")
    #elif move in ["resipe"]:
    #    print(resipe)
    # else:
    #     print("Not a real move")
    #     print("-______-")
    #     ## continue
    # # """
    # # Special plot moves AFTER the move
    # # """
    # if move == "grab" and obj == "rock":
    # * Added to helper_grab * #
    #     print("Under the rock you found a secretthing!")
    #     itemsininv.append("secretthing")
    # * added to helper_move because specialer cases * #
    # if    move == "e" and current_place == "Luxor Casino" and plot_moves["health"] == 0:
    #     print("you manage to get out")
    #     print("but not without getting scratched")
    #     plot_moves["health"] = 2
    # """
    # for later idc about it rn
    # if move == "talk" and npc == "dog" and current_place == "Allyway" and "dog" == 0:
    #     "dog" == 1
    # """
    # if move == "w" and current_place == "Lion Cage" and plot_moves["health"] == 2:
    #     print("you got eaten by the lion")
    #     ## break
    # if    move == "e" and current_place == "Luxor Casino" and plot_moves["health"] == 1:
    #     print("you just barely manage to get out with your life")
    #     print("you are extreamly close to death")