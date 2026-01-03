''' This is my file for practicing my knowledge in the intermediate course.'''

# FILTER
edades = [21, 32, 12, 4, 53, 27, 69, 10, 3]

mayores = list(filter( lambda x : x > 18 , edades))

print(mayores)

# MAP
digits = [1,2,3,4,5,6,7,8,9,0]
pw = list(map(lambda i: pow(i,2), digits))
print(pw)

# List Comprehension

print([i for i in range(10)])

numeros = [1, 2, 3, 4, 5]
print([i*2 for i in numeros])

palabras = ["hola", "python", "lista"]
print([palabra.upper() for palabra in palabras])

print([i for i in range(20) if i % 2 == 0 ])

numeros = [3, -1, 4, -2, 0, -5]
print([i if i > 0 else 0 for i in numeros])

palabras = ["python", "es", "genial"]
print([len(p) for p in palabras])

palabra = "list comprehension"
print([b for b in palabra if b in 'aeiou'])

print([(x,x**2) for x in range(6)])

matriz = [[1, 2], [3, 4], [5, 6]]
print([n for l in matriz for n in l])

print(['par' if n % 2 == 0 else 'impar' for n in range(10)])