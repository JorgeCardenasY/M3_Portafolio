print('BIENVENIDO A LA AGENDA TELEFÓNICA DE CONTACTOS\n')
agenda = {}
while True:
    print('Menu de Opciones')
    print('1. Agregar Contacto')
    print('2. Mostrar Contactos')
    print('3. Buscar Contacto')
    print('4. Salir')
    opcion = input('\nSelecciona una opcion: ')
    if opcion == '1':
        nombre = (input('Ingrese el nombre del contacto: '))
        nombre = nombre.upper()
        telefono = input('Ingrese el telefono del contacto: ')
        agenda[nombre] = telefono
        print('\nContacto agregado exitosamente!\n')
        print('la agenda tiene la siguiente estructura:\n',agenda,'\n')
        
    elif opcion == '2':
        if agenda:
            print('\nContactos en la agenda:\n')
            for nombre, telefono in agenda.items():
                print(f'\nNombre: {nombre}, Telefono: {telefono}\n')
        else:
            print('\nLa agenda esta vacia.')
    elif opcion == '3':
        nombre = input('\nIngrese el nombre del contacto a buscar:\n ')
        nombre = nombre.upper()
        if nombre in agenda:
            print(f'\nContacto encontrado: Nombre: {nombre}, Telefono: {agenda[nombre]}\n')
        else:
            print('\nContacto no encontrado.\n')
    elif opcion == '4':
        print('\nSaliendo de la agenda. ¡Hasta luego!\n')
        break
    else:
        print('\nOpcion no valida. Por favor, intente de nuevo.\n')