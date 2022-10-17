from custom_modules.api_functions import import_cars_by_plate
from custom_modules.conversion_functions import convert_list_to_df
from custom_modules.export_functions import export_df_license_to_csv

# specify the plate
my_plate = input("Specify the License plate:\n") or None


# import the cars
cars_list = import_cars_by_plate(my_plate)

# convert to data
cars_df = convert_list_to_df(cars_list)

# export the car
export_df_license_to_csv(cars_df, my_plate)