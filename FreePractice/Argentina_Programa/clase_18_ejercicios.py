"""Ejercicio 1
Ingresar 10 alumnos y 3 notas por alumno, calcular el promedio de cada uno,
mostrar la cantidad de alumnos promocionados con nota mayor o igual a 7, regulares los alumnos
con nota mayor que 5 y menor que 7, y los demás desaprobados."""

def promedio(nota1, nota2, nota3):
    prom = (nota1 + nota2 + nota3)/3
    return prom

# aprobados = 0
# regulares = 0
# desaprobados = 0
# for i in range(1,3):
#     print(f'Para el alumno número {i}')
#     n1 = int(input('Ingrese la primer nota: '))
#     n2 = int(input('Ingrese la segunda nota: '))
#     n3 = int(input('Ingrese la tercer nota: '))
#     prom_final = promedio(n1, n2, n3)
#     if prom_final >= 7:
#         aprobados += 1
#     elif prom_final > 5 and prom_final < 7:
#         regulares += 1
#     else:
#         desaprobados += 1

# print(f'De 10 alumnos, aprobaron {aprobados}, son regulares {regulares} y desaprobaron {desaprobados}')

"""
Ejercicio 2
Desarrollar una función para calcular el factorial de un número
# Ejemplo: fact(4) = 4*3*2*1 = 24.
# 0! = 1
# 1! = 1 * 1
# 2! = 1 * 1 * 2 = 2
# 3! = 1 * 1 * 2 * 3 = 6
# 4! = 1 * 1 * 2 * 3 * 4 = 24"""

def factorial(numero):
    if(type(numero) != int):
        return 'El numero debe ser un entero'
    if(numero < 0):
        return 'El numero debe ser positivo'
    if (numero > 1):
        numero = numero * factorial(numero - 1)
    return numero


"""Ejercicio 3
Escribir una función que reciba como parámetros dos números enteros y
devuelva la concatenación de ambos. Resolver en lo posible sin convertir tipos de datos.
Por ejemplo, concatenar (123,456) devuelve 123456."""

def concatena(num1, num2):
    print(f"{num1}{num2}")

"""Ejercicio 4
Recibir tres números correspondientes al día, mes y año de una fecha y retornar True/False
indicando si es o no una fecha válida."""

def validez_fecha(dd, mm, aaaa):
    val = True
    if aaaa >= 1 and aaaa <= 2100:
        if dd >= 1 and dd <= 31:
            if mm >= 1 and mm <= 12:
                if mm == 2 and dd > 28:
                    val = False
                if mm == 4 or mm == 6 or mm == 9 or mm == 11 and dd == 31:
                    val = False
            else:
                val = False
        else:
            val = False
    else:
        val = False
    return val

print(validez_fecha(31,4,2023))
#print(factorial(5))
#concatena(123, 456)