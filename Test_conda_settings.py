#import sys 
#print(sys.version)

class Autos:
    #este sería el setter
    def __init__(self, marca, color):
        self.marca = marca
        self.color = color

    #y este sería el getter
    def show(self):
        return print("Brand", self.marca), print("Color", self.color)

    def change(self):
        return print(self.marca,"cambiar a Toyota")

#crear una instancia llamada auto1 de la clase  y le ingresamos los atributos que requiere esa clase
marca = str(input("Enter car brand: "))
color = str(input("Enter car color: "))
auto1 = Autos(marca,color)
auto2 = Autos("CHevrolet", "azul islandia")
#ahora motrar la interface del método show
auto1.show()
auto2.show()
auto2.change()

