from deck import Deck
from player import Player

class Game:
  def __init__(self, deck, players) -> None:
    self.deck: list[Deck] = deck.build_and_shuffle()
    self.players_state: list[Player] = players.initialize_players()
    self.discard_pile = list()
    self.history = list()
    self.turn_state = {
      'how_many_cards': None,
      'last_card_value': None,
      'play_type': None
    }
    self.game_state = {
      'current_turn_order': list(),
      'turn_number': 0,
      'player_in_power': None,    
    }
    
  def start_game(self):
    self.pass_out_cards()
    print(self.players_state)
    
  def pass_out_cards(self):
    cards_per_player = int(len(self.deck) / len(self.players_state))
    
    for x in range(cards_per_player):
      for player in self.players_state:
        player['hand'].append(self.deck.pop())
        
    