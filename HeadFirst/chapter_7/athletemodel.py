import pickle
from athletelist import AthleteList, get_coach_data

def put_to_store(files_list):
    all_athletes = {}

    for each_file in files_list:
        ath = get_coach_data(each_file)
        # Each name is used as the key, the value is the AthleteList object instance.
        all_athletes[ath.name] = ath
    try:
        with open('atheletes.pickle', 'wb') as athf:
            pickle.dump(all_athletes, athf)
    except IOError as err:
        print("File error (put_and_store): "+ str(err))

    return (all_athletes)

def get_from_store():
    all_athletes = {}
    try:
        with open('atheletes.pickle', 'rb') as athf:
            all_athletes = pickle.load(athf)
    except IOError as err2:
        print("File error (get_from_store): "+ str(err2))
    return all_athletes