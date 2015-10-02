# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

ffox = webdriver.Firefox()
ffox.get('http://localhost:8000/work/add/')

# pegar o campo de busca onde podemos digitar algum termo
search = ffox.find_element_by_id('id_username')
search.send_keys('admin')

search = ffox.find_element_by_id('id_password')
search.send_keys('admin')

button = ffox.find_element_by_class_name('grp-button')
button.click()

# pegar o campo de busca onde podemos digitar algum termo
campo_busca = ffox.find_element_by_id('id_name_work')
campo_busca.send_keys('Ed. Faria Lima')

campo_busca = ffox.find_element_by_id('id_person')
campo_busca.send_keys('Regis da Silva')

campo_busca = ffox.find_element_by_id('id_customer')
campo_busca.send_keys('Hochtief')

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

button = ffox.find_element_by_id('id_submit')
button.click()
