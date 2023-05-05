import asyncio
from time import sleep
from time import perf_counter

productos = ['prod1', 'prod2', 'prod3']

async def buscaProdAsync(prodx:str):
    print("Buscando...")
    await asyncio.sleep(2)
    found = False
    for prod in productos:
        if prod == prodx:
            print(f"{prodx} Encontrado!")
            found = True
        
    return found

lista_busca = ['prod2', 'prod1', 'prod4', 'prod3']

async def main(lista):
    for prod in lista:
        task = asyncio.create_task(buscaProdAsync(prod))
    await task


start = perf_counter()
asyncio.run(main(lista_busca))
finish = perf_counter()

totalTime = round((start-finish),3)

print(f"Total time is: {totalTime} sec.")