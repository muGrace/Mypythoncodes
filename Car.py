class Car_import():

    def __inti__(self,make,model,year):
        """Car attribute initialized in the constructor"""
        self.make-make
        self.model=model
        self.year=year

        self.fuel_capacity=120
        self.fuel_level=12

        """functions inside a classs -are class methods or simply methods"""

        def fill_tank_import(self):
            self.fuel_level=self.fuel_capacity
            print("\nCar has now been fueled!")

            def drive_import(self):
                print("you are now cruising in the CBD!")
class Battery_import():
    def __init__(self,size=70):
        self.size=size
        self.charge_level=0

    def get_range(self):
        if self.size ==70:
            return 240

        elif self.size ==85:
            return 270

class CarElectric_import(Car_import):
    def __inti__(self,make,model,year):
        super(). __init__(make,model,year)

        self.battery=Battery_import()


    def  charge_import(self):
        self.battery.charge_level=99
        print("\nThe vehicle has sufficient charge!")

        
        
        
