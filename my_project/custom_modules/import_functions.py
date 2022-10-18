import pandas as pd
import sqlite3


def import_license_from_db(plate: str) -> pd.DataFrame:
    '''
    Importing a single car from the database
    '''

    # specify the database path
    db_path = 'data/data.db'

    # setup the connection_string
    con = sqlite3.connect(db_path)

    # specify the query
    qry = '''
          SELECT kenteken, merk, handelsbenaming, 
                eerste_kleur, catalogusprijs, 
                aantal_cilinders
          FROM licensed_cars
          WHERE kenteken = ?
          '''

    # read the data into the data frame
    df_car = pd.read_sql_query(qry, con=con, params=(plate,))

    return df_car