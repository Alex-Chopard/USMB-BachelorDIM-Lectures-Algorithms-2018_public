import numpy as np
import random

def average_above_zero (items):
  """
    Compute the average of an given array only for positive values.

    @type items: list
    @param items: List of positive values

    @rtype: float
    @return: Return the average of the list
  """

  # Don't compute if items isn't an List (array)
  if type(items) is not list:
    raise TypeError('Type of items param need to be \'list\' and not ' + str(type(items)))

  average = -1
  sum = 0
  items_length = len(items)

  # Don't compute if items is empty
  if items_length > 0:
    for item in items:
      if (type(item) is float or type(item) is int) and item >= 0:
        sum += float(item)
      else:
        # Remove 1 to items_length if item isn't an positive value
        items_length -= 1
    average = sum / items_length
  else:
    raise ValueError('Items list must not be empty')

  return average


def max_value (items):
  """
    Function for found the max value of list

    @type items: list
    @param items: List of values

    @rtype: float
    @return: Return the max value of the list
  """

   # Don't compute if items isn't an List (array)
  if type(items) is not list:
    raise TypeError('Type of items param need to be \'list\' and not ' + str(type(items)))

  items_length = len(items)
  max_val = None
  index = None

  # Find max number in items list
  if items_length > 0:
    for key, item in enumerate(items, start = 0):
      number = float(item)
      if max_val == None or number > max_val:
        max_val = number
        index = key
  else:
    raise ValueError('Items list must not be empty')

  return max_val, index


def reverse_table (items):
  """
    Useless function for reverte an list

    @type items: list
    @param items: List of values to reverte

    @rtype: list
    @return: Return reverted list
  """

  # Don't compute if items isn't an List (array)
  if type(items) is not list:
    raise TypeError('Type of items param need to be \'list\' and not ' + str(type(items)))

  return items[::-1]


def roi_bbox (input_image) :
  """
    Function compute the boundary box of an binary image

    @type input_image: numpy array
    @param input_image: The binary image

    @rtype: numpy array
    @return: Return boundary box of an binary image
  """

  if (type(input_image) is not np.ndarray):
    raise TypeError('Type of k must be \'numpy.ndarray\' and not ' + str(type(input_image)))

  x = { 'min': None, 'max': None }
  y = { 'min': None, 'max': None }

  comput_min_max(y, input_image)

  input_image_rotated = np.rot90(input_image, 3)
  comput_min_max(x, input_image_rotated)

  '''
  for index, row in enumerate(input_image_rotated):
    length = row.size - 1
    max = max_value(row.tolist())[0]
    if max != 0:
      if width_max == -1:
        width_max = length - index
      width_min = length - index
  '''
  print(np.array([[x['min'], y['min']], [x['max'], y['min']], [x['min'], y['max']], [x['max'], y['max']]]))
  return np.array([[x['min'], y['min']], [x['max'], y['min']], [x['min'], y['max']], [x['max'], y['max']]])

def comput_min_max (coo, mat):
  for index, row in enumerate(mat):
    max = max_value(row.tolist())[0]
    if max != 0:
      if coo['max'] == None:
        coo['max'] = index
      coo['min'] = index

def random_fill_sparse (table, k):
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
    raise TypeError('Type of k must be \'int\' and not ' + str(type(k)))
  if (type(table) is not np.ndarray):
    raise TypeError('Type of k must be \'numpy.ndarray\' and not ' + str(type(table)))

  shape = table.shape

  if (k > shape[0] * shape[1]):
    k = shape[0] * shape[1]
  x_max = shape[1] - 1
  y_max = shape[0] - 1

  while k > 0:
    k -= 1
    x = random.randint(0, x_max)
    y = random.randint(0, y_max)
    if (table[y, x] == 'X'):
      k += 1
    else:
      table[y, x] = 'X'

  return table


def remove_whitespace (string):
  """
    Useless function how remove all whitespaces of string

    @type string: numpy str
    @param string: The string with whitespaces

    @rtype: str
    @return: Return the saem string but whitout whitespaces
  """
  if (type(string) is not str):
    raise TypeError('Type of string must be \'str\' and not ' + str(type(string)))

  return string.replace(' ', '')


def shuffle (array):
  """
    Useless function how shuffle an given list

    @type array: list
    @param array: The list how need to be shiffuled

    @rtype: list
    @return: Return the shuffled list
  """
  if (type(array) is not list):
    raise TypeError('Type of array must be \'list\' and not ' + str(type(array)))

  random.shuffle(array)
  return array


def sort_selective (array):
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
    raise TypeError('Type of array must be \'list\' and not ' + str(type(array)))
  
  n = len(array)

  for j in range(n - 1):
    i_min = j
    for i in range(j + 1, n):
      if (array[i] < array[i_min]):
        i_min = i
    
    if (i_min != j):
      # Swape value
      tmp = array[j]
      array[j] = array[i_min]
      array[i_min] = tmp

  return array

def sort_bubble (array):
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
    raise TypeError('Type of array must be \'list\' and not ' + str(type(array)))

  n = len(array)
  swapped = True

  while swapped:
    swapped = False

    for i in range(n - 1):
      if array[i] > array[i + 1]:
        #swape value
        tmp = array[i]
        array[i] = array[i + 1]
        array[i + 1] = tmp
        swapped = True

  return array
