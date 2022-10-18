
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


if __name__ == '__main__':

    my_result =  calc_interest_inflation_print(100, 5, 10)
    my_result_2 = calc_interest_print(100, 5, 10)

    pass