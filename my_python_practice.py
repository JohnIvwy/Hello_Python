'''This file is to practice my knowledge by Python'''

### Functions ###
def name_function():
    print('Code of function')

name_function() # there we call the function


# Function with parameters and return

def sum_two_values(first_value, second_value):
    sum = first_value + second_value
    return(sum) # we can return a value with the function

result = sum_two_values(3,5)
print(f'"return" of function is {result}')

# We can specify the sort of items

result_2 = sum_two_values(second_value=2, first_value=4)
print(result_2)


# We can put a value by default to the function

def fun_default(name='N/N', nickname='Sin nickname'):
    print(f'User: {name}, {nickname}')

fun_default() # Don´t put the parameter

# RETURN
def is_even (n):
    if n % 2 == 0:
        print('even')
        return True    # return stops further execution of the function, similar to break 
    return False
print(is_even(10)) # True
print(is_even(7)) # False



# ---------------------------------------
# -------------- Exercises --------------
# ---------------------------------------
# 1-) 
def convert_celsius_to_fahrenheit(celsius):
    fahrenheit = (celsius * (9/5)) + 32
    return fahrenheit

grados = convert_celsius_to_fahrenheit(3)
print(f'3 °C corresponde a {grados} Fahrenheit')

# 2-)
def check_season(month):
    if month == 'January':
        print('Autumn')
    elif month == 'February':
        print('Winter')
    elif month == 'March':
        print('Spring')
    else:
        print('Summer')

check_season('March')

# 3-)
def print_list(els):
    for el in els:
        print(el)

lst = [12,'Hola',12.23,True]
print_list(lst)

# 4-)
def reverse_list(lst):
    return lst[::-1]

print(reverse_list([1,2,3,4,5,6]))

# 5-)
def capitalize_list_items(lista):
    lst = []
    for item in lista:
        lst.append(item.capitalize())
    return lst
lista = ['john','andrea','marco','thony']
print(capitalize_list_items(lista))

# 6-)
def remove_item(lst,item):
    if item in lst:
        lst.remove(item)
        return lst
    else:
        return 'The item is not in the list'

print(remove_item([35, 1.77, "Brais", "Moure"], 'Bras'))
