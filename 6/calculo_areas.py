import os
import math
import time

def area_cuadrado(lado):
    return lado ** 2

def area_rectangulo(base, altura):
    return base * altura

def area_triangulo(base, altura):
    return (base * altura) / 2

def area_circulo(radio):
    return math.pi * (radio ** 2)

# principal
def main():
    while True:
        print("\n--- Calculadora de Áreas ---")
        print("1. Cuadrado")
        print("2. Rectángulo")
        print("3. Triángulo")
        print("4. Círculo")
        print("5. Salir")
        opcion = input("\nSelecciona una opción (1-5): ")
        if opcion == "1":
            time.sleep(2)
            lado = float(input("Ingresa el lado del cuadrado: "))
            print(f"\nÁrea del cuadrado: {area_cuadrado(lado)}")
            time.sleep(2)
        elif opcion == "2":
            time.sleep(2)
            base = float(input("Ingresa la base del rectángulo: "))
            altura = float(input("Ingresa la altura del rectángulo: "))
            print(f"\nÁrea del rectángulo: {area_rectangulo(base, altura)}")
            time.sleep(2)
        elif opcion == "3":
            time.sleep(2)
            base = float(input("Ingresa la base del triángulo: "))
            altura = float(input("Ingresa la altura del triángulo: "))
            print(f"Área del triángulo: {area_triangulo(base, altura)}")
            time.sleep(2)
        elif opcion == "4":
            time.sleep(2)
            radio = float(input("Ingresa el radio del círculo: "))
            print(f"Área del círculo: {area_circulo(radio):.2f}")
            time.sleep(2)
        elif opcion == "5":
            print("¡Hasta luego!")
            time.sleep(2)
            break
        else:
            print("\nOpción no válida. Intenta nuevamente.\n")

# Ejecutar el programa

if __name__ == "__main__":
    main()