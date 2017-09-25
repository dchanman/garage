class Garage:
    def __init__(self, abstract_door_io):
        self.door_io = abstract_door_io
    
    def toggle(self):
        self.door_io.toggle()