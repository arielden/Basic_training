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

james = loader('james.txt')
julie = loader('julie.txt')
mikey = loader('mikey.txt')
sarah = loader('sarah.txt')

print(sorted(set([sanitize(each_element) for each_element in james]))[0:3])
print(sorted(set([sanitize(each_element) for each_element in julie]))[0:3])
print(sorted(set([sanitize(each_element) for each_element in mikey]))[0:3])
print(sorted(set([sanitize(each_element) for each_element in sarah]))[0:3])

