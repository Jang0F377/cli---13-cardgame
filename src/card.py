
class Card:
  def __init__(self) -> None:
    self.unicode_characters = {
      'D': '♦',
      'C': '♣',
      'H': '♥',
      'S': '♠'
    }
  
  def create_card(self, suit, value, card_suits, card_values) -> dict:
    card = dict()
    suit_str = str(card_suits[f'{suit}'])
    value_str = str(card_values[f'{value}'])
    full_name = self._return_full_name(suit_str, value_str)
    comparable_value = self._determine_comparable_value(suit, value)
    display_image = self.create_display_image(suit, value)
    card = {
      "suit": suit,
      "rank": value,
      "suit_str": suit_str,
      "rank_str": value_str,
      "full_name": full_name,
      "comparable_value": comparable_value,
      "display_image": display_image
    }
    return card    
    
  def _return_full_name(self, suit, value) -> str:
    return f"{value} of {suit}"
  
  def create_display_image(self, suit, value):
    suit_img = str(self.unicode_characters[f'{suit}'])
    return value + ' ' + suit_img
    
    
  
  def _determine_comparable_value(self, suit, value) -> tuple[int]:
    suit_value: int
    rank_value: int
    
    if suit == 'D':
      suit_value = 1
    elif suit == 'C':
      suit_value = 2
    elif suit == 'H':
      suit_value = 3
    else:
      suit_value = 4
      
      
    if value == '2':
      rank_value = 15  
    elif value == 'J':
      rank_value = 11
    elif value == 'Q':
      rank_value = 12
    elif value == 'K':
      rank_value = 13
    elif value == 'A':
      rank_value = 14
    else:
      rank_value = int(value)
      
    return (rank_value, suit_value)