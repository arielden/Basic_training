# """Ejercicio 3
# Un negocio desea saber el importe total recaudado al fin del día, desea contar con un programa que
# pueda ingresar el importe de cada venta realizada. Para indicar que finalizó el día se ingresa -1. ¿Cuál
# fue el monto total vendido y cuántas ventas se realizaron? El importe de cada venta realizada debe
# ser un valor positivo."""

# venta_realizada = float(input("Ingrese el valor de la venta: "))
# contador = 0
# suma = 0
# while venta_realizada != -1:
#     if venta_realizada > 0:
#         suma = suma + venta_realizada
#         contador += 1
#     else:
#         print("el valor debe ser mayor positivo")
#     venta_realizada = float(input("Ingrese el valor de la venta: "))
# print(f"Se realizaron {contador} ventas, por un valor de {suma}")

"""Ejercicio 5
Escribir un algoritmo que permita ingresar los números de legajo de los alumnos de un curso y su
nota de examen final. El fin de la carga se determina ingresando un -1 en el legajo. Informar para
cada alumno si aprobó o no el examen considerando que se aprueba con nota mayor o igual a 4. Se
debe validar que la nota ingresada sea entre 1 y 10. Terminada la carga de datos, informar:
• Cantidad de alumnos que aprobaron con nota mayor o igual a 4.
• Cantidad de alumnos que desaprobaron el examen. Nota menor a 4.
• Porcentaje de alumnos que están aplazados (tienen 1 en el examen)."""

aprobados = 0
desaprobados = 0
aplazados = 0
contador = 0

legajo = int(input("legajo: "))

while legajo != -1:
    contador += 1
    nota_final = float(input("nota: "))
    if nota_final > 1 and nota_final <= 10:
        if nota_final >= 4:
            print(f"el legajo {legajo}, está APROBADO")
            aprobados += 1
        else:
            print(f"el legajo {legajo}, está DESAPROBADO")
            desaprobados += 1
    elif nota_final == 1:
        print(f"el legajo {legajo}, está APLAZADO")
        desaprobados += 1
        aplazados += 1
    else:
        print("la nota debe estar entre 1 y 10")
    legajo = int(input("otro legajo: "))
    
print(f'desaprobaron {desaprobados} y aprobaron {aprobados} de {contador} alumnos')
print(f'con un {(aplazados/contador)*100}% de aplazos')