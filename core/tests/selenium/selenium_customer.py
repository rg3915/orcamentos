# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
# import os


# test using selenium with chromedriver
# customer = webdriver.Chrome(executable_path='/home/dhelbegor/workspace/Chromedriver/chromedriver')
customer = webdriver.Firefox()
customer.get('http://localhost:8000/customer/add/')

# pegando o campo de busca e inserindo um customer fake no mesmo.
search = customer.find_element_by_id('id_treatment')
search.send_keys('sr')

search = customer.find_element_by_id('id_first_name')
search.send_keys('Rafael')

search = customer.find_element_by_id('id_last_name')
search.send_keys('Cândido de Morais')  # get_lastname()

search = customer.find_element_by_id('id_company')
search.send_keys('Supertoys')

search = customer.find_element_by_id('id_department')
search.send_keys('Contábil')

search = customer.find_element_by_id('id_email')
search.send_keys('rafael@supertoys.com')

search = customer.find_element_by_id('id_phone1')
search.send_keys('10 1234-5678')  # str(generate_phone())

search = customer.find_element_by_id('id_phone2')
search.send_keys('10 1234-5679')

search = customer.find_element_by_id('id_phone3')
search.send_keys('10 1234-5680')

search = customer.find_element_by_id('id_cpf')
search.send_keys('11156358329')  # str(generate_cpf())

search = customer.find_element_by_id('id_rg')
search.send_keys('73552210')

search = customer.find_element_by_id('id_cnpj')
search.send_keys('10094604000116')

search = customer.find_element_by_id('id_ie')
search.send_keys('1542682213')

search = customer.find_element_by_id('id_type_customer')
search.send_keys('particular')

search = customer.find_element_by_id('id_address')
search.send_keys('Rua Verde, 132')  # r['Logradouro']

search = customer.find_element_by_id('id_complement')
search.send_keys('Apto 303')

search = customer.find_element_by_id('id_district')
search.send_keys('Centro')  # r['Bairro']

search = customer.find_element_by_id('id_city')
search.send_keys(u'São Paulo')  # r['Localidade']

search = customer.find_element_by_id('id_uf')
search.send_keys('SP')  # r['UF']

search = customer.find_element_by_id('id_cep')
search.send_keys('01200100')  # r['CEP']

button = customer.find_element_by_id('id_submit')
button.click()
