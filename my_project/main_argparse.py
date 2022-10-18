from custom_modules.calculation_functions import calc_circle
import argparse

# define a argument parser
parser = argparse.ArgumentParser()

# add arguments to the argument parser
parser.add_argument("--diameter", type=float, required=True, help="Required: The diameter of the circle")
parser.add_argument("--rounding", type=int, required=False, default=1, help="Optional: Rounding for the value")
parser.add_argument("--import_type", type=str, required=False, choices=['brand', 'license'], default='brand')

# parse the arguments
args = parser.parse_args()

# get the values of the arguments from the argument parser
my_diameter = args.diameter
my_rounding = args.rounding

my_circle = calc_circle(my_diameter, rounding=my_rounding)

print(my_circle)