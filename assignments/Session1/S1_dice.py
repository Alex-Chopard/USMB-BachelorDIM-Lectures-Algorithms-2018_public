from enum import Enum
import random

MAX_SCORES = 100

# Enum for identify types of players
class TypeOfPlayers (Enum):
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

  if (scores[TypeOfPlayers.PLAYER] >= MAX_SCORES or scores[TypeOfPlayers.COMPUTER] >= MAX_SCORES):
    return True
  else:
    return False

def switch_player (who_play):
  """
    Function for switch the player

    @type whoPlay: TypeOfPlayers
    @param whoPlay: The current player

    @rtype: TypeOfPlayers
    @return: Return the new user who play
  """

  if (who_play == TypeOfPlayers.PLAYER):
    who_play = TypeOfPlayers.COMPUTER
  else:
    who_play = TypeOfPlayers.PLAYER

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
  
  scores = { TypeOfPlayers.PLAYER: 0, TypeOfPlayers.COMPUTER: 0 }
  who_play = TypeOfPlayers.COMPUTER

  while not game_is_ended(scores):
    print('----------------------------------------------------------')
    print('Scores :')
    print('     - You : ' + str(scores[TypeOfPlayers.PLAYER]))
    print('     - Computer : ' + str(scores[TypeOfPlayers.COMPUTER]) + '\n')

    print('How play : ' + str(who_play.value))

    if (who_play == TypeOfPlayers.PLAYER):
      scores[TypeOfPlayers.PLAYER] += player_played()
    else:
      scores[TypeOfPlayers.COMPUTER] += random.randint(1, 6)

    who_play = switch_player(who_play)

  result = ''
  if (game_is_ended(scores) and scores[TypeOfPlayers.PLAYER] >= MAX_SCORES):
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

