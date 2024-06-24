from card import Card
from deck import Deck
from player import Player
from game import Game
from ai import AI
from scoreboard import Scoreboard
from colored import Style, fore, Back
from card_play_parser import CardPlayParser
from sys import exit


def print_command_options() -> None:
  show_options_color = f"{Style.BOLD}{fore('deep_sky_blue_1')}"
  show_possible_plays = 'pp : shows all your possible card plays given the current play type.'
  show_recommended_play = 'rp : shows the recommended play.'
  print_history = 'h : shows the game log of what has happened.'
  resign = 'quit : prematurely end the game.'
  play_cards = '1,2,3,4/8,11,12/1,3,4/etc. : play your cards'
  options = [
    show_possible_plays,
    show_recommended_play,
    print_history,
    resign,
    play_cards
  ]
  print(f"{show_options_color}{'\n'.join(options)}{Style.reset}")
  
  
def start_game(game: Game) -> None:
  ai_opponent = AI(game)
  parser = CardPlayParser(game)
  game.start_game()
  while True:
    for player in game.game_state['current_turn_order']:
      if player == 0:
        game.print_hand()
        command = input("It's your turn. Chose which cards you wish to play.\nUse comma-seperated values: 1,2,3/1,2,4,5,7/etc.\nType '?' for options:  ")
        if command.lower() == 'pp':
            continue
            # TODO: Add functionality to show all possible plays
        elif command.lower() == 'rp':
            continue
          # TODO:  Add functionality to give recommended play
        elif command.lower() == 'h':
            continue
          # TODO: Add functionality to track and view game history
        elif command.lower() == 'quit':
            exit()
        elif command.lower() == '?':
            print_command_options()
            continue
        else:
          try:
            parser.parse_card_play(command)
          except ValueError as error:
            print(f"{error}")
            continue
      else:
        ai_opponent.print_thinking(player)
        ai_opponent.analyze_hand(game.players_state[int(player)])



def main() -> None:
  scoreboard = Scoreboard()
  card = Card()
  deck = Deck(card)
  players = Player()
  game = Game(deck, players, scoreboard)
  start_game(game)
  # chose_cards(game.human_player['hand'])




if __name__ == '__main__':
  main()