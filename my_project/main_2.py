from custom_modules.api_functions import import_cars_by_brand
from custom_modules.conversion_functions import convert_list_to_df



# specify the brand
my_brand = input("Please select a Brand:\n")

# get the list of cars from the api
cars_list = import_cars_by_brand(my_brand)

# convert the list to a data frame
cars_df = convert_list_to_df(cars_list)

pass