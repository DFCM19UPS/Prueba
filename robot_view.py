class View:
    def get_information(self):
        rotation=int(input("¿Cuantos grados desea rotar?: "))
        elevation=int(input("¿Cuantos cm desea elevar?: "))
        length=int(input("¿Cuantos cm desea estirar?: "))
        return rotation,elevation,length
    
    
    def show_error(self, message):
        print(f"Error: {message}")
        
                     
  