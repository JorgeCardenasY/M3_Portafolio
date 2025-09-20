print ('\nBIENEVIDO AL GENERADOR DE TABLAS DE MULTIPLICAR\n')
num1 = (input('¿Con la Tabla de qué número deseas trabajar?: '))
num2 = (input('¿Cual es el limite Superior de la Tabla: '))
try:
    num1 = int(num1)
    num2 = int(num2)
    if num2 > 0:
        print(f'\nTabla de Multiplicar del {num1} hasta el {num2}\n')
        for i in range(1, num2 + 1):
            resultado = num1 * i
            print(f'{num1} x {i} = {resultado}')
    else:
        print('El limite superior debe ser un número positivo mayor que cero.')
except ValueError:
    print('\nChequea que el dato ingresado sea fehacientemente un número\n')