'''This file is to practice my knowledge by Python'''

### Exceptions Handling (Manejo de errores) ###
# Meaning: 

# To declarare:
try:
    pass # Ejecuta el código
except:
    pass # Se ejecuta si manda error
else: # Opcional
    pass # Se ejecuta si no manda error
finally: # Opcional
    pass # Se ejecuta siempre, con error o sin error


# Excepciones por tipo

try:
    pass # Ejecuta el código
except ValueError:
    pass # Se ejecuta cuando se produce un ValueError
except TypeError:
    pass # Se ejecuta cuando se produce un TypeError
except:
    pass # Se ejecuta si no se cumplen los otros except


# Captura de la información de la excepción

try:
    pass # Ejecuta el código
except ValueError as e:
    print(e) # Encuentra un ValueError y lo guarda en una variable (e = error)
except Exception as my_random_error_name:
    print(my_random_error_name)
    # Captura cualquier error y lo guarda en una variable


# ---------------------------------------
# -------------- Exercises --------------
# ---------------------------------------
# 1-)
