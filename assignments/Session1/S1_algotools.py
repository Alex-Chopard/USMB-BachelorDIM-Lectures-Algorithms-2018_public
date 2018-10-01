
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
average = average_above_zero([2, 5, 10])
average2 = average_above_zero([])
average3 = average_above_zero([-1, 2, 4])
average4 = average_above_zero('sdfndsjk')

print('Average of [2, 5, 10] is : ' + str(average))
print('Average of [] is : ' + str(average2))
print('Average of [-1, 2, 4] is : ' + str(average3))
print('Average of \'sdfndsjk\' is : ' + str(average4))

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
    return ValueError('Type of items param need to be \'list\' and not ' + str(type(items)))

  itemsLength = len(items)
  maxValue = None

  if itemsLength > 0:
    for item in items:
      number = float(item)
      if maxValue == None or number > maxValue:
        maxValue = number
  else:
    return ValueError('Items list must not be empty')

  return maxValue, 1


# Some test for max_value function
average = max_value([2, 5, 10])
average2 = max_value([])
average3 = max_value([-1, 2, 4])
average4 = max_value('sdfndsjk')

print('max_value of [2, 5, 10] is : ' + str(average[1]) + ' and index is : ' + str(average[0]))
print('max_value of [] is : ' + str(average2[1]) + ' and index is : ' + str(average2[0]))
print('max_value of [-1, 2, 4] is : ' + str(average3[1]) + ' and index is : ' + str(average3[0]))
print('max_value of \'sdfndsjk\' is : ' + str(average4[1]) + ' and index is : ' + str(average4[0]))