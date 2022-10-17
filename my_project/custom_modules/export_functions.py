import pandas as pd
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