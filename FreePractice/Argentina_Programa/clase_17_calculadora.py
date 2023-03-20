print("             MENU          ")
print("***************************")
print("     INGRESE UNA OPCION    ")
print(" 1-  SUMAR (valores fijos)")
print(" 2-  RESTA")
print(" 3-  MULTIPLICACION")
print(" 4-  DIVISION (parte enterta)")
print(" 5-  EXPONENTE")
print("-1   SALIR")

opcion = int(input('Ingrese opción (-1 para salir): '))

def sumar():
    num_a = 10
    num_b = 20
    return num_a + num_b

def restar(a,b):
    return a - b

def multip(a,b):
    return a * b

def exponente(a,b):
    return a ** b

def division(a,b):
    return a // b

while opcion != -1:
    if opcion >= 1 and opcion <= 5:
        if opcion == 1:
            print('Se suman los valores fijos 10 y 20')
            resultado = sumar()
            print(f'el resultado es {resultado}\n')
        elif opcion == 2:
            print('Ingresar los valores a restar')
            num_a = float(input("Ingrese el primer valor: "))
            num_b = float(input("Ingrese el segundo valor: "))
            resultado = restar(num_a,num_b)
            print(f'el resultado es {resultado}\n')
        elif opcion == 3:
            print('Ingresar los valores a multiplicar')
            num_a = float(input("Ingrese el primer valor: "))
            num_b = float(input("Ingrese el segundo valor: "))
            resultado = multip(num_a,num_b)
            print(f'el resultado es {resultado}\n')
        elif opcion == 4:
            print('Ingresar los valores a dividir')
            num_a = float(input("Ingrese el primer valor: "))
            num_b = float(input("Ingrese el segundo valor: "))
            resultado = division(num_a,num_b)
            print(f'el resultado (parte entera) es {resultado}\n')
        elif opcion == 5:
            print('Ingresar los valores para cálculo de potencia')
            num_a = float(input("Ingrese la base: "))
            num_b = float(input("Ingrese la potencia: "))
            resultado = exponente(num_a,num_b)
            print(f'el resultado de {num_a} elevado a {num_b} es {resultado}\n')
    else:
        print("ingrese una opción válida (entre 1 y 5)")
    opcion = int(input('Ingrese opción (-1 para salir): '))