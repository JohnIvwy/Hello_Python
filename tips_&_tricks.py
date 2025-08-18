
# -------------- RANGE --------------
# The range() function is used list of numbers. The range(start, end, step)
# takes three parameters: starting, ending and increment.
# By default it starts from 0 and the increment is 1.
# The range sequence needs at least 1 argument (end).
rg = list(range(0,20,3))
print(rg)

# -------------- PASS --------------
# In python when statement is required (after semicolon), but we don't like 
# to execute any code there, we can write the word pass to avoid errors. 
# Also we can use it as a placeholder, for future statements.
# Example:
for number in range(6):
    pass

# -------------- [::-1] --------------
# Esta expresión nos permite revertir los elementos de una lista
lst = ['primero','segundo','tercero','cuarto']
lst = lst[::-1]
print(lst) # salida: ['cuarto', 'tercero', 'segundo', 'primero']

# -------------- Empaquetado de argumentos --------------
# A veces no sabemos cuántos argumentos deben pasarse a una función de Python.
# Podemos usar el método de empaquetado para permitir que nuestra función 
# acepte un número ilimitado o arbitrario de argumentos.
def sum_all(*args):
    s = 0
    for i in args:
        s += i
    return s
print(sum_all(1, 2, 3))             # 6
print(sum_all(1, 2, 3, 4, 5, 6, 7)) # 28


# -------------- Desempaquetado de argumentos --------------
# Poder pasar una lista como argumento
def sum_of_five_nums(a, b, c, d, e):
    return a + b + c + d + e

lst = [1, 2, 3, 4, 5]
print(sum_of_five_nums(*lst))  # 15

# Una lista o una tupla también se puede descomprimir de la siguiente manera:
countries = ['Finland', 'Sweden', 'Norway', 'Denmark', 'Iceland']
fin, sw, nor, *rest = countries
print(fin, sw, nor, rest)   # Finland Sweden Norway ['Denmark', 'Iceland']
numbers = [1, 2, 3, 4, 5, 6, 7]
one, *middle, last = numbers
print(one, middle, last)      #  1 [2, 3, 4, 5, 6] 7

# -------------- Propagación en Python --------------
# Al igual que en JavaScript, la propagación es posible en Python.
lst_one = [1, 2, 3]
lst_two = [4, 5, 6, 7]
lst = [0, *lst_one, *lst_two]
print(lst)  # [0, 1, 2, 3, 4, 5, 6, 7]
