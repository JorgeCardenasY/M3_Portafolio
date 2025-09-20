import os
import time

def registrar_usuario():
    usuarios = []
    
    nombre = input('Por favor, ingresa tu Primer Nombre:\n')
    apellido = input('Por favor, ingresa tu Primer Apellido:\n')
    region = input('Por favor, ingresa tu Región de Residencia:\n')
    ciudad = input('Por favor, ingresa tu Ciudad de Residencia:\n')

    return [nombre, apellido, region, ciudad]

os.system('cls' if os.name == 'nt' else 'clear')
print('Bienvenido al formulario de Registro Arbitrario\n')
print("Deseamos conocerte. Ten a bien responder las siguientes preguntas:\n")

wait_time = 5
time.sleep(wait_time)
os.system('cls' if os.name == 'nt' else 'clear')

Usuarios = registrar_usuario()
print(f'Gracias!. Haz sido registrado exitosamente con los datos\n {Usuarios[-1]}\n')
while True:
    otro_usuario = input('¿Desea agregar otro usuario? Presiona 1 para Sí o cualquier otra tecla para No:\n')
    if otro_usuario == '1':
        Usuarios.append(registrar_usuario())
    else:
        break

print("\nSe registraron los siguientes usuarios:")
for i, usuario in enumerate(Usuarios, 1):
    print(f"\nUsuario {i}:")
    print(f"Nombre: {usuario[0]}")
    print(f"Apellido: {usuario[1]}")
    print(f"Región: {usuario[2]}")
    print(f"Ciudad: {usuario[3]}")

print("Gracias por usar el formulario de Registro Arbitrario. ¡Hasta luego!\n")
