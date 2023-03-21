"""Ejercitación Adicional con entrega, resolver desarrollando y utilizando funciones.
Una Tienda ofrece un descuento a sus clientes según la compra realizada:
- menos de 1000 pesos, no se le aplica descuento.
- Si el monto de la compra es entre 1000 y 2000, ofrece un 15% de descuento.
- Si el monto supera los 2000, ofrece un 20% de descuento.
Desarrollar un programa que ingrese el monto de la compra (validar que sea positivo) e
informe el monto a pagar con el descuento aplicado en caso de corresponder para cada compra.
El fin de carga se indica con un monto de compra igual a -1.
Luego emitir un informe final con la siguiente información:
a. Cuantas ventas se realizaron sin descuento / con el 15% de descuento / con el 20% de
descuento
b. Cuál fue el monto total de descuento realizado con el 15% de descuento / con el 20% de
descuento
c. Monto Promedio Total de ventas con el descuento aplicado.
d. Porcentaje de ventas sin descuento / con descuento
e. Mayor compra realizada.
f. Compra de menor valor."""

ventas = 0
descuento15 = 0
descuento20 = 0
descuento_total_15 = 0
descuento_total_20 = 0
mayor_venta = 0
monto_total_desc = 0
monto_desc = 0

 
def desc_20(monto):
    monto_d20 = monto * 0.80
    print(f"El monto a pagar (con descuento) es: {monto_d20}")
    return monto_d20
 
def desc_15(monto):
    monto_d15 = monto * 0.85
    print(f"El monto a pagar (con descuento) es: {monto_d15}")
    return monto_d15

monto = float(input("Ingrese el monto de la venta (-1 para salir): "))
menor_venta = monto
while monto != -1:
    if monto > 0:
        ventas += 1
        if monto >= 1000 and monto <= 2000:
            descuento15 += 1
            monto = desc_15(monto)
            descuento_total_15 = descuento_total_15 + monto
        elif monto >= 2000:
            descuento20 += 1
            monto = desc_20(monto)
            descuento_total_20 = descuento_total_20 + monto
        elif monto < 1000:
            print(f"El monto a pagar no tiene descuento: {monto}")
        monto_total_desc = monto_total_desc + monto
    else:
        print("El monto debe ser positivo")
        
    monto = float(input("Ingrese el monto de la venta (-1 para salir): "))
 
    if monto > mayor_venta:
        mayor_venta = monto
    if monto != -1:
        if monto < menor_venta:
            menor_venta = monto
if ventas > 0:
    print(f" ventas totales {ventas}, ventas con 15%: {descuento15},ventas con 20%: {descuento20}, ventas sin desc {ventas-descuento15-descuento20}")
    print(f"el monto total descontado (15%) fué de: {descuento_total_15}")
    print(f"el monto total descontado (20%) fué de: {descuento_total_20}")
    print(f"La mayor compra realizada fué de: {mayor_venta}, y la de menor valor {menor_venta}")
    if descuento15 + descuento20 >0:
        print(f"El monto promedio de ventas con descuento aplicado es de: {monto_total_desc/(descuento15+descuento20)}")
        print(f"El porcentaje de ventas con descuento es de: {((descuento15+descuento20)/ventas)*100}%")
        print(f"El porcentaje de ventas sin descuento es de: {(1-((descuento15+descuento20)/ventas))*100}%")
    else:
        print('No se realizaron ventas con descuentos')
else:
    print('No se realizaron ventas')