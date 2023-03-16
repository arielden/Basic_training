"""
Desarrollar un programa generar N números al azar de
un dígito positivo. N se ingresa por teclado. Mostrar los
números a medida que se van creando. Al finalizar
mostrar su suma."""

import random

num = int(input("Ingrese cantidad de números a generar: "))
suma = 0
for i in range(num+1):
    aleatorio = random.randint(i, num)
    suma = suma + aleatorio
    print(aleatorio)

print(f'La suma de todos los aleatorios es: {suma}')