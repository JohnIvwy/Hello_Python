'''This file is to practice my knowledge by Python'''

### Modules ###
# Meaning: A module is a file containing a set of codes or a 
# set of functions which can be included to an application.

# To declarare:
# We can import the all module
import math # Or a file from our project. Ej: import tips_and_tricks

print(math.pi)

# We can import a specific element of module or several
from math import pi

print(pi)

# We can give a nickname to use it
from math import pi as PI_VALUE

# print(pi) -> pi is not defined
print(PI_VALUE)

# It is also possible to import multiple functions at once

from math import pi, sqrt, pow, floor, ceil, log10

print(pi)                 # 3.141592653589793
print(sqrt(2))            # 1.4142135623730951
print(pow(2, 3))          # 8.0
print(floor(9.81))        # 9
print(ceil(9.81))         # 10
print(math.log10(100))    # 2

# But if we want to import all the function in math module we can use * .

from math import *

print(pi)                  # 3.141592653589793, pi constant
print(sqrt(2))             # 1.4142135623730951, square root
print(pow(2, 3))           # 8.0, exponential
print(floor(9.81))         # 9, rounding to the lowest
print(ceil(9.81))          # 10, rounding to the highest
print(math.log10(100))     # 2

# ---------------------------------------
# -------------- Exercises --------------
# ---------------------------------------
# 1-) Escriba una función que genere un random_user_id de seis dígitos/caracteres
import string as s
import random as r

def random_user_id():
    id_user = ""
    all_elm = s.ascii_lowercase + s.digits
    for i in range(6):
        id_user += r.choice(all_elm)
    return id_user

print(random_user_id())

# Solution chat GPT
import random
import string

def random_user_id():
    caracteres = string.ascii_letters + string.digits  # letras mayúsculas, minúsculas y números
    user_id = ''.join(random.choices(caracteres, k=6)) # elige 6 al azar y los une
    return user_id

# Ejemplo de uso
print(random_user_id())


# 2-) Declare una función llamada user_id_gen_by_user. No acepta parámetros, 
# pero acepta dos entradas mediante input(). Una de las entradas es el número 
# de caracteres y la otra, el número de ID que se generarán.

def user_id_gen_by_user():
    try:
        num_chars = int(input('Number of chars: ')) # Numero de caracteres
        num_ids = int(input('Number of ids: ')) # Numero de ids que se generan

        for i in range(num_ids):
            caracteres = string.ascii_letters + string.digits  # letras mayúsculas, minúsculas y números
            user_id = ''.join(random.choices(caracteres, k=num_chars)) # elige 6 al azar y los une
            print(user_id)
    
    except Exception as e:
        print(e)

user_id_gen_by_user()

# 3-) Write a function named rgb_color_gen. 
# It will generate rgb colors (3 values ranging from 0 to 255 each).
import random
def rgb_color_gen():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    return f'rgb({r},{g},{b})'

def rgb_colors(n):
    return [rgb_color_gen() for _ in range(n)]

print(rgb_color_gen())
[print(rgb_colors(3)) for _ in range(2)]

# 4-) Call your function shuffle_list, it takes a list as a parameter and it returns a shuffled list
import random

def shuffle_list(lst):
    random.shuffle(lst)
    return lst

print(shuffle_list([1,2,3,4,5,6,7,8,9,0]))

# 5-) Write a function which returns an array of seven 
# random numbers in a range of 0-9. All the numbers must be unique.
import random

def seven_random_array():
    array_random = random.sample(range(9),k=7)
    return array_random

print(seven_random_array())
