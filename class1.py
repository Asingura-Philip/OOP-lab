class Vehicle:
    def __init__(self):
        self.color = None
    def getColor(self,color):
            self.color = color
    def toString(self):
            print(f"This vehicle is {self.color}")

vehicle1 = Vehicle()
vehicle1.getColor("blue")
vehicle1.toString()