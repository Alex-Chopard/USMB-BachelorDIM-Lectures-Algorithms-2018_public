
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