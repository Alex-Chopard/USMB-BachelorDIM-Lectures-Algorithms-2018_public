"""
Basic introduction to unit testing with Python

@brief get started with python testing by looking at https://docs.pytest.org/en/latest/getting-started.html#getstarted. Note that any script to be ran within the python testing framework (pytest) should follow the standard test discovery rules (https://docs.pytest.org/en/latest/goodpractices.html#test-discovery)
"""

import os

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

def test_S1_selective_average_non_zeros_values():
    ##
    # @test validates average_above_zero works fine with integer values > 0
    assert load_s1_script().average_above_zero([1, 2, 3, 4, -7]) == 2.5

def test_S1_selective_average_with_zeros_values():
    ##
    # @test validates average_above_zero works fine with integer values >= 0
    assert load_s1_script().average_above_zero([0, 1, 2, 3, 4, -7]) == 2.0

def test_S1_selective_average_with_negative_values():
    ##
    # @test validates average_above_zero works fine with integer values <= 0
    assert load_s1_script().average_above_zero([0, -7]) == 0

def test_S1_selective_average_with_string_values():
    ##
    # @test validates average_above_zero works fine with integer values <= 0
    try:
        load_s1_script().average_above_zero(['ad', 'c'])
        assert False
    except ZeroDivisionError:
        assert True

def test_S1_selective_average_with_empty_values():
    ##
    # @test validates average_above_zero works fine with an empty list
    try:
        load_s1_script().average_above_zero([])
        assert False
    except ValueError:
        assert True

def test_S1_selective_average_with_string():
    ##
    # @test validates average_above_zero works fine with an string
    try:
        load_s1_script().average_above_zero('string')
        assert False
    except TypeError:
        assert True
