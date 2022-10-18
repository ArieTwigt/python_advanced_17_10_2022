from multiprocessing.sharedctypes import Value
import requests


def import_cars_by_brand(brand: str, color: str=None) -> list:
    '''
    Imports data from the car API
    
    '''
    # uppercase the brand
    brand_upper = brand.upper()


    # define the endpoint for the API
    if color == None:
        endpoint = f"https://opendata.rdw.nl/resource/m9d7-ebf2.json?merk={brand_upper}"
    else:
        color_upper = color.upper()
        endpoint = f"https://opendata.rdw.nl/resource/m9d7-ebf2.json?merk={brand_upper}?eerste_kleur={color_upper}"
    
    # execute the GET request for the endpoint
    response = requests.get(endpoint)

    # method for extracting JSON from the body
    cars_list = response.json()

    return cars_list


def import_cars_by_plate(plate:str) -> list:
    '''
    Imports data from the car API
    
    '''

    # modify the plate
    # uppercase
    plate_upper_no_dash = plate.upper().replace("-", "") # method-chaining
    

    # define the endpoint
    endpoint = f"https://opendata.rdw.nl/resource/m9d7-ebf2.json?kenteken={plate_upper_no_dash}"

    # execute the request for the endpoint
    response = requests.get(endpoint)

    # get the data from the response
    cars_list = response.json()

    # if the list is empty
    if len(cars_list) == 0:
        raise ValueError(f"No cars found for plate: {plate}")

    return cars_list