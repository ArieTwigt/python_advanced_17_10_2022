# define a function/method with "type hinting"
import math


def calc_circle(diameter: float, rounding: int=1) -> float:
    '''
    Calculates the size of a circle    
    '''

    radius = diameter / 2
    size = (radius ** 2) * math.pi
    size_rounded = round(size, rounding)

    return size_rounded


# define the decorator for inflation
def inflation_adjusted(func):

    def wrapper(amount, rate, years):
        return func(amount, rate / 2, years)
    
    return wrapper


# define the decorator for printing the yearly interest
def print_interest(func):
    
    def wrapper(amount, rate, years):
        for year in range(years):
            amount = func(amount, rate, 1)
            print(f"{year +1}: {amount}")
        return amount
    return wrapper


# define the base function
@inflation_adjusted
@print_interest
def calc_interest_inflation_print(amount: float, rate: float, years:int) -> float:
    rate = rate / 100
    result = amount * (1 + rate) ** years
    return result


@inflation_adjusted
def calc_interest_inflation(amount: float, rate: float, years:int) -> float:
    rate = rate / 100
    result = amount * (1 + rate) ** years
    return result

@print_interest
def calc_interest_print(amount: float, rate: float, years:int) -> float:
    rate = rate / 100
    result = amount * (1 + rate) ** years
    return result