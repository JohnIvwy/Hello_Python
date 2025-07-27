'''This file is to practice my knowledge by Python'''

### Conditionals ###

# Basic structure to built a conditional
suma = True
if suma: # Check if the variable is 'True'
    print()
elif suma != False: # Check if the variable is difference to 'True'
    print()
else: # This part execute if anyone of the conditionals se cumple
    print()

# Exercises

# 1
age = int(input('Enter your age: '))

if age < 18:
    print(f'You need {18 - age} more years to learn to drive')
if age >= 18:
    print('You are old enough to learn to drive')

# 2
my_age = 21
your_age = int(input('Enter your age: '))

if your_age > my_age:
    difference = your_age - my_age
    if difference == 1:
        print('You are 1 year older than me')
    else:
        print(f'You are {difference} years older than me')
elif your_age < my_age:
    difference = my_age - your_age
    if difference == 1:
        print('You are 1 year younger than me')
    else:
        print(f'You are {difference} years younger than me')
else:
    print('We are the same age!')

# 3
a = int(input('Enter nombre one: '))
b = int(input('Enter nombre two: '))

if a > b:
    print(f'{a} is greater than {b}')
else:
    print(f'{a} is less than {b}')

# 4
score = int(input('Enter your score (0-100): '))

if score >= 0 and score < 50:
    print('Grade: F')
elif score >= 50 and score < 60:
    print('Grade: D')
elif score >= 60 and score < 70:
    print('Grade: C')
elif score >= 70 and score < 90:
    print('Grade: B')
elif score >= 80 and score <= 100:
    print('Grade: A')
else:
    print('Your score is incorrect!')

# 5
# If a fruit doesn't exist in the list add the fruit to the list and print the modified list. 
# If the fruit exists print('That fruit already exist in the list')
fruits = ['banana', 'orange', 'mango', 'lemon']
new_fruit = input('Enter a fruit: ')

if new_fruit in fruits:
    print('That fruit already exist in the list')
    print(f'List: {fruits}')
else:
    fruits.append(new_fruit)
    print(f'List modify: {fruits}')

# 6
person={
    'first_name': 'Asabeneh',
    'last_name': 'Yetayeh',
    'age': 250,
    'country': 'Finland',
    'is_marred': True,
    'skills': ['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
    'address': {
        'street': 'Space street',
        'zipcode': '02210'
        }
    }

if 'skills' in person:
    print(person['skills'][int(len(person['skills'])/2)])
    
if 'Python' in person['skills']:
    print('Yeah')
