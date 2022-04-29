import utils

class GameState:
  def __init__(self):
      
    ## load vars
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


class Actions:
  def __init__(self):
    game_state = GameState()
    game_state.reset()

    