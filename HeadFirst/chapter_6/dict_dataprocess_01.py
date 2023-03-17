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
def loader(data_file):
    try:
        with open(data_file) as daf:
            data = daf.readline()
        return data.strip().split(',')
    except IOError as err:
        print(f"The file doesn't exist! --> {err}")
        return None
#------------------------------------
sarah = loader('sarah2.txt')
(sarah_name, sarah_dob) = sarah.pop(0), sarah.pop(0)
# print(sarah_name + "'s fastest times are: " +
#       str(sorted(set(sanitize(each) for each in sarah))[0:3]))

sarah_dict = {'Name': sarah_name, 'Birthdate': sarah_dob, 'Times': sorted(set(sanitize(each) for each in sarah))[0:3] }
print(sarah_dict)