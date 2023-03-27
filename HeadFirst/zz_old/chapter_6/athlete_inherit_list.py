class AthleteList(list):
    def __init__(self, a_name, a_dob=None, a_times=[]):
        list.__init__([])
        self.name = a_name
        self.dob = a_dob
        self.extend(a_times)

    def top3(self):
        return sorted(set(sanitize(each) for each in self))[0:3]
    
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
        templist = data.strip().split(',')
        return AthleteList(templist.pop(0), templist.pop(0), templist)
    except IOError as err:
        print(f"The file doesn't exist! --> {err}")
        return None
#------------------------------------

james = get_coach_data('./data/james2.txt')
julie = get_coach_data('./data/julie2.txt')
mikey = get_coach_data('./data/mikey2.txt')
sarah = get_coach_data('./data/sarah2.txt')

print(f"{james.name}'s fastest times are: {james.top3()}")
print(f"{julie.name}'s fastest times are: {julie.top3()}")
print(f"{mikey.name}'s fastest times are: {mikey.top3()}")
print(f"{sarah.name}'s fastest times are: {sarah.top3()}")

james.append('1.93')
sarah.extend(['1.98', '1.92'])

print(f"{james.name}'s fastest times are: {james.top3()}")
print(f"{sarah.name}'s fastest times are: {sarah.top3()}")