import requests


def import_cars_by_brand(brand: str) -> None:
    '''
    Imports data from the car API
    
    '''
    # uppercase the brand
    brand_upper = brand.upper()


    # define the endpoint for the API
    endpoint = f"https://opendata.rdw.nl/resource/m9d7-ebf2.json?merk={brand_upper}"
    
    # execute the GET request for the endpoint
    response = requests.get(endpoint)

    # method for extracting JSON from the body
    cars_list = response.json()

    return cars_list