from enum import Enum

class Person(Enum):
    name = 'John'
    lastname = 'Leon'

# Para acceder al valor de los atributos utilizamos .value
print(Person.name.value) # Salida: John

# Podemos obtener el nombre de un atributo si tenemos su valor
print(Person('John')) # Salida: Person.name

# Para recorrer los atributos de la clase utilizamos una list comprehension
atributos_person = [i for i in Person]

print(atributos_person[1])

for i in atributos_person:
    print(i.value)