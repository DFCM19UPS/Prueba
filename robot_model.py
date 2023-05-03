class Robot_model:
    def __init__(self):
        self.rotation=0
        self.elevation=0
        self.length=0
    
    def move_rotation(self, rotation):
        self.rotation = rotation
        print(f'Moviendo hacia {self.rotation} grados')
    
    def move_elevation(self, elevation):
        self.elevation=elevation
        print(f'Elevando {self.elevation} grados')
    
    def move_length(self, length):
        self.length=length
        print(f'Estirando {self.length} cm')
        
    def stopped(self):
        print('Deteniendo movimientos')
    
        
        
#robot=Robot_model()    
#robot.move_rotation(86)
#robot.move_length(15)
#robot.move_elevation(10)