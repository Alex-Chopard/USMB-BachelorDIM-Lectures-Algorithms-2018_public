from enum import Enum
import random

MAX_SCORES = 100

# Enum for identify types of players
class Type_of_players (Enum):
  PLAYER = 'Player'
  COMPUTER = 'Computer'

def game_is_ended (scores):
  """
    Check if the game is ended with the scores table.

    @type scores: Dict
    @param scores: The Dict of scores of players

    @rtype: boolean
    @return: Return True if a player win the game, or False if no user win.
  """

  if (scores[Type_of_players.PLAYER] >= MAX_SCORES or scores[Type_of_players.COMPUTER] >= MAX_SCORES):
    return True
  else:
    return False

def switch_player (who_play):
  """
    Function for switch the player

    @type whoPlay: Type_of_players
    @param whoPlay: The current player

    @rtype: Type_of_players
    @return: Return the new user who play
  """

  if (who_play == Type_of_players.PLAYER):
    who_play = Type_of_players.COMPUTER
  else:
    who_play = Type_of_players.PLAYER

  return who_play

def player_played ():
  """
    Function for manager the real player when he play

    @rtype: int
    @return: Return the scores optain by the player
  """

  tour_ended = False
  current_score = 0

  while not tour_ended:
    print('Current score : ' + str(current_score))
    roll = input('Roll the dice ?(y/n)')

    # Check if the player when to roll the dice one more time.
    if (type(roll) is str and (roll == 'y' or roll == 'Y' or roll == 'yes' or roll == 'Yes')):
      dice = random.randint(1, 6)
      print('Result : ' + str(dice))
      # If the player optain 1, then exit the function
      if (dice == 1):
        tour_ended = True
        current_score = 0
        print('You optained 1, turn has stoped and next')
      else:
        current_score += dice
    else:
      tour_ended = True

  return current_score

def dice_game ():
  """
    Function for manage all the game.

    @rtype: None
    @return: Return None when the game is ended
  """
  
  scores = { Type_of_players.PLAYER: 0, Type_of_players.COMPUTER: 0 }
  who_play = Type_of_players.COMPUTER

  while not game_is_ended(scores):
    print('----------------------------------------------------------')
    print('Scores :')
    print('     - You : ' + str(scores[Type_of_players.PLAYER]))
    print('     - Computer : ' + str(scores[Type_of_players.COMPUTER]) + '\n')

    print('How play : ' + str(who_play.value))

    if (who_play == Type_of_players.PLAYER):
      scores[Type_of_players.PLAYER] += player_played()
    else:
      scores[Type_of_players.COMPUTER] += random.randint(1, 6)

    who_play = switch_player(who_play)

  result = ''
  if (game_is_ended(scores) and scores[Type_of_players.PLAYER] >= MAX_SCORES):
    result = 'WIN '
  else:
    result = 'LOSE'

  # Print the result of the game
  print('*--------------------------------------------------------*')
  print('\n|                       YOU ' + result + ' !                       |\n')
  print('*--------------------------------------------------------*')
  
  return None

# Start the game
print('*--------------------------------------------------------*')
print('|                                                        |')
print('|              Welcome to the DICE GAME !                |')
print('|                                                        |')
print('*--------------------------------------------------------*')

play = input('\nStart a new Game ? (y/n)\n')

if (type(play) is str and (play == 'y' or play == 'Y' or play == 'yes' or play == 'Yes')):
  dice_game()
else:
  print('See you soon ;)')

