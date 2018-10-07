import numpy as np
import random

def averageAboveZero (items):
  """
    Compute the average of an given array only for positive values.

    @type items: list
    @param items: List of positive values

    @rtype: float
    @return: Return the average of the list
  """

  # Don't compute if items isn't an List (array)
  if type(items) is not list:
    return ValueError('Type of items param need to be \'list\' and not ' + str(type(items)))

  average = -1
  sum = 0
  itemsLength = len(items)

  # Don't compute if items is empty
  if itemsLength > 0:
    for item in items:
      if item > 0:
        sum += float(item)
      else:
        # Remove 1 to itemsLength if item isn't an positive value
        itemsLength -= 1
    average = sum / itemsLength
  else:
    return ValueError('Items list must not be empty')

  return average

# Some test for average_above_zero function
average = averageAboveZero([2, 5, 10])
average2 = averageAboveZero([])
average3 = averageAboveZero([-1, 2, 4])
average4 = averageAboveZero('sdfndsjk')

# Print results
print('Average of [2, 5, 10] is : ' + str(average))
print('Average of [] is : ' + str(average2))
print('Average of [-1, 2, 4] is : ' + str(average3))
print('Average of \'sdfndsjk\' is : ' + str(average4))

def maxValue (items):
  """
    Function for found the max value of list

    @type items: list
    @param items: List of values

    @rtype: float
    @return: Return the max value of the list
  """

   # Don't compute if items isn't an List (array)
  if type(items) is not list:
    return ValueError('Type of items param need to be \'list\' and not ' + str(type(items)))

  itemsLength = len(items)
  maxVal = None

  # Find max number in items list
  if itemsLength > 0:
    for item in items:
      number = float(item)
      if maxVal == None or number > maxVal:
        maxVal = number
  else:
    return ValueError('Items list must not be empty')

  return maxVal, 1


# Some test for maxValue function
average = maxValue([2, 5, 10])
average2 = maxValue([])
average3 = maxValue([-1, 2, 4])
average4 = maxValue('sdfndsjk')

# Print results
print('maxValue of [2, 5, 10] is : ' + str(average[1]) + ' and index is : ' + str(average[0]))
print('maxValue of [] is : ' + str(average2))
print('maxValue of [-1, 2, 4] is : ' + str(average3[1]) + ' and index is : ' + str(average3[0]))
print('maxValue of \'sdfndsjk\' is : ' + str(average4))



def reverseTable (items):
  """
    Useless function for reverte an list

    @type items: list
    @param items: List of values to reverte

    @rtype: list
    @return: Return reverted list
  """

  # Don't compute if items isn't an List (array)
  if type(items) is not list:
    return ValueError('Type of items param need to be \'list\' and not ' + str(type(items)))

  return items[::-1]

# Some test for reverseTable function
reverted = reverseTable([2, 5, 10])
reverted2 = reverseTable([2, 'dscjk', [1, 2]])
reverted3 = reverseTable('sdfndsjk')

# Print results
print('reverseTable of [2, 5, 10] is : ' + str(reverted))
print('reverseTable of [2, \'dscjk\', [1, 2]] is : ' + str(reverted2))
print('reverseTable of \'sdfndsjk\' is : ' + str(reverted3))

'''
def roiBbox (inputImage) :
  """
    Function compute the boundary box of an binary image

    @type inputImage: numpy array
    @param inputImage: The binary image

    @rtype: numpy array
    @return: Return boundary box of an binary image
  """

  return False

# Some test for roiBbox function
boundary = roiBbox(np.array([[0, 0, 0], [0, 1, 0], [0, 0, 0]]))

print(boundary)
'''


def randomFillSparse (table, k):
  """
    Function fill k cells at random position with 'X'

    @type table: numpy array
    @param table: The table of chars

    @type k: int
    @param k: Number of cells how need to be fill.

    @rtype: numpy array
    @return: Return the filled array
  """

  if (type(k) is not int):
    return ValueError('Type of k must be \'int\' and not ' + str(type(k)))
  if (type(table) is not np.ndarray):
    return ValueError('Type of k must be \'numpy.ndarray\' and not ' + str(type(table)))

  shape = table.shape

  if (k > shape[0] * shape[1]):
    k = shape[0] * shape[1]
  xMax = shape[1] - 1
  yMax = shape[0] - 1

  while k > 0:
    k -= 1
    x = random.randint(0, xMax)
    y = random.randint(0, yMax)
    if (table[y, x] == 'X'):
      k += 1
    else:
      table[y, x] = 'X'

  return table



# Some test for randomFillSparse function
rand = randomFillSparse(np.array([['', '', ''], ['', '', '']]), 2)
rand2 = randomFillSparse(np.array([['', '', ''], ['', '', '']]), 'dd')
rand3 = randomFillSparse([['', '', ''], ['', '', '']], 2)
rand4 = randomFillSparse(np.array([['', '', ''], ['', '', '']]), 20)

print('randomFillSparse of np[['', '', ''], ['', '', '']], 2 is : ' + str(rand))
print('randomFillSparse of np[['', '', ''], ['', '', '']], \'dd\' is : ' + str(rand2))
print('randomFillSparse of [['', '', ''], ['', '', '']], \'dd\' is : ' + str(rand3))
print('randomFillSparse of np[['', '', ''], ['', '', '']], 20 is : ' + str(rand4))

def removeWhitespace (string):
  """
    Useless function how remove all whitespaces of string

    @type string: numpy str
    @param string: The string with whitespaces

    @rtype: str
    @return: Return the saem string but whitout whitespaces
  """
  if (type(string) is not str):
    return ValueError('Type of string must be \'str\' and not ' + str(type(string)))

  return string.replace(' ', '')

sws = removeWhitespace('dfsve fzeqf  f bzh h h    qsjlj qjdl jQO JJ OIJ J   ALJ EJ')
sws2 = removeWhitespace(561)

print('removeWhitespace of \'dfsve fzeqf  f bzh h h    qsjlj qjdl jQO JJ OIJ J   ALJ EJ\' is : ' + str(sws))
print('removeWhitespace of 561 is : ' + str(sws2))

def shuffle (array):
  """
    Useless function how shuffle an given list

    @type array: list
    @param array: The list how need to be shiffuled

    @rtype: list
    @return: Return the shuffled list
  """
  if (type(array) is not list):
    return ValueError('Type of array must be \'list\' and not ' + str(type(array)))

  random.shuffle(array)
  return array

shuf = shuffle([i for i in range(10)])
shuf2 = shuffle(561)

print('shuffle of ' + str([i for i in range(10)]) + ' is : ' + str(shuf))
print('shuffle of 561 is : ' + str(shuf2))