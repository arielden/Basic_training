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

with open('./data/james.txt') as jaf: data = jaf.readline()
james = data.strip().split(',')

with open('./data/julie.txt') as juf: data = juf.readline()
julie = data.strip().split(',')

with open('./data/mikey.txt') as mif: data = mif.readline()
mikey = data.strip().split(',')

with open('./data/sarah.txt') as saf: data = saf.readline()
sarah = data.strip().split(',')

new_james = []
for each_element in james:
    new_james.append(sanitize(each_element))

new_julie = []
for each_element in julie:
    new_julie.append(sanitize(each_element))

new_mikey = []
for each_element in mikey:
    new_mikey.append(sanitize(each_element))

new_sarah = []
for each_element in sarah:
    new_sarah.append(sanitize(each_element))

print(sorted(new_james))
print(sorted(new_julie))
print(sorted(new_mikey))
print(sorted(new_sarah))