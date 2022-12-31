"""
6-3. Glossary: A Python dictionary can be used to model an actual dictionary.
However, to avoid confusion, let's call it a glossary.

• Think of five programming words you've learned about in the previous
chapters. Use these words as the keys in your glossary, and store their
meanings as values.

• Print each word and its meaning as neatly formatted output. You might
print the word followed by a colon and then its meaning, or print the word
on one line and then print its meaning indented on a second line. Use the
newline character (\n) to insert a blank line between each word-meaning
pair in your output.

"""

programming_words = {'for': 'this can be used for cylces',
                    'if': 'conditional word',
                    'len': 'this give us the lenght of a list',
                    'import': 'used for import modules',
                    'def': 'defines a function',
                    'self': 'internal function behaviour',
                    }
for key, value in programming_words.items():
    print(f"\n{key}:\t {value.title()}")