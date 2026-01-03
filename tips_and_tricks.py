# -------------- RANGE --------------
# range() se usa para generar una secuencia de números.
# range(inicio, fin, salto)
# - inicio: desde dónde empieza (opcional, por defecto 0)
# - fin: hasta dónde llega (obligatorio, no se incluye)
# - salto: de cuánto en cuánto avanza (opcional, por defecto 1)

rg = list(range(0, 20, 3))
print(rg)  # [0, 3, 6, 9, 12, 15, 18]


# -------------- PASS --------------
# pass se usa cuando Python exige una instrucción,
# pero no queremos que haga nada por ahora.
# Sirve como "relleno" para evitar errores.

for number in range(6):
    pass  # no hace nada


# -------------- [::-1] --------------
# Esta forma sirve para invertir una lista.
# [inicio:fin:paso] → con -1 recorremos la lista al revés

lst = ['primero', 'segundo', 'tercero', 'cuarto']
lst = lst[::-1]
print(lst)
# ['cuarto', 'tercero', 'segundo', 'primero']


# -------------- Empaquetado de argumentos (*args) --------------
# *args permite recibir muchos argumentos sin saber cuántos serán.
# Todos los valores se guardan como una tupla.

def sum_all(*args):
    total = 0
    for i in args:
        total += i
    return total

print(sum_all(1, 2, 3))              # 6
print(sum_all(1, 2, 3, 4, 5, 6, 7))   # 28


# -------------- Desempaquetado de argumentos (*) --------------
# Permite enviar una lista o tupla como argumentos separados.

def sum_of_five_nums(a, b, c, d, e):
    return a + b + c + d + e

lst = [1, 2, 3, 4, 5]
print(sum_of_five_nums(*lst))  # 15


# También se puede usar para asignar valores de una lista:
countries = ['Finland', 'Sweden', 'Norway', 'Denmark', 'Iceland']
fin, sw, nor, *rest = countries
print(fin, sw, nor, rest)
# Finland Sweden Norway ['Denmark', 'Iceland']

numbers = [1, 2, 3, 4, 5, 6, 7]
one, *middle, last = numbers
print(one, middle, last)
# 1 [2, 3, 4, 5, 6] 7


# -------------- Propagación (*) --------------
# El operador * permite unir listas fácilmente.

lst_one = [1, 2, 3]
lst_two = [4, 5, 6, 7]
lst = [0, *lst_one, *lst_two]
print(lst)
# [0, 1, 2, 3, 4, 5, 6, 7]


# -------------- JOIN --------------
# join() une una lista de strings en un solo string.
# El texto antes del .join() es el separador.

palabras = ["Hola", "mundo", "Python"]
resultado = " ".join(palabras)
print(resultado)
# Hola mundo Python
