class Garage:
    def __init__(self,vehicle):
        self.vehicle = vehicle

    def setVehicle(self):
        print("vehicle parked")

    def toString(self):
        print(f"Description of the parked vehicle: {self.vehicle.toString()}")


