# -------------------------- Collection of practical exercises in Python --------------------------

# ---------- Lesson: sets ----------

# Crea un set de números y elimina duplicados automáticamente.
numbers = {5,2,67,34,1,6,2,67}
print(numbers)

# Comprueba si un elemento pertenece a un set.
print(3 in numbers)

# Encuentra la unión de dos sets.
more_nums = {3,4,7,34,9,8,1,12}
union = more_nums.union(numbers)
print(union)

# Encuentra la intersección de dos sets.
intersection = numbers.intersection(more_nums)
print(intersection)

# Encuentra la diferencia entre dos sets.
difference = more_nums.difference(numbers)
print(difference)

# Crea un set y agrega un nuevo elemento.
colors = {'Green','Blue','Orange','Purple','Rose','Violet'}
colors.add('Gray')
print(colors)

# Elimina un elemento de un set con remove() y con discard().
numbers.remove(67)
numbers.discard(34)
print(numbers)

numbers.discard(999)  # No lanza error
# numbers.remove(999)  # Esto daría error

# Comprueba si dos sets son disjuntos.
print(numbers.isdisjoint(more_nums))

# Convierte una lista con elementos repetidos en un set.
elements = ['glasses','bottle','mouse','speaker','bottle','door','curtain','pen','eraser','door']
elem_set = set(elements)
print(elem_set)
