# -------------------------- Collection of practical exercises in Python --------------------------

# ---------- Lesson: lists ----------

# Crea una lista con 10 números y muestra el mayor y el menor.
lst = [1,2,3,4,5,6,7,8,9,0]
print(min(lst))
print(max(lst))

# Elimina los duplicados de una lista.
lst_two = ['a','b','c','d','a','c']
sn_dup = list(set(lst_two))
print(sn_dup)

# Invierte una lista sin usar .reverse().
lst_reverse = lst[::-1]
print(lst_reverse)

# Cuenta cuántas veces aparece un número en una lista.
print(lst_two.count('a'))

# Une dos listas en una sola sin usar +.
lst_two.extend(lst)
print(lst_two)

# Suma todos los elementos de una lista usando un bucle.
total_sum = 0
for i in lst:
    total_sum += i
print(total_sum)

# Crea una lista de cuadrados de los primeros 20 números.
squares = []
for i in range(20):
    squares.append(i**2)

print(squares)

# Filtra los números pares de una lista.
even_numbers = []
for i in lst:
    if (i%2) == 0:
        even_numbers.append(i)

print(even_numbers)

# Reemplaza todos los números negativos de una lista por 0.
negative_list = [-1, 3, 6, -4, -8, 9, -3, -6, 8, 1]
for i in range(len(negative_list)):
    if negative_list[i] < 0:
        negative_list[i] = 0
print(negative_list)

# Ordena una lista sin usar sort().
new_list = [4, 2, -1, 6, 9, -6, -23, 12, -5, 83]

for i in range(len(new_list)):
    for j in range(len(new_list) - 1):
        if new_list[j] > new_list[j + 1]:
            new_list[j], new_list[j + 1] = new_list[j + 1], new_list[j]

print(new_list)
