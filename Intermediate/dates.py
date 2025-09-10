'''This file is to practice my knowledge by Python'''

### Dates ###

from datetime import datetime # fecha y hora juntos

# Meaning: Librería o modulo de fechas (día, mes, año, hora...)

now = datetime.now()
print(now.time())
print(f'Fecha: {now.year}/{now.month}/{now.day} or.... {now.date()}')
print(f'Hora: {now.hour}/{now.minute}/{now.second} or.... {now.time()}')


# Timestamp: es una secuencia de caracteres que registra la fecha y hora 
# exactas en que ocurrió un evento.

timestamp = now.timestamp()
print(f'Timestamp: {timestamp}')

# Definir una fecha con hora:
my_first_love = datetime(2024, 6, 15, 5, 39, 42)
print(my_first_love)




from datetime import date, time # fecha y hora por separado

print(date.today()) # Fecha actual

# Definir solo la fecha
fecha = date(2023, 5, 7)
print(fecha)

# Definir solo la hora

hora = time(12, 30, 54)
print(hora)


# Exercise
# Calculate the time difference between now and new year.
current_date = datetime.now()
miss_sofi = date(2023, 5, 7)
print(current_date.date() - miss_sofi)
