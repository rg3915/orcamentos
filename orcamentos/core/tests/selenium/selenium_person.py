import time
from random import randint
from gen_names import gen_male_first_name, gen_female_first_name, gen_last_name
from gen_random_values import gen_cpf, gen_timestamp, gen_phone
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

# page = webdriver.Firefox()
page = webdriver.Chrome(executable_path='/home/rg3915/Downloads/chromedriver')
page.maximize_window()
time.sleep(0.5)
page.get('http://localhost:8000/person/add/')

search = page.find_element_by_id('id_username')
search.send_keys('regis')

search = page.find_element_by_id('id_password')
search.send_keys('1')

button = page.find_element_by_xpath("//input[@type='submit']")
button.click()

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

email = '{}.{}@example.com'.format(first_name[0].lower(), last_name.lower())

search = page.find_element_by_id(gender)
search.click()

fields = [
    ['id_treatment', treatment],
    ['id_first_name', first_name],
    ['id_last_name', last_name],
    ['id_company', 'Soan'],
    ['id_department', 'Financeiro'],
    ['id_occupation', 'Estagiário'],
    ['id_email', email],
    ['id_phone1', gen_phone()],
    ['id_phone2', gen_phone()],
    ['id_phone3', gen_phone()],
    ['id_cpf', gen_cpf()],
    ['id_rg', '73552210'],
    ['id_address', 'Rua Verde, 132'],
    ['id_complement', 'Apto 303'],
    ['id_district', 'Centro'],
    ['id_city', 'São Paulo'],
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
