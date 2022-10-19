#import sys 
#print(sys.version)

class Autos:

    """class variables != instance variables
    we set class variables inside the class, and are shared among all instances
    car_1.num_of_cars = car_2.num_of_cars = Autos.num_of_cars """
    num_of_cars = 0
    price_of_cars = 500
    
    #este sería como el setter?
    #Special method: constructor, main diff between functions and methods
    #does not have a return value
    def __init__(self, marca, color, price):
        self.marca = marca
        self.color = color
        self.price = price
        Autos.num_of_cars += 1

    #Se comporta como el getter
    def show(self):
        #return print(Autos.num_of_cars)
        return print("Brand", self.marca), print("Color", self.color)

    #Método que une los atributos marca y color y los muestra en uno solo
    def full_inf(self):
        return print('{} {}'.format(self.marca, self.color))

    def final_price(self):
        return self.price * self.price_of_cars
    

"""crear una instancia llamada auto1 de la clase  y le ingresamos los atributos que requiere esa clase """
marca = str(input("Enter car brand: "))
color = str(input("Enter car color: "))
auto1 = Autos(marca,color, float(0.2))

""" instancia llamada auto2 de la clase Autos """
auto2 = Autos("Chevrolet", "azul islandia",float(0.1))

""" instancia llamada auto3 de la clase Autos """
auto3 = Autos("Audi","naranja",float(0.3))

""" ahora motrar la interface de los métodos """
#auto1.show()
#auto3.full_inf()
print(auto1.final_price()) # != print(auto1.final_price)
print(auto2.final_price())
print(auto3.final_price(), "\n")

""" Instance variable, este nuevo valor solo va a afectar a la instancia y en auto2._dict_ 
encontraremos esta nueva variable junto con la de marca, color y precio """
auto2.price_of_cars = 4000
print(auto1.final_price()) # != print(auto1.final_price)
print(auto2.final_price())
print(auto3.final_price())

