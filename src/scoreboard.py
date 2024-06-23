from colored import Style, fore, Back


class Scoreboard:
  def __init__(self) -> None:
    pass
  
  
  def __print_turn_state(self, turn_state):
    turn_state_key_color = f"{Style.BOLD}{fore('orange_1')}"
    turn_state_title_color = f"{Style.BOLD}{Style.underline}{fore('white')}{Back.BLACK}"
    turn_state_value_color = f"{Style.BOLD}{fore('cyan_1')}"
    print(f"{turn_state_title_color}Turn State:{Style.reset}")
    for key in turn_state:
      print(f"{turn_state_key_color}{key}:  {turn_state_value_color}{turn_state[key]}{Style.reset}", sep='')
    
  def __print_game_state(self, game_state):
    game_state_key_color = f"{Style.BOLD}{fore('plum_1')}"
    game_state_title_color = f"{Style.BOLD}{Style.underline}{fore('white')}{Back.BLACK}"
    game_state_value_color = f"{Style.BOLD}{fore('green_1')}"
    print(f"{game_state_title_color}Game State:{Style.reset}")
    for key in game_state:
      print(f"{game_state_key_color}{key}:  {game_state_value_color}{game_state[key]}{Style.reset}", sep='')

    
  def print_current_scoreboard(self, game_state, turn_state):
    self.__print_game_state(game_state)
    self.__print_turn_state(turn_state)
    print()
    
    