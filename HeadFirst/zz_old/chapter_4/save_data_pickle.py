import os
import pickle
from custom_nester import print_lol

man = []
other = []

os.chdir('/home/arield/Documentos/CODE/Python/Basic_training/HeadFirst/chapter_3')

try:
    data = open('./sketch.txt')
    for each_line in data:
        try:
            (role, line_spoken) = each_line.split(':', 1)
            line_spoken = line_spoken.strip()
            if role == 'Man':
                man.append(line_spoken)
            elif role == 'Other Man':
                other.append(line_spoken)
        except ValueError:
            pass

    data.close()


except IOError:
    print('Data file does not exist!')


"""When you use with, you no longer have to worry about closing any opened
files, as the Python interpreter automatically takes care of this for you.
We don't need to add the 'finnaly' section"""

os.chdir('/home/arield/Documentos/CODE/Python/Basic_training/HeadFirst/chapter_4/')

new_man = []

try:
    with open('man_data.txt', 'wb') as man_file, open('other_data.txt', 'wb') as other_file:
        pickle.dump(man, man_file)
        pickle.dump(other, other_file)


except IOError as err:
    print(f'{str(err)} happened!! :(')
except pickle.PicklingError as perr:
    print('pickling error!')