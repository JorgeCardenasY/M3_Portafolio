print ('\nEste segmento de Código solicita al usuario ingresar\nun número y determina si es positivo, negativo o cero.\nCaso contrario, lo reporta como texto.')
num = (input('Ingrese algo: '))
try:
    num = float(num)
    if num > 0:
        print('El número es positivo')
    elif num < 0:
        print('El número es negativo')
    else:
        print('El número es cero')
except ValueError:
    print('El valor ingresado no es un número')