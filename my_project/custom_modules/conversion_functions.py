import pandas as pd
import numpy as np


def convert_list_to_df(obj_list: list) -> pd.DataFrame:
    '''
    Converts a list to a DataFrame
    
    '''

    # convert to a DataFrame
    cars_df = pd.DataFrame(obj_list)

    # converting a column in a data frame

    # price
    cars_df['catalogusprijs'] = cars_df['catalogusprijs'].astype(float)

    # cilinders
    cars_df['aantal_cilinders'] = cars_df['aantal_cilinders'].fillna(0)
    cars_df['aantal_cilinders'] = cars_df['aantal_cilinders'].astype(int)

    # replace 0 cilinders for the median
    cars_df['aantal_cilinders'] = np.where(cars_df['aantal_cilinders'] == 0,     # evaluation
                                           cars_df['aantal_cilinders'].median(), # if evaluation is True
                                           cars_df['aantal_cilinders'])          # if evaluation is False


    # specify subset of columns
    columns_list = ['merk', 'handelsbenaming', 'eerste_kleur', 
                    'catalogusprijs', 'aantal_cilinders']

    cars_df_subset = cars_df[columns_list]

    return cars_df_subset


'''
Exploring the Data Frame

* df.head()
* df.info()
* df['column'].unique()
* df['column'].value_counts()
* df.describe()

* df['column'].isna() # detecting NaN values
* cars_df[cars_df['aantal_cilinders'].isna()] # show rows with NaN

* Filtering

selected_colours = ['WIT', 'ZWART']
cars_df_subset.query("aantal_cilinders > 4 & eerste_kleur == @selected_colours")



'''