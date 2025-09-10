# -------------------------- Collection of practical exercises in Python --------------------------

# ---------- Lesson: conditionals ----------

# Determina si un número es positivo, negativo o cero.
number = 6

if number > 0:
    print('Número positivo')
elif number < 0:
    print('Número negativo')
else:
    print('Igual a cero')


# Verifica si un número es par o impar.
print('Número par' if number % 2 == 0 else 'Número impar')


# Comprueba si una persona es mayor de edad (>=18).
years_old = 18
print('Mayor de edad' if years_old >= 18 else 'Menor de edad')


# Determina si una letra es vocal o consonante.
letter = 'b'
if letter.lower() in "aeiou":
    print('Vocal')
else:
    print('Consonante')


# Calcula el mayor de tres números.
a, b, c = 5, 3, 8
mayor = max(a, b, c)
print(f'El mayor es {mayor}')


# Verifica si un año es bisiesto.
year = 2020
if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print('Año bisiesto')
else:
    print('Año no bisiesto')


# Determina si una cadena es un palíndromo.
cadena = "anilina"
if cadena.lower().replace(" ", "") == cadena.lower().replace(" ", "")[::-1]:
    print('Es un palíndromo')
else:
    print('No es un palíndromo')


# Comprueba si una contraseña cumple con mínimo 8 caracteres.
password = "contraseña123"
print('Contraseña válida' if len(password) >= 8 else 'Contraseña inválida')


# Clasifica una nota (0–59 “F”, 60–79 “C”, 80–89 “B”, 90–100 “A”).
nota = 85
if 0 <= nota < 60:
    print('Nota: F')
elif 60 <= nota < 80:
    print('Nota: C')
elif 80 <= nota < 90:
    print('Nota: B')
elif 90 <= nota <= 100:
    print('Nota: A')
else:
    print('Nota inválida')


# Calcula el descuento en una compra según el monto.
monto = 120
if monto > 100:
    descuento = monto * 0.10
    total = monto - descuento
    print(f'Descuento del 10%. Total a pagar: {total}')
else:
    print('Sin descuento')
