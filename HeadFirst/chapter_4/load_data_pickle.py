import os
import pickle
from custom_nester import print_lol

new_man = []

os.chdir('/home/arield/Documentos/CODE/Python/Basic_training/HeadFirst/chapter_4')

try:
    with open('./man_data.txt', 'rb') as man_file:
        new_man = pickle.load(man_file)

except IOError as err:
    print(f'IO error!! --> {err}')

except pickle.PickleError as perr:
    print('picke error!')

print_lol(new_man)