"""
Unit testing with Python for Session1 function

@brief get started with python testing by looking at https://docs.pytest.org/en/latest/getting-started.html#getstarted. Note that any script to be ran within the python testing framework (pytest) should follow the standard test discovery rules (https://docs.pytest.org/en/latest/goodpractices.html#test-discovery)
"""

import os
import numpy as np

print('Starting test script from working directory : ' + os.getcwd())

#testing session 1 functions
def load_s1_script():
    """
        utility function that tris to load the script written along the first lesson
        @throws an ImportError exception if the script file does not exist
        @return the script as a loaded module
    """
    s1_script_filename = 'assignments/Session1/S1_algotools.py'
    print('Trying to load target scripts : ' + s1_script_filename)
    import imp
    s1_algotools=imp.load_source('session_1_script', s1_script_filename)
    return  s1_algotools



#load the scripts to check
def test_session1script_exists():
    try:
        load_s1_script()
        assert True
    except  ImportError:
        print('Expected script not found, carrefuly check the assignement instructions ')
        assert False

# ----------- TEST FOR average_above_zero FUNCTION -----------

def test_s1_selective_average_non_zeros_values():
    ##
    # @test validates average_above_zero works fine with integer values > 0
    assert load_s1_script().average_above_zero([1, 2, 3, 4, -7]) == 2.5

def test_s1_selective_average_with_zeros_values():
    ##
    # @test validates average_above_zero works fine with integer values >= 0
    assert load_s1_script().average_above_zero([0, 1, 2, 3, 4, -7]) == 2.0

def test_s1_selective_average_with_negative_values():
    ##
    # @test validates average_above_zero works fine with integer values <= 0
    assert load_s1_script().average_above_zero([0, -7]) == 0

def test_s1_selective_average_with_string_values():
    ##
    # @test validates average_above_zero works fine with integer values <= 0
    try:
        load_s1_script().average_above_zero(['ad', 'c'])
        assert False
    except ZeroDivisionError:
        assert True

def test_s1_selective_average_with_empty_values():
    ##
    # @test validates average_above_zero works fine with an empty list
    try:
        load_s1_script().average_above_zero([])
        assert False
    except ValueError:
        assert True

def test_s1_selective_average_with_string():
    ##
    # @test validates average_above_zero works fine with an string
    try:
        load_s1_script().average_above_zero('string')
        assert False
    except TypeError:
        assert True

# ----------- TEST FOR max_value FUNCTION -----------

def test_s1_max_value():
    ##
    # @test validates max_value works fine with integer values > 0
    assert load_s1_script().max_value([1, 2, 3, 4, 10]) == (10, 4)

def test_s1_max_value_with_negative_value():
    ##
    # @test validates max_value works fine with integer values < 0
    assert load_s1_script().max_value([-1, -2, -3, -4, -10]) == (-1, 0)

def test_s1_max_value_with_max_at_index_0():
    ##
    # @test validates max_value works fine with integer values > 0
    assert load_s1_script().max_value([77, 2, 3, 4, 10]) == (77, 0)

def test_s1_max_value_with_max_at_index_2():
    ##
    # @test validates max_value works fine with integer values > 0
    assert load_s1_script().max_value([1, 2, 42, 4, 10]) == (42, 2)

def test_s1_max_value_with_empty_array():
  ##
  # @test validates max_value works fine with empty array
  try:
    load_s1_script().max_value([])
    assert False
  except ValueError:
    assert True

def test_s1_max_value_with_no_array_value():
  ##
  # @test validates max_value works fine with an no array value
  try:
    load_s1_script().max_value('array')
    assert False
  except TypeError:
    assert True

# ----------- TEST FOR reverse_table FUNCTION -----------

def test_reverse_table_value():
    ##
    # @test validates reverse_table works fine with correct array
    assert load_s1_script().reverse_table([1, 2, 3, 4]) == [4, 3, 2, 1]

def test_reverse_table_value_negative():
    ##
    # @test validates reverse_table works fine with correct array, with negative value
    assert load_s1_script().reverse_table([1, -2, -3, 4]) == [4, -3, -2, 1]

def test_reverse_table_with_no_int_values():
    ##
    # @test validates reverse_table works fine with correct array but with not only number inside
    assert load_s1_script().reverse_table([1, -2, 'v', [4, 3]]) == [[4, 3], 'v', -2, 1]

def test_reverse_table_with_string():
    ##
    # @test validates reverse_table works fine with string instead of array
    try:
        load_s1_script().reverse_table('array')
        assert False
    except TypeError:
        assert True

# ----------- TEST FOR roi_bbox FUNCTION -----------

def test_roi_bbox_no_np_array():
    ##
    # @test validates roi_bbox works fine with no np.array given.
    try:
        load_s1_script().roi_bbox(42)
        assert False
    except TypeError:
        assert True


def test_roi_bbox_with_7_7_array():
    ##
    # @test validates roi_bbox works fine with 7*7 array.
    assert load_s1_script().roi_bbox(np.array([
            [0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 1, 0],
            [0, 0, 0, 1, 0, 0, 0],
            [0, 0, 0, 1, 1, 0, 0],
            [0, 0, 1, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0]
        ])).tolist() == [[2, 1], [5, 1], [2, 4], [5, 4]]


# ----------- TEST FOR random_fill_sparse FUNCTION -----------

def test_random_fill_sparse_value_with_no_int_k():
    ##
    # @test validates random_fill_sparse works fine with k as not Int
    try:
        load_s1_script().random_fill_sparse(np.array([['', '', ''], ['', '', '']]), 'dd')
        assert False
    except TypeError:
        assert True

def test_random_fill_sparse_value_with_no_np_array_table():
    ##
    # @test validates random_fill_sparse works fine with table as not np.array
    try:
        load_s1_script().random_fill_sparse([['', '', ''], ['', '', '']], 2)
        assert False
    except TypeError:
        assert True

# ----------- TEST FOR remove_whitespace FUNCTION -----------

def test_remove_whitespace_with_one_whitespace():
    ##
    # @test validates remove_whitespace works fine with string with 1 whitespace.
    assert load_s1_script().remove_whitespace('str ing') == 'string'

def test_remove_whitespace_with_many_whitespace():
    ##
    # @test validates remove_whitespace works fine with string with many whitespace.
    assert load_s1_script().remove_whitespace('   s    t   r i   n   g   ') == 'string'

def test_remove_whitespace_with_no_string_value():
    ##
    # @test validates remove_whitespace works fine with no string given.
    try:
        load_s1_script().remove_whitespace(42)
        assert False
    except TypeError:
        assert True

# ----------- TEST FOR shuffle FUNCTION -----------

def test_shuffle_with_no_array_value():
    ##
    # @test validates shuffle works fine with no array given.
    try:
        load_s1_script().shuffle(42)
        assert False
    except TypeError:
        assert True

def test_shuffle_with_array():
    ##
    # @test validates shuffle works fine with array, test if all number are there.
    array_test = [i for i in range(10)]
    init_sum = sum(array_test)
    result = load_s1_script().shuffle(array_test)

    assert init_sum == sum(result)

# ----------- TEST FOR sort_selective FUNCTION -----------


def test_sort_selective_with_no_array_value():
    ##
    # @test validates sort_selective works fine with no array given.
    try:
        load_s1_script().sort_selective(42)
        assert False
    except TypeError:
        assert True

def test_sort_selective_with_array_of_ten():
    ##
    # @test validates sort_selective works fine with array of 10 values.
    assert load_s1_script().sort_selective([2, 5, 3, 7, 9, 6, 7, 7, 1, 0]) == [0, 1, 2, 3, 5, 6, 7, 7, 7, 9]

# ----------- TEST FOR sort_bubble FUNCTION -----------


def test_sort_bubble_with_no_array_value():
    ##
    # @test validates sort_bubble works fine with no array given.
    try:
        load_s1_script().sort_bubble(42)
        assert False
    except TypeError:
        assert True

def test_sort_bubble_with_array_of_ten():
    ##
    # @test validates sort_bubble works fine with array of 10 values.
    assert load_s1_script().sort_bubble([2, 5, 3, 7, 9, 6, 7, 7, 1, 0]) == [0, 1, 2, 3, 5, 6, 7, 7, 7, 9]
