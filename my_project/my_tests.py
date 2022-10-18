import pytest
from custom_modules.calculation_functions import calc_interest_print, calc_interest_inflation_print


# define the tests
def test_calc_interest_print():
    assert calc_interest_print(100, 5, 1) == 105
    assert calc_interest_print(100, 5, 2) == 110.25


def test_calc_interest_inflation_print():
    assert round(calc_interest_inflation_print(100, 5, 5), 2) == 113.14
    assert round(calc_interest_inflation_print(100, 5, 10), 2) == 128.01


'''
Install the pytest library
* pip3 install pytest

Generating a test report -> run the Command Line /Terminal
* pytest -q my_tests.py --junitxml=report.xml

'''