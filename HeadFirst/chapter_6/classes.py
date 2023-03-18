class Athlete():
    def __init__(self, a_name, a_dob=None, times=[]):
        self.name = a_name
        self.dob = a_dob
        self.top3 = times[0:3]
        pass

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
        athlete = Athlete(athlete.pop(0), athlete.pop(0), sorted(set(sanitize(each) for each in athlete)))
        return athlete
    except IOError as err:
        print(f"The file doesn't exist! --> {err}")
        return None
#------------------------------------

james = get_coach_data('james2.txt')