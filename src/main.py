from card import Card
from deck import Deck
from player import Player
from game import Game
from questionary import checkbox, Choice
from colored import Fore, Style


def chose_cards(players_hand):
  choice_array: list = list()
  for card in players_hand:
    if card['comparable_value'] == (3, 1):
      three_of_diamonds = Choice(card['display_image'], card['comparable_value'], checked=True)
      choice_array.append(three_of_diamonds)
    else:
      choice = Choice(card['display_image'], card['comparable_value'])
      choice_array.append(choice)
  
  chosen_cards = checkbox('Chose what cards to play', choice_array).ask()
  print(chosen_cards)
  

def print_turn_state(turn_state):
  turn_state_color = f"{Style.BOLD}{Fore.GREEN}"
  turn_state_info = f"""Turn State: 
  How many cards:  {turn_state['how_many_cards']}
  First card played:  {turn_state['first_card_value']}
  Last card played: {turn_state['last_card_value']}
  Play type: {turn_state['play_type']}
  """
  print(f"{turn_state_color}{turn_state_info}{Style.reset}")
  
def print_game_state(game_state):
  game_state_color = f"{Style.BOLD}{Fore.BLUE}"
  game_state_info = f"""Game State:
  Current turn order: {game_state['current_turn_order']}
  Turn number:  {game_state['turn_number']}
  Player in power:  {game_state['player_in_power']}
  """
  print(f"{game_state_color}{game_state_info}{Style.reset}")
  
def print_current_game_info(turn_state, game_state):
  print_game_state(game_state)
  print_turn_state(turn_state)
  

def main() -> None:
  card = Card()
  deck = Deck(card)
  players = Player()
  game = Game(deck, players)
  game.start_game()
  print_current_game_info(game.turn_state, game.game_state)
  # chose_cards(game.human_player['hand'])




if __name__ == '__main__':
  main()