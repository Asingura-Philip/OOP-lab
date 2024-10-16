from class1 import Vehicle  

class Car(Vehicle):
    def __init__(self,winterTires=False):
        self.winterTires = winterTires
    def toString(self):
        print(f"has winter tires: {self.winterTires}")

car1 = Car()
car1.getColor("purple")
car1.toString()      
