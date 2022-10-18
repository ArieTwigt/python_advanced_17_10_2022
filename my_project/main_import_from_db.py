from custom_modules.import_functions import import_license_from_db

selected_plate = "RD799K"

car_df = import_license_from_db(selected_plate)
