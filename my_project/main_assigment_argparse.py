import re
from custom_modules.api_functions import import_cars_by_brand, import_cars_by_plate

import argparse

# define the argument parser
parser = argparse.ArgumentParser()

# add arguments to the argument parser
parser.add_argument('--import_by', 
                    type=str, 
                    required=False,
                    choices=['brand', 'plate'], 
                    default='brand')

parser.add_argument('--brand', 
                    type=str,
                    required=False)

parser.add_argument('--plate', 
                    type=str,
                    required=False)

parser.add_argument('--color', 
                    type=str,
                    required=False)
                    


# parse the arguments
args = parser.parse_args()


# execute if it is the main script
if __name__ == '__main__':

    # verify the supplied arguments
    #if ('brand' not in vars(args) and args.import_by == 'brand'):
    #    parser.error('If you import by brand, you should specify the --brand')

    # get the value of 'import_by'
    import_by = args.import_by

    # verify if the color is specified
    selected_color = args.color

    if import_by == 'brand':
        selected_brand = args.brand

        if selected_color == None:
            cars_list = import_cars_by_brand(selected_brand)
        else:
            print("By Color")
            cars_list = import_cars_by_brand(selected_brand, selected_color)
    else:
        selected_plate = args.plate
        cars_list = import_cars_by_plate(selected_plate)


    print(cars_list)