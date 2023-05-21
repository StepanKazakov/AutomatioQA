class Cars():
    #create new class cars#

    def __init__(self, model, year, eng_volume, price, mileage):
        #set base attributes for cars#
        self.model = model
        self.year = year
        self.eng_volume = eng_volume
        self.price = price
        self.mileage = mileage
        self.wheels = 4

    def description_car(self):
        #set description for new car#
        description = 'New car model: ' + self.model + ',\nyear of manufacture: ' + self.year + ',\nengine volume: ' + self.eng_volume + ' cm3,\nprice: $' + str(self.price) + ',\nmileage: ' + self.mileage + ' km,\nwheels: ' + str(self.wheels)
        return description

class Truck(Cars):
    #create cars subclass - trucks#

    def __init__(self, model, year, eng_volume, price, mileage):
        super().__init__(model, year, eng_volume, price, mileage)
        #set specify attribute for truck#
        self.wheels = 8

    def description_truck(self):
        # set description for new truck#
        description = 'New truck model: ' + self.model + ',\nyear of manufacture: ' + self.year + ',\nengine volume: ' + self.eng_volume + ' cm3,\nprice: $' + str(
            self.price) + ',\nmileage: ' + self.mileage + ' km,\nwheels: ' + str(self.wheels)
        return description

ferrari = Cars('Ferrari 430', '2000', '5998', 500000, '350000')
print(ferrari.description_car())
print()
volvo = Truck('Volvo', '2023', '15995', 1500000, '100')
print(volvo.description_truck())