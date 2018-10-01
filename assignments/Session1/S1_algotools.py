print('Hello World')

def average_above_zero (items):
  """
    brief: compute the average of an given array only for positive values
    Args:
      items: array of positive values
    return:
      the computed average
      or -1 if items prop is empty or if is not an array
  """

  # Don't compute if items isn't an List (array)
  if type(items) is not list:
    return -1

  average = -1
  sum = 0
  itemsLength = len(items)

  # Don't compute if items is empty
  if itemsLength > 0:
    for item in items:
      if item > 0:
        sum += item
    average = sum / itemsLength

  return average


average = average_above_zero([2, 5, 10])
average2 = average_above_zero([])
average3 = average_above_zero([-1, 2, 4])
average4 = average_above_zero('sdfndsjk')

print('Average of [2, 5, 10] is : ' + str(average))
print('Average of [] is : ' + str(average2))
print('Average of [-1, 2, 4] is : ' + str(average3))
print('Average of \'sdfndsjk\' is : ' + str(average4))