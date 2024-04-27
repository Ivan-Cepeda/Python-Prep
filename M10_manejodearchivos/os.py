import os

archivo = open('ejemplo.txt', 'w')

archivo.write('Hola estoy siendo creado para ser usado de ejemplo')

archivo.close()

archivo = open('ejemplo.txt', 'a')
archivo.write('\nHola de nuevo, me estoy actualizando\n')
archivo.close()

os.makedirs('Ejemplo')

os.system('copy ejemplo.txt Ejemplo')