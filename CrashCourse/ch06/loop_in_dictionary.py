favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
}

for name, language in favorite_languages.items():
    print(f"{name.title()}'s, favorite language is, {language.title()}")


print("The folowing languages have been mentioned: ")
for language in favorite_languages.values():
    print(f"\t\t\t\t\t\t{language.title()}")