from custom_modules.api_functions import import_cars_by_plate
from custom_modules.conversion_functions import convert_list_to_df
from custom_modules.export_functions import export_df_to_sql


# specify the plate
selected_plate = input("Insert a license plate:\n")

# import from the API
cars_list = import_cars_by_plate(selected_plate)

# convert to a data frame
cars_df = convert_list_to_df(cars_list)

# export the data frame to a database
export_df_to_sql(cars_df)
