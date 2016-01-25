import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

# page = webdriver.Firefox()
page = webdriver.Chrome(executable_path='/home/rg3915/Downloads/chromedriver')
page.maximize_window()
time.sleep(0.5)
page.get('http://localhost:8000/customer/add/')

search = page.find_element_by_id('id_username')
search.send_keys('regis')

search = page.find_element_by_id('id_password')
search.send_keys('1')

button = page.find_element_by_xpath("//input[@type='submit']")
button.click()

fields = [
    ['id_treatment', 'sr'],
    ['id_first_name', 'Rafael'],
    ['id_last_name', 'Cândido de Morais'],  # get_lastname,
    ['id_company', 'Supertoys'],
    ['id_department', 'Contábil'],
    ['id_email', 'rafael@supertoys.com'],
    ['id_phone1', '10 1234-5678'],  # generate_phone,
    ['id_phone2', '10 1234-5679'],
    ['id_phone3', '10 1234-5680'],
    ['id_cpf', '11156358329'],
    ['id_rg', '73552210'],
    ['id_cnpj', '10094604000116'],
    ['id_ie', '1542682213'],
    ['id_type_customer', 'particular'],
    ['id_address', 'Rua Verde, 132'],   # r['Logradouro']
    ['id_complement', 'Apto 303'],
    ['id_district', 'Centro'],  # r['Bairro']
    ['id_city', 'São Paulo'],  # r['Localidade']
    ['id_uf', 'SP'],
    ['id_cep', '01200100'],
]

for field in fields:
    search = page.find_element_by_id(field[0])
    search.send_keys(field[1])


# button = page.find_element_by_id('id_submit')
button = page.find_element_by_class_name('btn-primary')
button.click()

page.quit()
