from game import Game

class CardPlayParser:
  def __init__(self, game: Game) -> None:
    self.game = game
  
  
  def parse_card_play(self, cards_chosen: str):
    
    if ',' in cards_chosen:
      print(f"Comma detected {cards_chosen}")
      card_arr_idx = cards_chosen.split(',')
      print(card_arr_idx)
      for card in card_arr_idx:
        idx = int(card) - 1
        self.game.human_player['hand'].pop(idx)
        # print(f"{self.game.human_player['hand'][int(card) - 1]}")