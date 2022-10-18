from custom_modules.api_functions import import_cars_by_brand
from flask import Flask

# initiate the flask app
app = Flask(__name__)


# create a route
@app.route('/')
def index():
    return "Hello world!"


# route for getting a car list by brand
@app.route('/cars')
def cars():
    selected_brand = "TESLA"
    cars_list = import_cars_by_brand(selected_brand)
    return cars_list


if __name__ == '__main__':
    app.run()

