def calcPromedio(lista):
    """ Recibe una lista, suma sus elementos
    y calcula el promedio"""
    suma = 0
    promedio = 0
    for elemento in lista:
        suma = suma + elemento
    promedio = suma / len(lista)
    return promedio

def buscaMinimos(lista, promedio):
    """ Recibe una lista, busca valores menores al promedio
    y devuelve otra lista con sus posiciones en la lista original"""
    lista_pos = []
    for i in range(len(lista)):
        if lista[i] < promedio:
            lista_pos.append(i)
    return lista_pos

def filtraDias(lista_pos, lista_dias):
    """Recibe una lista de posiciones y busca esas posiciones
     en la lista de días. Compara si los dias son menor o igual a 10
      devuelve otra lista con posiciones que cumplen el criterio """
    lista_selecc = []
    for elemento in lista_pos:
        if lista_dias[elemento] <= 10:
            lista_selecc.append(elemento)
    return lista_selecc

def ordenaListas(lista_pnom, lista_ppre, lista_dias):
    aux_pnom = ""
    aux_dias = 0
    aux_ppre = 0
    # Puntero
    for i in range(len(lista_dias)):
        j = i
        # Iteracion del valor siguiente al puntero
        while j < len(lista_dias):
            if(lista_dias[i] > lista_dias[j]):
                aux_dias = lista_dias[i]
                lista_dias[i] = lista_dias[j]
                lista_dias[j] = aux_dias

                aux_pnom = lista_pnom[i]
                lista_pnom[i] = lista_pnom[j]
                lista_pnom[j] = aux_pnom

                aux_ppre = lista_ppre[i]
                lista_ppre[i] = lista_ppre[j]
                lista_ppre[j] = aux_ppre
            j = j + 1

lista_pnom = []
lista_ppre = []
lista_dias = []

# respuesta = 'y'
# while respuesta != 'n':
#     prov_nombre = input("Ingrese el nombre del proveedor: ")
#     lista_pnom.append(prov_nombre)
#     prov_presup = float(input("Ingrese el valor del presupuesto: "))
#     lista_ppre.append(prov_presup)
#     dias_ent = int(input("Ingrese la cant. de días para entrega: "))
#     lista_dias.append(dias_ent)
#     respuesta = input("Quiere continuar, (s/n)")

lista_pnom = ["prov_1", "prov_2", "prov_3", "prov_4"]
lista_ppre = [40, 20, 10, 30]
lista_dias = [5, 7, 8, 15]

res_promedio = calcPromedio(lista_ppre)
lista_pos = buscaMinimos(lista_ppre, res_promedio)
seleccion = filtraDias(lista_pos, lista_dias)

for elemento in seleccion:
    print(f"El proveedor seleccionado es {lista_pnom[elemento]} con un presupuesto de ${lista_ppre[elemento]} y {lista_dias[elemento]} dias de entrega ")