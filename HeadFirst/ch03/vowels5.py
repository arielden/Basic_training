vowels = ['a', 'e', 'i', 'o', 'u']
word = input("Provide a word to search for vowels: ")

found = {}
# found['a'] = 0
# found['e'] = 0
# found['i'] = 0
# found['o'] = 0
# found['u'] = 0

for letter in word:
    if letter in vowels:
        found.setdefault(letter, 0)
        #setdefault method replace the following two (commented) lines.
        # if letter not in found:
        #    found[letter] = 0
        found[letter] += 1
for k, v in sorted(found.items()):
    print(k, 'was found', v, 'time(s).')
