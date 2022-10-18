import re
from custom_modules.api_functions import import_cars_by_brand, import_cars_by_plate
from custom_modules.conversion_functions import convert_list_to_df
from custom_modules.export_functions import export_df_to_csv, export_df_license_to_csv, export_df_to_sql


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
                    
parser.add_argument('--export',
                    type=str,
                    required=False,
                    choices=['print', 'db', 'csv'],
                    default='print')


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
            cars_df = convert_list_to_df(cars_list)
        else:
            print("By Color")
            cars_list = import_cars_by_brand(selected_brand, selected_color)
            cars_df = convert_list_to_df(cars_list)
    else:
        selected_plate = args.plate
        cars_list = import_cars_by_plate(selected_plate)

    # get the export_type
    export_type = args.export

    if export_type == 'csv':
        if import_by == 'brand':
            export_df_to_csv(cars_df, selected_brand)
        elif import_by == 'plate':
            export_df_license_to_csv(cars_df, selected_plate)
    elif export_type == 'db':
        export_df_to_sql(cars_df)
    else:
        print(cars_df)