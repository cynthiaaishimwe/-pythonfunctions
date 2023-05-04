
class Fruit:

    color:"red"
    type:"citrus"
    size:"medium"
    shape:"oval"

def __init__(self, color, type, size,shape):
       
        self.color = color
        self.type = type
        self.size = size
        self.shape = shape

def grow(self):
      return f"my{self.type} is growing in an {self.size}"