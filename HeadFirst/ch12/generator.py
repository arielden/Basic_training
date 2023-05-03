import requests
from time import sleep
urls = ('http://headfirstlabs.com', 'http://oreally.com', 'http://twitter.com')

#-----------This block is a listcomp-------------------------------------------
print("Executing listcomp...")
for resp in [requests.get(url) for url in urls]:
    print(len(resp.content), '->', resp.status_code, '->', resp.url)

sleep(3)
#-----------This block is a generator-------------------------------------------
print("Executing generator...")
for resp in (requests.get(url) for url in urls):
    print(len(resp.content), '->', resp.status_code, '->', resp.url)