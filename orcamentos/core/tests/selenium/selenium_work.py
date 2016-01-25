import time
import csv
from random import randint, choice
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

# page = webdriver.Firefox()
page = webdriver.Chrome(executable_path='/home/rg3915/Downloads/chromedriver')
page.maximize_window()
time.sleep(0.5)
page.get('http://localhost:8000/work/add/')

search = page.find_element_by_id('id_username')
search.send_keys('regis')

search = page.find_element_by_id('id_password')
search.send_keys('1')

button = page.find_element_by_xpath("//input[@type='submit']")
button.click()

address_list = []

''' Lendo os dados de enderecos_.csv '''
with open('fixtures/enderecos_.csv', 'r') as f:
    r = csv.DictReader(f)
    for dct in r:
        address_list.append(dct)
    f.close()

INDEX = randint(0, 146)

fields = [
    ['id_name_work', 'Obra ' + str(randint(1, 5))],
    ['id_person', 'Sr. Regis da Silva'],
    ['id_customer', 'Hochtief'],
    ['id_address', address_list[INDEX]['address']],
    ['id_complement', ''],
    ['id_district', address_list[INDEX]['district']],
    ['id_city', address_list[INDEX]['city']],
    ['id_uf', address_list[INDEX]['city']],
    ['id_cep', address_list[INDEX]['cep']],
]

for field in fields:
    search = page.find_element_by_id(field[0])
    search.send_keys(field[1])


button = page.find_element_by_class_name('btn-primary')
button.click()

page.quit()
