import random

def generarListaAzar(n):
    lista = []
    for i in range(0,n):
        nro = random.randint(10,99)
        lista.append(nro)
    return lista

def MostrarLista(lista):
    i = 0
    #lista = []
    while i < len(lista):
        print(lista[i], end=" ")
        #print(lista)
        i = i + 1
    print('\n')

def BuscarValorSecuencial(lista, nro):
    encontrado = False
    i = 0
    while i < len(lista) and encontrado == False:
        if lista[i] == nro:
            encontrado = True
        i = i + 1
    return encontrado

N = int(input('Ingrese la cantidad de elementos que se desea crear: '))
miLista = generarListaAzar(N)
MostrarLista(miLista)

valor=int(input('Ingrese el valor a buscar: '))

if BuscarValorSecuencial(miLista,valor) == True:
    print('El valor se encuentra en la lista')
else:
    print('El valor No se encuentra en la lista')