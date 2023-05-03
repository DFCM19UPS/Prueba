from robot_model import Robot_model
from robot_view import View

class Controller_Robot:
    
    def __init__(self, model, view):
        self.model=Robot_model()
        self.view=View()
        
    def run(self):
        while True:
            
            command=input("Ingrese la orden 'move' or 'stop': " )
            if command=='move' or "Move" or "MOVE":
                
                elevation=self.elevation
                rotation=self.rotation
                length=self.length    
                
                self.model.move_elevation(elevation)
                self.model.move_rotation(rotation)
                self.model.move_length(length)
            
            else:
                self.model.stopped