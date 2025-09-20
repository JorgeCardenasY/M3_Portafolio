import os
import time

usuarios = []
def registrar_usuario():
    nombre = input('Por favor, ingresa tu Primer Nombre:\n')
    apellido = input('Por favor, ingresa tu Primer Apellido:\n')
    region = input('Por favor, ingresa tu Región de Residencia:\n')
    ciudad = input('Por favor, ingresa tu Ciudad de Residencia:\n')

    usuario = {'nombre': nombre, 'apellido': apellido, 'region': region, 'ciudad': ciudad}
    usuarios.append(usuario)
    print('Usuario registrado exitosamente.')
    time.sleep(2)
    os.system('cls' if os.name == 'nt' else 'clear')
    return usuario

def mostrar_usuarios():
    for usuario in usuarios:
        print(f'Nombre: {usuario["nombre"]}')
        print(f'Apellido: {usuario["apellido"]}')
        print(f'Región: {usuario["region"]}')
        print(f'Ciudad: {usuario["ciudad"]}')
        print('------------------')
    input('Presiona Enter para continuar...')
    os.system('cls' if os.name == 'nt' else 'clear')
    return usuarios

def menu():
    while True:
        print('Menu de Opciones')
        print('1. Registrar Usuario')
        print('2. Mostrar Usuarios')
        print('3. Mostrar Información almacenada por Variables')
        print('4. Salir')
        opcion = input('Selecciona una opcion: ')
        if opcion == '1':
            registrar_usuario()
        elif opcion == '2':
            if len(usuarios) == 0:
                print('No hay usuarios registrados.')
                time.sleep(2)
                os.system('cls' if os.name == 'nt' else 'clear')
            mostrar_usuarios()
        elif opcion == '3':
            if len(usuarios) == 0:
                print('No hay usuarios registrados.')
                time.sleep(2)
                os.system('cls' if os.name == 'nt' else 'clear')
            else:
                print('Información almacenada por Variables:')
                nombres = [usuario["nombre"] for usuario in usuarios if "nombre" in usuario]
                print(f'Los nombres de los usuarios registrados son:\n{nombres}')
                apellidos = [usuario["apellido"] for usuario in usuarios if "apellido" in usuario]
                print(f'Los apellidos de los usuarios registrados son:\n{apellidos}')
                regiones = [usuario["region"] for usuario in usuarios if "region" in usuario]
                print(f'Las regiones de los usuarios registrados son:\n{regiones}')
                ciudades = [usuario["ciudad"] for usuario in usuarios if "ciudad" in usuario]
                print(f'Las ciudades de los usuarios registrados son:\n{ciudades}')
                input('Presiona Enter para continuar...')
                os.system('cls' if os.name == 'nt' else 'clear')
        elif opcion == '4':
            break

if __name__ == '__main__':
    menu()
    print('Gracias por utilizar el programa.')

