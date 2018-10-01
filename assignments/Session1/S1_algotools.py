
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

# Some test
average = average_above_zero([2, 5, 10])
average2 = average_above_zero([])
average3 = average_above_zero([-1, 2, 4])
average4 = average_above_zero('sdfndsjk')

print('Average of [2, 5, 10] is : ' + str(average))
print('Average of [] is : ' + str(average2))
print('Average of [-1, 2, 4] is : ' + str(average3))
print('Average of \'sdfndsjk\' is : ' + str(average4))