from card import Card
from deck import Deck
from player import Player
from game import Game

if __name__ == '__main__':
  card = Card()
  deck = Deck(card)
  players = Player()
  game = Game(deck, players).start_game()