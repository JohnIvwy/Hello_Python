# ---------------------------------------------------------------------------------
# ------------------------------- CLASES Y OBJETOS --------------------------------
# ---------------------------------------------------------------------------------

# "self" nos permite acceder a los atributos y métodos de la misma clase

class Cellphone():

    # Atributos / Propiedades con constructor __init__
    # El constructor __init__ permite definir los atributos de una clase
    def __init__(self, bra, mod, qua):
        self.welcome = 'Hello Champion'
        # Para encapsular un atributo utilizamos '__' antes del nombre
        self.__branch = bra
        self.__model = mod
        self.__quantity = qua
        self.__available = True


    # Métodos SETs y GETs
    def get_branch(self):
        return self.__branch
    
    def get_model(self):
        return self.__model
    
    def get_quantity(self):
        return self.__quantity
    
    def set_quantity(self, qua):
        self.__quantity = qua


    # Métodos / Funciones
    # Para encapsular una función utilizamos '__' antes del nombre
    def __is_available(self):
        if(self.__quantity > 0):
            self.__available = True
        else:
            self.__available = False

    def comprar(self, qua):
        self.__is_available()
        if(self.__available and (qua <= self.__quantity)):
            self.__quantity = self.__quantity - qua
            print(f'Cantidad restante {self.__quantity}')
        else:
            print(f'Compra imposible: Cantidad disponible {self.__quantity}')

    def info(self):
        info = {'Branch': self.__branch, 'Model': self.__model, 'Quantity': self.__quantity}
        return info

    # Metodo para definir que mostrar cuando se llama solo al objeto sin definir nada mas
    # y que sea entendible al usuario (ejm: print(objeto) imprimir los atributos puede ser)
    def __str__(self):
        message = f'Cellphone: \nMarca: {self.__branch} \nModelo: {self.__model} \nCantidad: {self.__quantity}'
        return message

# ------------------------------------------------------------------------

# Iniciamos nuestro Objeto / Instancia
moto_edge_fusion = Cellphone('Motorola', 'Edge 50 Fusion', 3)

# Accedemos a sus atributos
moto_edge_fusion.welcome = 'Hello my Bro'
print(moto_edge_fusion.welcome)

# Accedemos a sus métodos
print(moto_edge_fusion.get_branch())
print(moto_edge_fusion.get_model())

moto_edge_fusion.set_quantity(7)
moto_edge_fusion.comprar(10)

# Al acceder al objeto sin especificar nada se ejecuta el método __str__
print(moto_edge_fusion)

# ------------------------------------------------------------------------


# HERENCIA
# Creamos una nueva clase y como parámetro colocamos la clase Padre
# esto nos permite heredar todos los atributos y métodos de la clase padre
class Computer(Cellphone):

    # Para poder heredar y definir nuevos atributos usamos la funcion 
    # 'super()' para heredar el constructor de la clase padre
    def __init__(self, bra, mod, qua, siz):
        super().__init__(bra, mod, qua)
        self.size = siz

    # Para sobrescribir un método de la clase padre y añadirle algo usamos 'super()'
    # como si copiaramos la funcion padre y la pegaramos en la linea de super...
    def info(self):
        info_p = super().info()
        info_p['Size'] = self.size
        return info_p



asus_vivobook = Computer('Asus', 'Vivobook mk14', 5, '14 inch')
print(asus_vivobook.welcome)

print(asus_vivobook.size)
print(asus_vivobook.info())
