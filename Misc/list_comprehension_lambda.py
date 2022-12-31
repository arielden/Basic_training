# Crea una lista con números enteros del 1 al 9
list_numbers = [number for number in range(1, 10)]
print(list_numbers)

# Filtra la lista anterior dejando sólo números pares, y crea otra lista llamada "even_numbers"
even_numbers = list(filter(lambda x: x%2==0, list_numbers))
print(even_numbers)