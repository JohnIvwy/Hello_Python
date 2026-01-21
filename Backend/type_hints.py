### Type Hints ###

# Nos permite declarar el tipo de dato de una variable (int, str, bool...)
# asi el servidor podrá trabajar mas rápido al validar los datos y a indicarnos 
# si no nos llegó el tipo de dato que esperábamos recibir. 
# Como Python en dinámico igual podemos cambiar su tipo de dato por el camino, 
# pero FastAPI nos mandara error

# Definimos el tipo después del nombre de la variable
mi_string: str = "Esta es una cadena"
mi_number: int = 22
mi_bool: bool = True
