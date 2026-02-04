# -----------------------------------------------------------------------------------------------------
# ---------------------------------------- Principios SOLID -------------------------------------------
# -----------------------------------------------------------------------------------------------------

# Son 5 principios que nos ayudan a crear código más limpio, mantenible y fácil de escalar.

# -----------------------------------------------------------------------------------------------------

# Principio #2: O - Open / Closed Principle (OCP)

# Abierto a extensión / cerrado a modificación
# Poder añadir nuevas funcionalidades sin tener que modificar nuestro código existente 

'''EXTRA'''

'''
EJERCICIO:
    Explora el "Principio SOLID Abierto-Cerrado (Open-Close Principle, OCP)"
    y crea un ejemplo simple donde se muestre su funcionamiento
    de forma correcta e incorrecta.

DIFICULTAD EXTRA (opcional):
    Desarrolla una calculadora que necesita realizar diversas operaciones matemáticas.
Requisitos:
    - Debes diseñar un sistema que permita agregar nuevas operaciones utilizando el OCP.
Instrucciones:
    1. Implementa las operaciones de suma, resta, multiplicación y división.
    2. Comprueba que el sistema funciona.
    3. Agrega una quinta operación para calcular potencias.
    4. Comprueba que se cumple el OCP.
'''

from abc import ABC, abstractmethod

class Operation(ABC):
    @abstractmethod
    def execute(self, a, b):
        pass


class Addition(Operation):
    def execute(self, a, b):
        return a + b


class Substration(Operation):
    def execute(self, a, b):
        return a - b


class Multiplication(Operation):
    def execute(self, a, b):
        return a * b


class Division(Operation):
    def execute(self, a, b):
        return a / b


class Power(Operation):
    def execute(self, a, b):
        return a ** b


class Calculator:
    def __init__(self) -> None:
        self.operations = {}

    def add_operation(self, name, operation):
        self.operations[name] = operation

    def calculate(self, name, a, b):
        if name not in self.operations:
            raise ValueError(f"La operación {name} no está soportada.")
        return self.operations[name].execute(a, b)


calculator = Calculator()
calculator.add_operation("addition", Addition())
calculator.add_operation("substration", Substration())
calculator.add_operation("multiplication", Multiplication())
calculator.add_operation("division", Division())
calculator.add_operation("power", Power())

print(calculator.calculate("addition", 10, 5))
print(calculator.calculate("substration", 10, 5))
print(calculator.calculate("multiplication", 10, 5))
print(calculator.calculate("division", 10, 5))
print(calculator.calculate("power", 10, 5))
