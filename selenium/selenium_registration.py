import time
from random import randint, choice
from gen_names import gen_male_first_name, gen_female_first_name, gen_last_name
from gen_random_values import gen_cpf, gen_rg, gen_phone
from selenium import webdriver

# page = webdriver.Firefox()
page = webdriver.Chrome(executable_path='/home/rg3915/Downloads/chromedriver')
page.maximize_window()
time.sleep(0.5)
page.get('http://localhost:8000/registration/')

g = randint(0, 1)

if g:
    dict_ = gen_female_first_name()
else:
    dict_ = gen_male_first_name()

first_name = dict_['first_name'].lower()
# last_name = gen_last_name()
print(first_name)

email = '{}@example.com'.format(first_name.lower())

fields = [
    ['id_username', first_name],
    ['id_email', email],
    ['id_password', 'demodemo'],
]

for field in fields:
    search = page.find_element_by_id(field[0])
    search.send_keys(field[1])

# button = page.find_element_by_id('id_submit')
button = page.find_element_by_class_name('btn-primary')
button.click()

page.quit()
