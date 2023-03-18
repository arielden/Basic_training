string = input('Ingrese el string: ')
reversed_string = ""
for letra in string:
    reversed_string = (f"{letra}{reversed_string}")

print(reversed_string)
