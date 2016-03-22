import time
import csv
from random import randint, choice
from gen_names import gen_male_first_name, gen_female_first_name, gen_last_name
from gen_random_values import gen_cpf, gen_rg, gen_digits, gen_phone
from selenium import webdriver
from lists import company_list, department_list
# from selenium.webdriver.common.keys import Keys

# page = webdriver.Firefox()
page = webdriver.Chrome(executable_path='/home/rg3915/Downloads/chromedriver')
page.maximize_window()
time.sleep(0.5)
page.get('http://localhost:8000/crm/customer/add/')


# search = page.find_element_by_id('id_username')
# search.send_keys('regis')

# search = page.find_element_by_id('id_password')
# search.send_keys('1')

# button = page.find_element_by_xpath("//input[@type='submit']")
# button.click()

INDEX = randint(0, 146)

g = randint(0, 1)

if g:
    gender = 'id_gender_1'
    dict_ = gen_female_first_name()
else:
    gender = 'id_gender_0'
    dict_ = gen_male_first_name()

treatment = dict_['treatment']
first_name = dict_['first_name']
last_name = gen_last_name()
print(first_name, last_name)

email = '{}.{}@example.com'.format(
    first_name[0].lower(), last_name.lower())

slug = '{}-{}'.format(first_name.lower(), last_name.lower())

photo = 'http://icons.iconarchive.com/icons/icons-land/vista-people/256/Office-Customer-Male-Light-icon.png'

address_list = []

''' Lendo os dados de enderecos_.csv '''
with open('fix/enderecos_.csv', 'r') as f:
    r = csv.DictReader(f)
    for dct in r:
        address_list.append(dct)
    f.close()

search = page.find_element_by_id(gender)
search.click()

fields = [
    ['id_treatment', treatment],
    ['id_first_name', first_name],
    ['id_last_name', last_name],
    ['id_email', email],
    ['id_slug', slug],
    ['id_company', choice(company_list)],
    ['id_department', choice(department_list)],
]

for field in fields:
    search = page.find_element_by_id(field[0])
    search.send_keys(field[1])
    # time.sleep(0.5)

button = page.find_element_by_link_text('Documentos')
button.click()

fields = [
    ['id_photo', photo],
    ['id_cpf', gen_cpf()],
    ['id_rg', gen_rg()],
    ['id_cnpj', gen_digits(14)],
    ['id_ie', gen_digits(12)],
]

for field in fields:
    search = page.find_element_by_id(field[0])
    search.send_keys(field[1])
    # time.sleep(0.5)

button = page.find_element_by_link_text('Endereço')
button.click()

fields = [
    ['id_address', address_list[INDEX]['address']],
    ['id_complement', 'Apto 303'],
    ['id_district', address_list[INDEX]['district']],
    ['id_city', address_list[INDEX]['city']],
    ['id_uf', address_list[INDEX]['city']],  # deixa city mesmo
    ['id_cep', address_list[INDEX]['cep']],
]

for field in fields:
    search = page.find_element_by_id(field[0])
    search.send_keys(field[1])
    # time.sleep(0.5)

# button = page.find_element_by_id('id_submit')
button = page.find_element_by_class_name('btn-primary')
button.click()

page.quit()
