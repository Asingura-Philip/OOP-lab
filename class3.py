from class1 import Vehicle

class Truck(Vehicle):
    def __init__(self,hasTrailer=False):
        self.hasTrailer = hasTrailer

    def toString(self):
        print(f"has trailer: {self.hasTrailer}")


truck1 = Truck()
truck1.toString()