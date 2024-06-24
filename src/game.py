from deck import Deck
from player import Player
from scoreboard import Scoreboard
from colored import Style, fore, Back

class Game:
  def __init__(self, deck: Deck, players: Player, scoreboard: Scoreboard) -> None:
    self.deck: list[Deck] = deck.build_and_shuffle()
    self.players_state: list[Player] = players.initialize_players()
    self.discard_pile = list()
    self.history = list()
    self.player_to_start = None
    self.human_player = self.players_state[0]
    self.scoreboard = scoreboard
    self.turn_state = {
      'how_many_cards': None,
      'first_card_value': None,
      'last_card_value': None,
      'play_type': None
    }
    self.game_state = {
      'current_turn_order': list(),
      'turn_number': 0,
      'player_in_power': None,    
    }
    
    
  def print_hand(self):
    print_color = f"{Style.bold}{fore('blue_violet')}{Back.white}"
    hand = self.human_player['hand']
    hand_length = len(hand) + 1
    print(f"{print_color}You are player no: 0{Style.reset}")
    print(f"{print_color}Your hand:{Style.reset}")
    print()
    for card in hand:
      print(f"""{card['display_image']}""", end='\t')
    # Need to print an empty line to get everything in same column
    print()
    print()
    for idx in range(1, hand_length):
      print(f"{idx}", end='\t')
    print()
  
    
  def start_game(self):
    self.initialize_game()
    self.scoreboard.print_current_scoreboard(self.game_state,self.turn_state)
    
    
  def initialize_game(self):
    self.pass_out_cards()
    self.handle_remaining_card()
    self.sort_hands()
    self.determine_turn_order(self.player_to_start)
    self.game_state['turn_number'] = 1
    
    
  def determine_turn_order(self, starting_player):
    if starting_player is None:
      Exception("Starting player is undetermined!")
      
    match starting_player:
      case 0:
        self.game_state['current_turn_order'] = [0, 1, 2, 3]
      case 1:
        self.game_state['current_turn_order'] = [1, 2, 3, 0]
      case 2:
        self.game_state['current_turn_order'] = [2, 3, 0, 1]
      case 3:
        self.game_state['current_turn_order'] = [3, 0, 1, 2]
      case _:
        Exception("Error determining turn order!")
    
    
  def sort_hands(self) -> None:
    """Sorts the hands of each player
    
    This function loops through each player's hand
    and sorts the hand based on the card's 
    comparable_value.
    """
    for player in self.players_state:
      hand = player['hand']
      hand.sort(key=lambda card: card['comparable_value'])
      if hand[0]['comparable_value'] == (3,1):
        self.player_to_start = player['player_no']
  
  
  def pass_out_cards(self) -> None:
    """Pass out the cards to the players
    
    This function loops through the # of cards each player
    should receive and has an inner loop that pops one card
    off the end of the deck per player until each has the correct
    cards_per_player
    """
    cards_per_player = len(self.deck) // len(self.players_state)
    
    for _ in range(cards_per_player):
      for player in self.players_state:
        player['hand'].append(self.deck.pop())
        
  
  def handle_remaining_card(self) -> None:
    """Handles if there are left over cards in the deck
    
    If there are 3 players a card will be left over and this 
    function moves it to the discard pile.
    The deck should always be fully emptied before start.
    """
    remaining_cards = len(self.deck) % len(self.players_state)
    for _ in range(remaining_cards):
      self.discard_pile.append(self.deck.pop())