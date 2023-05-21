
class Car:
    tires:4
    model="Mustang"
    brand="Ford"
    color="Grey"


    
    def __init__(self, tires, model,brand, color):
        
        self.tires = tires
        self.model = model
        self.brand = brand
        self.color = color
    
    def start_moving(self):
        return f"my car has{self.tires}"
    

