# -------------------------- Collection of practical exercises in Python --------------------------

# ---------- Lesson: functions ----------

# Crea una función que sume dos números.
def sum_two_numbers(num_one, num_two):
    return num_one + num_two

print(sum_two_numbers(2, 3))

# Función que calcule el área de un círculo.
from math import pi
def area_circle(radio):
    return pi * (radio ** 2)

print(area_circle(2))

# Función que devuelva el mayor de tres números.
def largest_number(one_num, two_num, three_num):
    return max(one_num,two_num,three_num)

a, b, c = 8, 3, 4
print(largest_number(a,b,c))

# Función que invierta una cadena.
def inverted_chain(chain):
    return chain[::-1]

print(inverted_chain('Experimetado'))

# The correct way to solve it
def revers_text(text):
    
    len_text = len(text)
    text_reversed = ''
    
    for i in range(len_text):
        text_reversed += text[len_text - i - 1]
        return text_reversed

print(revers_text('Hola mundo'))

# Función que verifique si un número es primo.
# Intente realizar la función pero no funciono
"""def is_prime(number):
    prime_number = [1, 2, 3, 5, 7]
    a = False

    for i in prime_number[2:5]:
        print(i)
        if number == i:
            return f'The number {number} is prime'
        elif (number % i) == 0:
             return f'The number {number} is not prime'
        else:
            a = True

    if a:
        return f'The number {number} is prime'
    
print(is_prime(49))"""

# Solución IA
def es_primo(numero):
    if numero <= 1:
        return False
    for i in range(2, int(numero**0.5) + 1):  # solo hasta la raíz cuadrada
        if numero % i == 0:
            return False
    return True

# Ejemplos de uso
print(es_primo(2))   # True
print(es_primo(17))  # True
print(es_primo(20))  # False

# Solución MoureDev
def is_prime(number):
    
    if number <= 1:
        return False

    for i in range(2, number):
        if number % i == 0:
            return False
        
    return True

print(is_prime(7))

# Función que cuente palabras en una frase.
def count_words(frase):
    words = 0
    in_word = False  # indica si estamos dentro de una palabra

    for i in frase:
        if i != ' ' and not in_word:
            # inicio de una palabra
            words += 1
            in_word = True
        elif i == ' ':
            # estamos en un espacio, salimos de la palabra
            in_word = False

    return words


# Ejemplos de uso
print(count_words("Esta es mi frase de prueba"))   # 6

# Función integrada del sistema
def count_words_IA(frase):
    return len(frase.split())

print(count_words_IA('Esta es mi frase de prueba'))  # 6
print(count_words_IA('  Hola   mundo  '))            # 2

# Función que genere la secuencia Fibonacci hasta n.
def fibonacci(max_value):
    sequence = [0, 1]
    while sequence[-1] + sequence[-2] <= max_value:
        sequence.append(sequence[-1] + sequence[-2])
    return sequence

print(fibonacci(150))

# Función que reciba una lista y devuelva el promedio.
def average(lista):
    total = 0
    for number in lista:
        total += number
    return total / len(lista)

print(average([1,5,9,2,4]))
