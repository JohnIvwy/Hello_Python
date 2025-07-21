'''This file is to practice my knowledge by Python'''

# To create a Tuple
my_tuple = ()
tuple_two = tuple()

my_tuple = (1,2,3,4)
tuple_two = (5,6,7,8) 

my_tuple += tuple_two
print(type(my_tuple))

'''Nota importante: aunque las tuplas son inmutables
(no se pueden modificar en el sentido tradicional),
la operación += no modifica la tupla original,
sino que crea una nueva y reasigna el nombre my_tuple a ella.'''

# Exercises on the GitHub
name_sister = ('Diana','Ana')
names_brothers = ('Alex','Pedro')
siblings = names_brothers + name_sister
print(siblings)
parents = ('Amilcar','Johana')
family_members = parents + siblings
print(family_members)
print(f'Cantidad de hermanos: {len(siblings)}')
dad, mom, hno_mayor, hno_inter, hna_good, couple = family_members
print(dad, mom, hna_good)
print('Pedro' in family_members)
