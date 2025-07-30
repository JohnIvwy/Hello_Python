'''This file is to practice my knowledge by Python'''

### Loops ###

# While
'''a = 0
while a < 10:
    print('While condition is True, the loop execute again')
    a += 1
    print(a)
    if a == 7:
        print('To stop the loop use Break')
        break # El 'Break' rompe el bucle y se deja de ejecutar
else: # Es opcional
    print('else -> Se ejecuta cuando termina el bucle')



# For
# Para iterar un listado de elementos
for i in range(10):
    print(i)
    if i == 6:
        print('To stop the loop use Break')
        break # El 'Break' rompe el bucle y se deja de ejecutar
else: # Es opcional
    print('else -> Se ejecuta cuando termina el bucle')

language = 'Python'
for i in range(len(language)):
    print(language[i])

person = {
    'first_name':'Asabeneh',
    'last_name':'Yetayeh',
    'age':250,
    'country':'Finland',
    'is_marred':True,
    'skills':['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
    'address':{
        'street':'Space street',
        'zipcode':'02210'
    }
}
for key, value in person.items():
    print(key, value) # this way we get both keys and values printed out

for key in person:
    if key == 'skills':
        for skill in person['skills']:
            print(skill)'''

# Exercises

# 1-) Iterate 10 to 0 using for loop, do the same using while loop.
i = 10
while i >= 0:
    print(i)
    i -= 1
else:
    print('End while')

rg = list(range(11))
rg.reverse()
for x in rg:
    print(x)
else:
    print('End for')

# 2-)
for i in range(1,8):
    p = '#'
    print(p*i)

# 3-)
for f in range(8):
    a = '# '
    print(a*8)

for f in range(8):
    n = '# '
    for c in range(8):
        print(n,end='')
    print('')

# 4-) 
for i in range(11):
    print(f'{i} x {i} = {i*i}')

# 5-)
suma = 0
for i in range(1,101,2):
    suma += i
print(suma)

# 6-) Invierte el orden de la lista usando un bucle.
# Lista original
frutas = ['banana', 'naranja', 'mango', 'limón']

# Usamos un bucle para invertir la lista manualmente
frutas_invertidas = []

for i in range(len(frutas) - 1, -1, -1):
    frutas_invertidas.append(frutas[i])

# Sobrescribimos la lista original
frutas = frutas_invertidas

# Mostramos el resultado
print("Lista invertida:", frutas)
