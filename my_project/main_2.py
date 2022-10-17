from custom_modules.api_functions import import_cars_by_brand

my_brand = "VOLVO"

cars = import_cars_by_brand(my_brand)

print(cars)