''' This is my file for practicing my knowledge in the fundamental course.'''

# ---------------------------------------------------------------------------
# ---------------------------- LEVEL ONE ------------------------------------
# ---------------------------------------------------------------------------

name = 'John Leon'
age = 22
language = 'Python'

print(f'Hello and welcome!')
print(f'My name is {name}, I am {age} years old, my favorite languge is {language}')


# Function to print the sum of two values

def sum_two_numbers():
    num_one = int(input('Enter number one'))
    num_two = int(input('Enter number two'))
    return num_one + num_two

print(sum_two_numbers(2, 3))


# Function to identify the number

def identify(value):
    if(value < 0):
        print(f'The value {value} is negative')
    elif(value > 0):
        print(f'The value {value} is positive')
    elif(value == 0):
        print(f'The value {value} is cero')
    else:
        print('The number is incorrect')

identify(10)


# While

i = 0
digits = []

while(i < 10):
    digits.append(i)
    i += 1
print(digits)

# For

lst_to_15 = []

for i in range(-15,1):
    lst_to_15.append(i)
print(lst_to_15)

# Multiply table

number = 7

for i in range(1, 11):
    print(f'{number} x {i} = {number*i}')

# Exceptions

try:
    print('2'*2)
except:
    print('Fatal error')



# ---------------------------------------------------------------------------
# ---------------------------- LEVEL TWO ------------------------------------
# ---------------------------------------------------------------------------

lista = [1,2,3,4,5]
for value in lista:
    print(value)

print(sum(lista))

frutas = ['Apple', 'Pineapple', 'Orange', 'Strawberry', 'coconut']
print(len(frutas))

for fruta in frutas:
    print(fruta.upper())

print(min(lista))
print(max(lista))

list_reps = [1,2,3,9,3,2,1,8,3,1,2,4,7,8,6,4,5,4]
st = set(list_reps)
print(st)

diccionario = {'nombre': 'John', 'edad': 22, 'ciudad':'La Calera'}
print(diccionario.items())

for i in st:
    if (i % 2 == 0):
        print(i)



# ---------------------------------------------------------------------------
# --------------------------- LEVEL THREE -----------------------------------
# ---------------------------------------------------------------------------

