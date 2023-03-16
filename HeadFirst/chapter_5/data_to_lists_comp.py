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

# import os

# os.chdir('/home/arield/Documentos/CODE/Python/Basic_training/HeadFirst/chapter_5')

with open('./data/james.txt') as jaf: data = jaf.readline()
james = data.strip().split(',')

with open('./data/julie.txt') as juf: data = juf.readline()
julie = data.strip().split(',')

with open('./data/mikey.txt') as mif: data = mif.readline()
mikey = data.strip().split(',')

with open('./data/sarah.txt') as saf: data = saf.readline()
sarah = data.strip().split(',')

clean_james = sorted([sanitize(each_element) for each_element in james])
clean_julie = sorted([sanitize(each_element) for each_element in julie])
clean_mikey = sorted([sanitize(each_element) for each_element in mikey])
clean_sarah = sorted([sanitize(each_element) for each_element in sarah])


print(james)
print(clean_james)
print(clean_julie)
print(clean_mikey)
print(clean_sarah)