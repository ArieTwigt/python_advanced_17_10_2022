import pandas as pd
import numpy as np
import sqlite3
import os


def export_df_to_csv(df: pd.DataFrame, brand: str) -> None:
    '''
    Exports the DataFrame to a CSV-file in the filesystem
    
    '''

    # uppercase the brand name
    brand_upper = brand.upper()

    # export the csv in the right brand folder
    folder_name = f"data/brand/{brand_upper}/"

    # create the sub folder
    os.makedirs(folder_name, exist_ok=True)

    # compose the file name
    file_name = f"{folder_name}export_{brand}.csv"

    # export the DataFrame to csv
    print(f"Exporting to {file_name}")
    df.to_csv(file_name, sep=";", index=False)


def export_df_license_to_csv(df: pd.DataFrame, plate: str) -> None:
    '''
    Export the data set
    '''
    
    # specify the brand, get it from the columns in the data frame
    selected_brand = df['merk'][0]
    selected_brand_upper = selected_brand.upper()

    # format the plate
    plate_upper_no_dash = plate.lower().replace("-", "")\

    # export the csv in the right brand folder
    folder_name = f"data/license/{selected_brand_upper}/"

    # create the sub folder
    os.makedirs(folder_name, exist_ok=True)

    # compose the file name
    file_name = f"{folder_name}export_{plate_upper_no_dash}.csv"

    # export
    print(f"🚗 Exporting to {file_name}")
    df.to_csv(file_name, sep=";", index=False)


def export_df_to_sql(df: pd.DataFrame) -> None:
    '''
    Function to export the data frame to a database
    
    '''

    # specify the database path
    db_path = "data/data.db"
    
    # create the connection string
    con = sqlite3.connect(db_path)

    # specify the columns we want to export
    columns_list = ['kenteken', 'merk', 'handelsbenaming', 'eerste_kleur', 'catalogusprijs', 'aantal_cilinders']

    # loop through the DataFrame to check if all the columns are available
    for column in columns_list:
        if column not in df.columns:
            df[column] = np.nan

    # export the pandas data frame to the database
    print(f"Writing to the database {db_path}")
    df.to_sql('licensed_cars', con=con, index=False, if_exists='append')