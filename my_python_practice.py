'''This file is to practice my knowledge by Python'''

### Classes ###
# Meaning: 

# To declarare:
class Person: # nombres de clases en Camelcase UnEjemploEsEste
    # __init__ constructor de la clase, permite dar valores al objeto al crearlo
    # 'self' le asigna esos valores al objeto creado y permite acceder a ellos dentro de la clase
    def __init__(self, name, age, height, gender): 
        # atributos aquí abajo y se pasan por parámetros
        self.name = name
        self.age = age
        self.height = height
        self.gender = gender

    # definimos sus métodos
    def greeting(self):
        print(f'¡Hola {self.name}!')
    
    def get_age(self):
        return self.age
    
    def prt_full_name(self):
        self.name = 'Raton'
        self.age = 32
    
    def prt_attributes(self):
        print(f'Name: {self.name}')
        print(f'Age: {self.age}')
        print(f'Height: {self.height}')
        print(f'Gender: {self.gender}')
    
# Instanciamos el objeto (lo creamos)
john = Person('John', 21, 1.70, 'Male')

# Accedemos a sus atributos y métodos si son públicos
john.greeting()
print(john.get_age())

# Child class
class Stutdent(Person):
    def __init__(self, name, age, height, gender):
        super().__init__(name, age, height, gender)
    
    def prt_full_name(self):
        super().prt_full_name()
        self.age = 64

pedro = Stutdent('pedro', 12, 1.32, 'Male')
pedro.prt_full_name()
pedro.prt_attributes()

# ---------------------------------------
# -------------- Exercises --------------
# ---------------------------------------
# 1-) 

