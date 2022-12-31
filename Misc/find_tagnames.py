#Busca 

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support import expected_conditions as EC


import time

class FindByTagName:

    def test(self):
        baseURL = 'https://www.aviationweather.gov/metar/data?ids=saco&format=raw&date=&hours=6'
        s = Service(r"C:\Program Files\Google\Chrome\Application\chromedriver.exe")
        driver = webdriver.Chrome(service = s)
        driver.get(baseURL)

        metar_list = driver.find_elements(By.TAG_NAME, 'code') # this creates a list of elements
        EC.presence_of_element_located((By.ID, "awc_main_content_wrap"))

        try:
            if metar_list is not None:
                print('found tag element')
                print(metar_list[0].text)
                print(metar_list[1].text)
                print(metar_list[2].text)
                print(metar_list[3].text)
                print(metar_list[4].text)
                print(metar_list[5].text)

            time.sleep(3)
        except:
                print('Not Found!')
        finally:
            driver.quit()

search_1 = FindByTagName()
search_1.test()