# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
# from generate_random_values import *
# from list_firstname import get_firstname
# from list_lastname import get_lastname
# from list_cep import get_cep
# from list_email import get_email
# from cep import Correios

# chrome = webdriver.Chrome(executable_path='/home/rg3915/Downloads/chromedriver')
ffox = webdriver.Firefox()
ffox.get('http://localhost:8000/person/add/')

# pegar o campo de busca onde podemos digitar algum termo
search = ffox.find_element_by_id('id_username')
search.send_keys('admin')

search = ffox.find_element_by_id('id_password')
search.send_keys('admin')

button = ffox.find_element_by_class_name('grp-button')
button.click()

# nome = get_firstname()
# email = nome.lower() + get_email()

# ncep = get_cep()
# c = Correios()
# r = c.consulta(ncep, primeiro=True)

# pegar o campo de busca onde podemos digitar algum termo
campo_busca = ffox.find_element_by_id('id_treatment')
campo_busca.send_keys('sr')

campo_busca = ffox.find_element_by_id('id_first_name')
campo_busca.send_keys('Bianca')

campo_busca = ffox.find_element_by_id('id_last_name')
campo_busca.send_keys('Soares')  # get_lastname()

campo_busca = ffox.find_element_by_id('id_company')
campo_busca.send_keys('Soan')

campo_busca = ffox.find_element_by_id('id_department')
campo_busca.send_keys('Financeiro')

campo_busca = ffox.find_element_by_id('id_occupation')
campo_busca.send_keys('Estagiário')

campo_busca = ffox.find_element_by_id('id_email')
campo_busca.send_keys('bianca@soan.com')

campo_busca = ffox.find_element_by_id('id_phone1')
campo_busca.send_keys('10 1234-5678')  # str(generate_phone())

campo_busca = ffox.find_element_by_id('id_phone2')
campo_busca.send_keys('10 1234-5679')

campo_busca = ffox.find_element_by_id('id_phone3')
campo_busca.send_keys('10 1234-5680')

campo_busca = ffox.find_element_by_id('id_cpf')
campo_busca.send_keys('11156358329')  # str(generate_cpf())

campo_busca = ffox.find_element_by_id('id_rg')
campo_busca.send_keys('73552210')

campo_busca = ffox.find_element_by_id('id_address')
campo_busca.send_keys('Rua Verde, 132')  # r['Logradouro']

campo_busca = ffox.find_element_by_id('id_complement')
campo_busca.send_keys('Apto 303')

campo_busca = ffox.find_element_by_id('id_district')
campo_busca.send_keys('Centro')  # r['Bairro']

campo_busca = ffox.find_element_by_id('id_city')
campo_busca.send_keys(u'São Paulo')  # r['Localidade']

campo_busca = ffox.find_element_by_id('id_uf')
campo_busca.send_keys('SP')  # r['UF']

campo_busca = ffox.find_element_by_id('id_cep')
campo_busca.send_keys('01200100')  # r['CEP']

button = ffox.find_element_by_class_name('btn-primary')
button.click()
