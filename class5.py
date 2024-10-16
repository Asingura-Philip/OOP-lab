from class4 import Garage
from class3 import Truck

class GarageTester:
    @staticmethod
    def getExample():
        
        truck = Truck(color="black", has_trailer=False)
        garage = Garage()
        garage.setVehicle(truck)
        print(garage.toString())
