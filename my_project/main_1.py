from custom_modules.calculation_functions import calc_circle


my_diameter = float(input("Provide the value of the diameter:\n"))

my_rounding = input("How do you want to round? (1)\n") or '1'
my_rounding = int(my_rounding)

my_circle = calc_circle(my_diameter, my_rounding)

print(my_circle)