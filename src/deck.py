from constants import *
from card import Card
import random

class Deck:
  CARD_VALUES = CARD_VALUES
  CARD_SUITS = CARD_SUITS
  cards: list
  
  def __init__(self, card) -> None:
    self.card: Card = card
    self.cards = list()
    
  def build_and_shuffle(self, number_of_shuffles=5):
    self._build_cards()
    self._shuffle_deck(number_of_shuffles)
    return self.cards  
    
    
  def _build_cards(self):
    for suit in self.CARD_SUITS:
      for rank in self.CARD_VALUES:
        created_card = self.card.create_card(
          suit,
          rank,
          self.CARD_SUITS,
          self.CARD_VALUES
        )
        self.cards.append(created_card)
        
  def _shuffle_deck(self, number_of_shuffles):
    for _ in range(number_of_shuffles):
      random.shuffle(self.cards)