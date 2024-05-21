class Car:
    carType = ""
    #Constructor
    def __init__(self, color, carType):
        self.color = color
        self.carType = carType
    

    def driver(self):
        print("I'm driving "+self.color)

    def start(self):
        print("I'm starting "+self.carType)
    
    
    
    