def convertidor(monto):
    usd=960
    sol=287
    eur=1100
    print(f"\nTus ${monto} pesos Chilenos equivalen a: \n {round((monto/usd),2)} dolares americanos.\n {round((monto/eur),2)} euros.\n {round((monto/sol),2)} soles peruanos.")

while True:
    sopes = input("\n¿Ingresa la cantidad de pesos chilenos que deseas cambiar: ")
    try:
        monto = int(sopes)
        print(f"¡Perfecto! Has ingresado el número entero: {monto}")
        break
    except ValueError:
        print("Error: Por favor, ingresa un número entero válido.")

convertidor(monto)