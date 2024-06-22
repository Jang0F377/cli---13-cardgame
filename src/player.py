

class Player:
  players: list
  def __init__(self, number_of_players=4) -> None:
    self.number_of_players = number_of_players
    self.players = list()
    
  def _create_player_object(self, id: int) -> dict:
    new_player = {
      'hand': list(),
      'player_no': id
    }
    return new_player
  
  def initialize_players(self) -> list:
    for player_id in range(self.number_of_players):
      player_to_add = self._create_player_object(player_id)
      self.players.append(player_to_add)
      
    return self.players