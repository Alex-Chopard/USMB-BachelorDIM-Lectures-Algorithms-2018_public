from enum import Enum
import random

MAX_SCORES = 100

# Enum for identify types of players
class TypeOfPlayers (Enum):
  PLAYER = 'Player'
  COMPUTER = 'Computer'

def gameIsEnded (scores):
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

def switchPlayer (whoPlay):
  """
    Function for switch the player

    @type whoPlay: TypeOfPlayers
    @param whoPlay: The current player

    @rtype: TypeOfPlayers
    @return: Return the new user who play
  """

  if (whoPlay == TypeOfPlayers.PLAYER):
    whoPlay = TypeOfPlayers.COMPUTER
  else:
    whoPlay = TypeOfPlayers.PLAYER

  return whoPlay

def playerPlayed ():
  """
    Function for manager the real player when he play

    @rtype: int
    @return: Return the scores optain by the player
  """

  tourEnded = False
  currentScore = 0

  while not tourEnded:
    print('Current score : ' + str(currentScore))
    roll = input('Roll the dice ?(y/n)')

    # Check if the player when to roll the dice one more time.
    if (type(roll) is str and (roll == 'y' or roll == 'Y' or roll == 'yes' or roll == 'Yes')):
      dice = random.randint(1, 6)
      print('Result : ' + str(dice))
      # If the player optain 1, then exit the function
      if (dice == 1):
        tourEnded = True
        currentScore = 0
        print('You optained 1, turn has stoped and next')
      else:
        currentScore += dice
    else:
      tourEnded = True

  return currentScore

def diceGame ():
  """
    Function for manage all the game.

    @rtype: None
    @return: Return None when the game is ended
  """
  
  scores = { TypeOfPlayers.PLAYER: 0, TypeOfPlayers.COMPUTER: 0 }
  whoPlay = TypeOfPlayers.COMPUTER

  while not gameIsEnded(scores):
    print('----------------------------------------------------------')
    print('Scores :')
    print('     - You : ' + str(scores[TypeOfPlayers.PLAYER]))
    print('     - Computer : ' + str(scores[TypeOfPlayers.COMPUTER]) + '\n')

    print('How play : ' + str(whoPlay.value))

    if (whoPlay == TypeOfPlayers.PLAYER):
      scores[TypeOfPlayers.PLAYER] += playerPlayed()
    else:
      scores[TypeOfPlayers.COMPUTER] += random.randint(1, 6)

    whoPlay = switchPlayer(whoPlay)

  result = ''
  if (gameIsEnded(scores) and scores[TypeOfPlayers.PLAYER] >= MAX_SCORES):
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
  diceGame()
else:
  print('See you soon ;)')

