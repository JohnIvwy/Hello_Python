# -------------------------- Collection of practical exercises in Python --------------------------
#
# ---------- Lesson: dicts ----------

# Crea un diccionario con 5 estudiantes y sus notas.
students = {'Carlos': 3.4, 'Esteban': 7.0, 'Andrea': 10, 'Edwin': 4.3, 'Ana': 8.9}
print(students)

# Agrega un nuevo par clave-valor.
students['Melisa'] = 3.3
print(students)

# Elimina un elemento del diccionario.
students.pop('Carlos')
print(students)

print(students.popitem())
print(students)

del students['Ana']
print(students)

# Recorre el diccionario mostrando clave y valor.
for student, grade in students.items():
    print(f'Key: {student}, Value: {grade}')

# Verifica si una clave existe en el diccionario.
print('Diana' in students)

# Obtén solo las claves de un diccionario.
keys = list(students.keys())
print(keys)

# Obtén solo los valores de un diccionario.
values = list(students.values())
print(values)

# Actualiza el valor de una clave existente.
students['Andrea'] = 9.9
print(students)

# Combina dos diccionarios.
teachers = {'Javier': 'Edu. Física', 'Carmen': 'Matemáticas'}

combined = teachers | students
print(combined)
# or...
teachers.update(students)
print(teachers)

# Crea un diccionario que cuente cuántas veces aparece cada letra en una palabra.
counter = {}
word = 'dermatología'
for letter in word:
    if letter in counter:
        counter[letter] += 1
    else:
        counter[letter] = 1

print(counter)

from collections import Counter
counter = Counter(word)
print(counter)
