import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

# page = webdriver.Firefox()
page = webdriver.Chrome(executable_path='/home/rg3915/Downloads/chromedriver')
page.maximize_window()
time.sleep(0.5)
page.get('http://localhost:8000/entry/add/')

search = page.find_element_by_id('id_username')
search.send_keys('regis')

search = page.find_element_by_id('id_password')
search.send_keys('1')

button = page.find_element_by_xpath("//input[@type='submit']")
button.click()

fields = [
    ['id_priority', 'Normal'],
    ['id_category', 'orçamento'],
    ['id_work', 'Obra'],
    ['id_person', 'Sr. Regis da Silva'],
    ['id_description', 'Contém projetos e planilha.'],
    ['id_seller', 'regis'],
]

for field in fields:
    search = page.find_element_by_id(field[0])
    search.send_keys(field[1])


button = page.find_element_by_class_name('btn-primary')
button.click()

page.quit()
