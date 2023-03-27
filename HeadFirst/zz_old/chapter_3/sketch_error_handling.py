import os

os.chdir('/home/arield/Documentos/CODE/Python/Basic_training/HeadFirst/chapter_3')

"""Using “try/except”
lets you concentrate
on what your code
needs to do..."""

try:
    data = open('./sketch.txt')

    for each_line in data:
        try:
            (role, line_spoken) = each_line.split(':', 1)
            print(role, end='')
            print(' said: ', end='')
            print(line_spoken, end='')
        except ValueError:
            pass

    data.close()
except IOError:
    print('Data file is missing!')