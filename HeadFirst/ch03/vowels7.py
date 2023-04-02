vowels = set('aeiou')
word = input("Provide a word to search for vowels: ")
found = sorted(vowels.intersection(set(word)))
for vowel1 in found:
    print(vowel1)