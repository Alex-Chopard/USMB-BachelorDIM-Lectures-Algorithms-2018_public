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

def sortSelective (array):
  """
    Function how sort the given array

    b) no only the length of the array
    c) 21
    d) 5
    e) 13
    f) yes
    g)
      50  - p = 41  c = 125
      100 - p = 89  c = 281
      500 - p = 457 c = 1422
    

    @type array: list
    @param array: The list how need to be sorted

    @rtype: list
    @return: Return the sorted list
  """
  if (type(array) is not list):
    return ValueError('Type of array must be \'list\' and not ' + str(type(array)))
  
  n = len(array)
  it = 0
  p = 0
  c = 0

  for j in range(n - 1):
    iMin = j
    for i in range(j + 1, n):
      it += 1
      if (array[i] < array[iMin]):
        iMin = i
        c += 1
    
    if (iMin != j):
      #swape value
      tmp = array[j]
      array[j] = array[iMin]
      array[iMin] = tmp
      p += 1
      c += 1

  print(it)
  print(p)
  print(c)
  return array

def sortBubble (array):
  """
    Function how sort the given array

    b) yes
    c) 24
    d) 13
    e) 13
    f) no
    g)
      50  - p = 563   c = 563 
      100 - p = 2173  c = 2173
      500 - p = 54587 c = 54587

    @type array: list
    @param array: The list how need to be sorted

    @rtype: list
    @return: Return the sorted list
  """
  if (type(array) is not list):
    return ValueError('Type of array must be \'list\' and not ' + str(type(array)))

  n = len(array)
  swapped = True
  it = 0
  p = 0
  c = 0

  while swapped:
    swapped = False

    for i in range(n - 1):
      it += 1
      if array[i] > array[i + 1]:
        #swape value
        tmp = array[i]
        array[i] = array[i + 1]
        array[i + 1] = tmp
        swapped = True
        c += 1
        p += 1
  
  print(it)
  print(p)
  print(c)
  return array

array = [10, 15, 7, 1, 3, 3, 9]
array2 = [10, 15, 7, 1, 3, 3, 9]

print('[sortBubble] Sorted table = ' + str(sortBubble(array)))

print('[sortSelective] Sorted table = ' + str(sortSelective(array2)))

'''
print('-------------------------------------')
a = [3, 9, 1, 8, 1, 6, 5, 2, 6, 5, 5, 5, 6, 8, 4, 9, 1, 9, 2, 8, 6, 4, 0, 7, 7, 2, 9, 9, 0, 8, 2, 4, 3, 5, 1, 7, 2, 9, 3, 1, 3, 0, 0, 7, 4, 6, 8, 9, 5, 8]
b = [4, 5, 1, 2, 1, 5, 9, 8, 0, 2, 8, 9, 1, 7, 6, 4, 2, 1, 7, 2, 3, 5, 1, 7, 1, 6, 2, 4, 7, 5, 6, 1, 3, 9, 3, 4, 6, 2, 2, 0, 3, 4, 7, 2, 2, 3, 1, 9, 8, 2, 8, 6, 3, 1, 1, 6, 4, 8, 8, 9, 4, 9, 0,6, 5, 2, 5, 0, 1, 6, 0, 2, 3, 6, 3, 9, 9, 4, 9, 2, 3, 1, 0, 0, 3, 9, 1, 6, 8, 7, 3, 3, 4, 4, 3, 3, 7, 8, 1, 6]
c = [5, 5, 2, 4, 0, 0, 9, 1, 1, 9, 0, 9, 6, 3, 3, 5, 0, 2, 5, 5, 4, 9, 6, 3, 7, 0, 1, 1, 6, 3, 2, 1, 3, 7, 7, 0, 0, 2, 1, 2, 7, 2, 5, 4, 4, 3, 7, 4, 7, 8, 2, 0, 4, 7, 8, 2, 5, 1, 5, 2, 2, 5, 5,5, 8, 3, 7, 3, 2, 3, 8, 7, 2, 2, 1, 7, 0, 8, 7, 8, 9, 9, 7, 2, 5, 4, 1, 3, 9, 8, 0, 4, 6, 7, 3, 1, 6, 1, 1, 3, 5, 9, 5, 4, 8, 7, 5, 9, 6, 7, 6, 2, 2, 3, 5, 3, 2, 2, 0, 9, 9, 5, 9, 1, 2, 1, 7, 8, 3, 1, 7, 7, 5, 0, 0, 1, 9, 8, 0, 4, 3, 2, 5, 2, 5, 4, 4, 9, 9, 7, 5, 3, 4, 9, 3, 1, 0, 3,6, 5, 0, 5, 7, 6, 9, 8, 5, 1, 0, 3, 9, 2, 6, 7, 3, 9, 3, 4, 2, 6, 5, 5, 1, 7, 7, 6, 7, 5, 4, 8, 5, 4, 3, 6, 5, 9, 1, 2, 8, 0, 6, 7, 2, 4, 8, 8, 8, 0, 4, 9, 1, 4, 0, 3, 7, 1, 3, 7, 1, 5, 6, 1, 9, 5, 8, 4, 6, 8, 8, 2, 6, 1, 6, 9, 9, 8, 8, 1, 7, 3, 6, 4, 3, 3, 8, 1, 8, 8, 1, 5, 3, 2, 8,5, 0, 7, 5, 4, 2, 5, 7, 0, 1, 3, 6, 2, 7, 2, 0, 3, 9, 1, 0, 4, 5, 8, 2, 4, 3, 1, 6, 4, 2, 8, 3, 5, 5, 2, 1, 3, 0, 8, 0, 6, 2, 5, 4, 1, 1, 1, 2, 8, 7, 4, 3, 6, 0, 9, 0, 5, 5, 7, 5, 2, 7, 6, 4, 0, 5, 5, 8, 9, 8, 6, 9, 8, 5, 6, 9, 4, 0, 1, 7, 6, 0, 6, 2, 7, 7, 2, 3, 4, 4, 0, 3, 6, 0, 5,6, 8, 2, 6, 7, 9, 8, 5, 6, 8, 1, 6, 8, 5, 0, 1, 4, 7, 0, 2, 3, 8, 0, 6, 6, 2, 4, 5, 1, 9, 6, 6, 8, 3, 9, 2, 8, 1, 0, 9, 6, 7, 7, 3, 3, 2, 0, 0, 6, 7, 0, 3, 9, 3, 0, 2, 8, 0, 7, 0, 7, 7, 6, 9, 9, 5, 2, 6, 2, 1, 8, 3, 5, 4, 3, 4, 6, 1, 4, 4, 1, 2, 4, 7, 9, 5, 4, 6, 7, 3, 8, 4, 5, 2, 9,9, 1, 6, 4, 8, 6, 2, 0, 7, 5, 7, 8, 8, 1, 4, 0, 0, 8, 7, 3, 7, 2, 0, 0, 3, 1, 5, 8, 8, 0, 2, 6, 8, 1, 3, 7, 0, 5, 2, 1, 0, 4, 3, 7, 6, 6, 8, 8, 2, 1, 9, 6, 5, 7, 7, 7, 7]
# rand = [random.randint(0, 9) for e in range(500)]


print('[50] Sorted table = ' + str(sortBubble(a)))
print('[100] Sorted table = ' + str(sortBubble(b)))
print('[500] Sorted table = ' + str(sortBubble(c)))
'''