#------------------------------------
def sanitize(time_string):
    if '-' in time_string:
        splitter = '-'
    elif ':' in time_string:
        splitter = ':'
    else:
        return(time_string)
    (mins, secs) = time_string.split(splitter)
    return(mins + '.' + secs)
#------------------------------------
def get_coach_data(data_file):
    try:
        with open(data_file) as daf:
            data = daf.readline()
        athlete = data.strip().split(',')
        athlete = {'Name': athlete.pop(0),
                   'Birthdate': athlete.pop(0),
                   'Times': sorted(set(sanitize(each) for each in athlete))[0:3] }
        return athlete
    except IOError as err:
        print(f"The file doesn't exist! --> {err}")
        return None
#------------------------------------

james_data = get_coach_data('./data/james2.txt')
julie_data = get_coach_data('./data/julie2.txt')
mikey_data = get_coach_data('./data/mikey2.txt')
sarah_data = get_coach_data('./data/sarah2.txt')

print(james_data)
print(julie_data)
print(mikey_data)
print(sarah_data)