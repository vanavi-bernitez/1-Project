#import sys 
#print(sys.version)

class Autos:
    #este sería como el setter?
    #Special method: constructor, main diff between functions and methods
    #does not have a return value
    def __init__(self, marca, color):
        self.marca = marca
        self.color = color

    #Se comporta como el getter
    def show(self):
        return print("Brand", self.marca), print("Color", self.color)

    #Método random
    def change(self):
        return print(self.marca,"cambiar a Toyota")

#crear una instancia llamada auto1 de la clase  y le ingresamos los atributos que requiere esa clase
marca = str(input("Enter car brand: "))
color = str(input("Enter car color: "))
auto1 = Autos(marca,color)
#instancia llamada auto2 de la clase Autos
auto2 = Autos("Chevrolet", "azul islandia")
#ahora motrar la interface del método show
auto1.show()
auto2.show()
#return change method
auto2.change()

