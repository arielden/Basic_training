# Store information about a pizza being ordered.

pizza = {
'crust': 'thick',
'toppings': ['mushrooms', 'extra cheese'],
}

# Summarize the order

print(f"You ordered a {pizza['crust']}-crust pizza "
"whit the following toppings:")

for topping in pizza['toppings']:
    print("\t" + topping)


favorite_languages = {'sarah': ['python', 'ruby'], 'natalin': ['java', 'sql', 'html'], 'ariel': ['python']}
for name, languages in favorite_languages.items():
    print(f"{name.title()}'s favorite language/s is: ")
    for language in languages:
        print(language.title())