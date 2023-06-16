class Engine:
    def __init__(self, engine_type, volume, number):
        self.type = engine_type
        self.volume = volume
        self.number = number
        
    def start(self):
        print(f'I am {self.number} engine im starting')
        
class Car:
    def __init__(self, model, color, vin, engine):
        self.model = model
        self.color = color
        self.vin = vin
        self.engine = engine