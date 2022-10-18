from custom_modules.api_functions import import_cars_by_brand
from flask import Flask, render_template, request

# initiate the flask app
app = Flask(__name__)


# create a route
@app.route('/')
def index():
    return render_template("index.html")


# route for getting a car list by brand
@app.route('/cars', methods=['GET', 'POST'])
def cars():

    # if it is a GET request
    if request.method == 'GET':
        return render_template("cars.html")

    # if it is not a get, so a POST
    selected_brand = request.form.get("brand")

    # get the cars from the API
    cars_list = import_cars_by_brand(selected_brand)
    
    return render_template("cars.html", cars_list=cars_list)


if __name__ == '__main__':
    app.run()

