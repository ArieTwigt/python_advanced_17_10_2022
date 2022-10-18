class Car:


    # methods
    def __init__(self, brand:str, model:str, availability: str="available"):
        self.brand = brand
        self.model = model
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
    

    # represent the class
    def __repr__(self) -> str:
        return f"{self.brand}-{self.model}-{self.availability}"


if __name__ == '__main__':

    # create an instance of the 'Car' class
    my_car = Car('OPEL', 'vectra')
    my_car_2 = Car('TOYOTA', 'YARIS')
    my_car_3 = Car('BMW', 'i3')

    # create a loop for the cars
    cars_list = [my_car, my_car_2, my_car_3]
    
    for car in cars_list:
        if car.brand == 'BMW':
            car.reserve()

    pass  

'''
* my_car.__dict__ #show the attributes in a dict:


'''