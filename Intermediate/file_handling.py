'''This file is to practice my knowledge by Python'''

### File Handling ###

# We can create, read, update and delete files like .txt, .json, .xml, .csv, etc.
# We need to use open() build-in function

# Syntax
# open('filename', mode) # mode(r, a, w, x, t,b)

# Modes to open
# 'r' Modo de lectura (predeterminado). Abre el archivo para lectura.
# 'w' Modo de escritura. Abre el archivo para escritura. 
# Crea un archivo nuevo si no existe o trunca (borra) un archivo existente.
# 'a' Modo de adición. Abre el archivo para escritura, añadiendo el nuevo contenido al final 
# del archivo existente. Crea un archivo nuevo si no existe.
# 'x' Modo de creación exclusivo. Crea un archivo nuevo, 
# pero genera un error si el archivo ya existe.
# 'r+' Modo de lectura y escritura. Abre el archivo para lectura y escritura.
# 'w+' Modo de lectura y escritura. Abre el archivo para lectura y escritura. 
# Crea un archivo nuevo o trunca uno existente.
# 'a+' Modo de lectura y adición. Abre el archivo para lectura y adición de datos. 
# Crea un archivo nuevo o añade datos a uno existente.

# To write
# write(): Escribe una cadena de texto en el archivo.
# writelines(): Escribe una lista de cadenas de texto en el archivo. 

# To Read content
# read(): Lee todo el contenido del archivo como una sola cadena de texto.
# readline(): Lee una sola línea a la vez.
# readlines(): Lee todas las líneas y las devuelve como una lista de cadenas.

my_file_txt = open('file.txt', 'w+', encoding='utf-8')
my_file_txt.write('Hola muchachos, bienvenidos!\n')
my_file_txt.close()

my_file_txt = open('file.txt', 'r')
print(my_file_txt.read())
my_file_txt.close()


# The best way to works with files to open and close at the same time
# We use "with", esto garantiza que el archivo se cierre automáticamente al 
# finalizar el bloque de código, incluso si ocurren errores

# Syntax
# with open("nombre_archivo.txt", "modo") as variable_archivo:
#   Código para leer, escribir o modificar el archivo
#   variable_archivo.write("Hola mundo")

with open('file.txt', 'r') as file:
    file_text = file.read(4)
    print(file_text)

# To delete a file
# If we want to remove a file we use os module

# import os
# os.remove('file_text')

# But the best way to avoid mistakes is use a condition
# import os
# if os.path.exists('./file.txt'):
    # os.remove('./file.txt')
# else:
    # print('The file does not exist')


# .json file

import json

dev = {
    'name': 'John',
    'degree': 'Software Developer',
    'skills': ['Python, Git & GitHup'],
    'experience': '1 año'
}

with open('file.json', 'w', encoding='utf-8') as my_file_json:
    json.dump(dev, my_file_json, indent= 4)
