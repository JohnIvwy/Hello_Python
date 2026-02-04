# -----------------------------------------------------------------------------------------------------
# ---------------------------------------- Principios SOLID -------------------------------------------
# -----------------------------------------------------------------------------------------------------

# Son 5 principios que nos ayudan a crear código más limpio, mantenible y fácil de escalar.

# -----------------------------------------------------------------------------------------------------

# Principio #3: L - Liskov Substitution Principle (LSP)

# Las subclases deben poder reemplazar a la clase padre sin romper nada

'''EXTRA'''

'''
EJERCICIO:
    Explora el "Principio SOLID de Sustitución de Liskov (Liskov Substitution Principle, LSP)"
    y crea un ejemplo simple donde se muestre su funcionamiento
    de forma correcta e incorrecta.

DIFICULTAD EXTRA (opcional):
    Crea una jerarquía de vehículos. Todos ellos deben poder acelerar y frenar, así como
    cumplir el LSP.
Instrucciones:
    1. Crea la clase Vehículo.
    2. Añade tres subclases de Vehículo.
    3. Implementa las operaciones "acelerar" y "frenar" como corresponda.
    4. Desarrolla un código que compruebe que se cumple el LSP.
'''

class Vehicle:

    def __init__(self, speed=0):
        self.speed = speed

    def accelerate(self, increment):
        self.speed += increment
        print(f"Velocidad: {self.speed} Km/h")

    def brake(self, decrement):
        self.speed -= decrement
        if self.speed <= 0:
            self.speed = 0
        print(f"Velocidad: {self.speed} Km/h")


class Car(Vehicle):
    def accelerate(self, increment):
        print("El coche está acelerando")
        super().accelerate(increment)

    def brake(self, decrement):
        print("El coche está frenando")
        super().brake(decrement)


class Bicycle(Vehicle):
    def accelerate(self, increment):
        print("La bicicleta está acelerando")
        super().accelerate(increment)

    def brake(self, decrement):
        print("La bicicleta está frenando")
        super().brake(decrement)


class Motorcycle(Vehicle):
    def accelerate(self, increment):
        print("La moto está acelerando")
        super().accelerate(increment)

    def brake(self, decrement):
        print("La moto está frenando")
        super().brake(decrement)


def test_vehicle(vehicle):
    vehicle.accelerate(2)
    vehicle.brake(1)


car = Car()
bicycle = Bicycle()
motorcycle = Motorcycle()

test_vehicle(car)
test_vehicle(bicycle)
test_vehicle(motorcycle)
