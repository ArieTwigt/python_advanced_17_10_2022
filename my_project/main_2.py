from custom_modules.api_functions import import_cars_by_brand

my_brand = input("Please select a Brand:\n")

cars = import_cars_by_brand(my_brand)

print(cars)