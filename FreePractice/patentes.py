#ej 10
par = 0
impar = 0
patente = int(input("Ingrese la terminación de la patente (-1 para Salir): "))
while patente != -1:
    resultado = patente % 2
    if resultado == 1:
        impar += 1
    else:
        par += 1
    patente = int(input("Ingrese la terminación de la patente: "))
print(f"Se ingresaron {par} patentes pares y {impar} patentes impares")