'''This file is to practice my knowledge by Python'''

# To create a Dict
# syntax
dictionary = dict()
empty_dict = {}

# Exercises from GitHub

dog = {'name':'Max', 'color':'Yellow and brown', 'legs':4,'age':'I dont know'} # Declarando dog as a Dict

# Declarando student as a Dict
student = {
    'first_name':'Andrea',
    'last_name':'Useche',
    'gender':'Female',
    'age':19,
    'status':'Engagement',
    'skills':['Beautiful','Intelligence','Fashion'],
    'country':'Colombia',
    'city':'Bogota D.C',
    'address':{
        'street':'Calle 12 #2-32',
        'neighborhood':'Prado'
    }}

# Accediendo al index 2 del valor de la llave 'skills'
print(student['skills'][2])

# Añadiendo 3 elementos a la lista de la llave 'skills'
student['skills'].extend(['Sort','Intelectual','Responsable'])
print(student['skills'])

# Getting the values of dictionary as a list
list_of_dict = list(student.values())
print(list_of_dict)

# Change the dictionary to a list of tuples using items() method
lst_tpl_dct = list(student.items())
print(len(lst_tpl_dct))
print(lst_tpl_dct[5][1][2])

# Deleting one element of dict
del student['country']
student['status'] = 'Single'
print(student)

# Dropping all the dictionary
del dog
