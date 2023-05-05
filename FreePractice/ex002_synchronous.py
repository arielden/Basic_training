from time import sleep
from time import perf_counter

productos = ['prod1', 'prod2', 'prod3']

def buscaProdSync(prodx:str):
    print("Buscando...")
    sleep(2)
    found = False
    for prod in productos:
        if prod == prodx:
            print(f"{prodx} Encontrado!")
            found = True
        
    return found

lista_busca = ['prod2', 'prod1', 'prod4', 'prod3']

def main(lista):
    for prod in lista:
        buscaProdSync(prod)


start = perf_counter()
main(lista_busca)
finish = perf_counter()

totalTime = round((start-finish),3)

print(f"Total time is: {totalTime} sec.")