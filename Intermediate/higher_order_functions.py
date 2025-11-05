'''This file is to practice my knowledge by Python'''

### Higher Order Functions ###

# Function as a parameter
from functools import reduce


def multiply_two_nums(first_num, second_num):
    return first_num * second_num

def area_triangle(function, lst):
    return function(lst[0],lst[1])/2

triangle = area_triangle(multiply_two_nums,[2,4])
print(triangle)



# Function as a Return Value
def square(x):          # a square function
    return x ** 2

def cube(x):            # a cube function
    return x ** 3

def absolute(x):        # an absolute value function
    if x >= 0:
        return x
    else:
        return -(x)

def higher_order_function(type): # a higher order function returning a function
    if type == 'square':
        return square
    elif type == 'cube':
        return cube
    elif type == 'absolute':
        return absolute

result = higher_order_function('square')
print(result(3))       # 9
result = higher_order_function('cube')
print(result(3))       # 27
result = higher_order_function('absolute')
print(result(-3))      # 3



# Python Closures

def add_ten():
    ten = 10
    def add(num):
        return num + ten
    return add

closure_result = add_ten()
print(closure_result(5))  # 15
print(closure_result(10))  # 20



# Python Decorators

'''This decorator function is a higher order function
that takes a function as a parameter'''

def uppercase_decorator(function):
    def wrapper():
        func = function()
        make_uppercase = func.upper()
        return make_uppercase
    return wrapper
@uppercase_decorator
def greeting():
    return 'Welcome to Python'
print(greeting())   # WELCOME TO PYTHON



'''These decorator functions are higher order functions
that take functions as parameters'''

# First Decorator
def uppercase_decorator(function):
    def wrapper():
        func = function()
        make_uppercase = func.upper()
        return make_uppercase
    return wrapper

# Second decorator
def split_string_decorator(function):
    def wrapper():
        func = function()
        splitted_string = func.split()
        return splitted_string

    return wrapper

@split_string_decorator
@uppercase_decorator     # order with decorators is important in this case - .upper() function does not work with lists
def greeting():
    return 'Welcome to Python'
print(greeting())   # WELCOME TO PYTHON


# Accepting Parameters in Decorator Functions

def decorator_with_parameters(function):
    def wrapper_accepting_parameters(para1, para2, para3):
        function(para1, para2, para3)
        print("I live in {}".format(para3))
    return wrapper_accepting_parameters

@decorator_with_parameters
def print_full_name(first_name, last_name, country):
    print("I am {} {}. I love to teach.".format(
        first_name, last_name, country))

print_full_name("Asabeneh", "Yetayeh",'Finland')


# -------------------------------------------------------
# ---------------------- Exercises ----------------------

countries = ['Estonia', 'Finland', 'Sweden', 'Denmark', 'Norway', 'Iceland']
names = ['Asabeneh', 'Lidiya', 'Ermias', 'Abraham']
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, -19]

# Use map to create a new list by changing each country to uppercase in the countries list
print(list(map(lambda i: i.upper(), countries)))

# Use map to create a new list by changing each number to its square in the numbers list
print(list(map(lambda x: x ** 2, numbers)))

# Use filter to filter out countries containing 'land'.
print(list(filter(lambda i: 'land' in i, countries)))

# Use filter to filter out countries having exactly six characters.
print(list(filter(lambda x: len(x) == 6, countries)))

# Use filter to filter out countries starting with an 'E'
print(list(filter(lambda i: i[0] == 'E', countries)))

# Chain two or more list iterators (eg. arr.map(callback).filter(callback).reduce(callback))
print(list(reduce(
    lambda a, b: a + b, 
    filter(
        lambda x: x > 2, 
        map(lambda i: i * 3, numbers)))))

# Declare a function called get_string_lists which takes a list as a parameter and then returns a list containing only string items.
# Use reduce to sum all the numbers in the numbers list.
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

from functools import reduce

result = reduce(
    lambda acc, x: acc + x,
    filter(
        lambda x: x > 20,
        map(lambda x: x ** 2, numbers)
    )
)
print(result)  # 355
