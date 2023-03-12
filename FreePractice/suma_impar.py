#ej11
n = int(input("Ingrese un número: "))
suma = 0
while n < 0:
    print("El número ingresado es incorrecto. Ingrese otro número: ")
    n = int(input("Ingrese un número: "))
else:
    for i in range(1, n+1):
        if i % 2 != 0:
            print(i)
            suma = suma + i
    print(f"La suma de todos los impares es {suma}")