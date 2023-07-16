class Car:
    def __init__(self, car_version):
        self.car_version = car_version

    def typeCar(self):
        print("unclassified")
    
    def version(self):
        print("version:" , self.car_version)
    
    def __del__(self):
        print("Car destroyed")
    
class Electric_car(Car):
    def typeCar(self):
        print("electric car")

tesla = Electric_car("xy")
tesla.typeCar()
tesla.version()
del tesla