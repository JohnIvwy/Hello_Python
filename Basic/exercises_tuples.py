# -------------------------- Collection of practical exercises in Python --------------------------

# ---------- Lesson: tuples ----------

# Crea una tupla con nombres de frutas y accede al segundo y último elemento.
tpl = ('apple', 'pineapple', 'orange', 'banana', 'strawberry', 'melon')
print(tpl[1],tpl[-1])

# Convierte una lista en tupla.
lista = [1,2,3,4,5,6,7,8,9,0]
print(type(lista))
digits = tuple(lista)
print(type(digits))

# Comprueba si un elemento existe en una tupla.
print('apple' in tpl)

# Cuenta cuántas veces aparece un valor en una tupla.
print(tpl.count('orange'))

# Encuentra el índice de un elemento en una tupla.
print(digits.index(0))

# Empaca 3 variables en una tupla y desempácalas.
var_one, var_two, var_three = 'Hola','John', 22
info = (var_one, var_two, var_three)
print(info)
a, b, c = info
print(a, b, c)

# Usa una tupla como clave en un diccionario.
dct = {
    (0, 0): "origen",
    (1, 2): "punto A",
    (3, 4): "punto B"
}
print(dct)

# Concatena dos tuplas.
cont_tuples = tpl + digits
print(cont_tuples)

# Crea una tupla anidada (tupla dentro de tupla) y accede a un valor interno.
tuple_anidada = ('Greeting',('name', 'lastname'), 'question')
print(tuple_anidada[1][0])

# Escribe una función que reciba una lista y devuelva una tupla con el mínimo y el máximo.
def max_add_min(lista):
    max_min = (max(lista), min(lista))
    return max_min

print(max_add_min([1,2,3,4,5,6]))
