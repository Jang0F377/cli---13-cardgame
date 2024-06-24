from game import Game
from colored import Style, fore

class AI:
  thinking_statement_color = f"{Style.italic}{fore('dark_red_2')}"
  def __init__(self, game: Game) -> None:
    self.game = game
  
  
  def print_thinking(self, player_no: str):
    print()
    print(f"{self.thinking_statement_color}Opponent player no: {player_no} is thinking...{Style.reset}")
    print()
  
  def generate_possible_moves(self):
    moveTree = list()
    
  def analyze_hand(self, players_hand):
    play_single = []
    play_pairs = []
    play_triples = []
    play_straight = []
    play_pairs_of_doubles = []
    play_pairs_of_triples = []
    four_of_a_kind = []
    cop_killer = []
    threes = []
    fours = []
    
    if self.game.turn_state['play_type'] is None and self.game.game_state['turn_number'] is 1:
      # First player to go
      # must play 3 of Diamonds
      for card in players_hand['hand']:
        print(f"CARD: {card}")
        if card['rank'] is '3':
          threes.append(card)
        elif card['rank'] is '4':
          fours.append(card)
          
    print(threes)
    print(fours)
        # if card['comparable_value'] is (3,1):
        #   play_single.append(card) 
        # elif card['comparable_value'] > (3,1) and card['comparable_value'] < (3,4): 
        #   print('greater than and less than')
          
        # elif card['rank'] is '4':
        #   print(4)
        # elif card['comparable_value'] > (3,1) and card['comparable_value'] < (5,1):
          