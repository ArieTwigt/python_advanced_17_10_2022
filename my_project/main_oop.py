from typing import Tuple

class Car:


    # methods
    def __init__(self, brand:str, model:str, color:str, price: int=0, availability: str="available"):
        self.brand = brand
        self.model = model
        self.color = color
        self.price = price
        self.availability = availability

    # method to change the availability of the car
    def reserve(self):
        print(f"Status: {self.availability}")
        self.availability = 'reserved'
        print(f"Status: {self.availability}")

    # method to change the car to sold
    def sell(self):
        print(f"Status: {self.availability}")
        self.availability = 'sold'
        print(f"Status: {self.availability}")

    
    # method for specifying the price of a car
    def set_price(self, price: float):
        print(f"Price {self.price}")
        self.price = price
        print(f"Price {self.price}")

    
    # method for changing the price of the car
    def change_price(self, amount: float) -> None:
        old_price = self.price
        self.price += amount
        print(f"Price changed from {old_price} to {self.price}")


    # represent the class
    def __repr__(self) -> str:
        return f"{self.brand}-{self.model}-{self.price}-{self.color}-{self.availability}"


if __name__ == '__main__':

    # create an instance of the 'Car' class
    my_car = Car('OPEL', 'vectra', 'red')
    my_car_2 = Car('TOYOTA', 'YARIS', 'green')
    my_car_3 = Car('BMW', 'i3', 'blue')

    # create a loop for the cars
    cars_list = [my_car, my_car_2, my_car_3]
    
    for car in cars_list:
        if car.brand == 'BMW':
            car.reserve()

    pass  

'''
* my_car.__dict__ #show the attributes in a dict:


'''