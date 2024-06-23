from card import Card
from deck import Deck
from player import Player
from game import Game
from scoreboard import Scoreboard



def print_command_options() -> None:
  show_possible_plays = 'pp : shows all your possible card plays given the current play type.'
  show_recommended_play = 'rp : shows the recommended play.'
  print_history = 'h : shows the game log of what has happened.'
  resign = 'quit : prematurely end the game.'
  play_cards = '1-4, 13, 10-12, etc. : play your cards'
  options = [
    show_possible_plays,
    show_recommended_play,
    print_history,
    resign,
    play_cards
  ]
  print('\n'.join(options))



def main() -> None:
  scoreboard = Scoreboard()
  card = Card()
  deck = Deck(card)
  players = Player()
  game = Game(deck, players, scoreboard)
  game.start_game()
  # chose_cards(game.human_player['hand'])




if __name__ == '__main__':
  main()