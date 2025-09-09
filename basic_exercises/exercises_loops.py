# -------------------------- Collection of practical exercises in Python --------------------------

# ---------- Lesson: conditionals ----------

# Imprime los números del 1 al 100 con un for.
for i in range(1, 101):
    print(i)

# Imprime los múltiplos de 3 entre 1 y 50.
multiples_three = [i for i in range(1, 51) if i % 3 == 0]
print(multiples_three)

# Suma los números del 1 al 50.
suma = sum(range(1, 51))
print(suma)

# Crea una tabla de multiplicar de un número dado.
number = 7
for i in range(1, 13):
    print(f'{number} x {i} = {number * i}')

# Recorre una lista de nombres e imprímelos en mayúsculas.
names = ['John', 'Lean', 'Luisa']
for name in names:
    print(name.upper())

# Encuentra el factorial de un número.
number = 5
factorial = 1
for i in range(1, number+1):
    factorial *= i
print(factorial)

# Cuenta cuántas vocales hay en una palabra.
word = 'irreverencia'
amount_vowels = sum(1 for i in word.lower() if i in 'aeiou')
print(f'La palabra "{word}" tiene {amount_vowels} vocales')

# Imprime un triángulo de asteriscos con for.
height = 5
for i in range(1, height+1):
    print('*' * i)

# Busca un número en una lista (con break).
nums = [1, 2, 4, 6, 8, 7, 3, 9]
for i in nums:
    if i == 8:
        print('Existe, número encontrado')
        break
