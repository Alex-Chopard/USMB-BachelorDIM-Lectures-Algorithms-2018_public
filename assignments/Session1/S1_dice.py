from enum import Enum
import random

class TypeOfPlayers (Enum):
  PLAYER = 'Player'
  COMPUTER = 'Computer'

def gameIsEnded (scores):
  if (scores[TypeOfPlayers.PLAYER] >= 100 or scores[TypeOfPlayers.COMPUTER] >= 100):
    return True
  else:
    return False

def switchPlayer (whoPlay):
  if (whoPlay == TypeOfPlayers.PLAYER):
    whoPlay = TypeOfPlayers.COMPUTER
  else:
    whoPlay = TypeOfPlayers.PLAYER
  return whoPlay

def playerPlayed ():
  tourEnded = False
  currentScore = 0

  while not tourEnded:
    print('Current score : ' + str(currentScore))
    roll = input('Roll the dice ?(y/n)')
    if (type(roll) is str and (roll == 'y' or roll == 'Y' or roll == 'yes' or roll == 'Yes')):
      dice = random.randint(1, 6)
      print('Result : ' + str(dice))
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
  if (gameIsEnded(scores) and scores[TypeOfPlayers.PLAYER] >= 100):
    result = 'WIN '
  else:
    result = 'LOSE'

  # Print the result of the game
  print('*--------------------------------------------------------*')
  print('\n|                       YOU ' + result + ' !                       |\n')
  print('*--------------------------------------------------------*')
  
  return True

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

