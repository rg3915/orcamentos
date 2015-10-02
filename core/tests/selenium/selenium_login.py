# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

ffox = webdriver.Firefox()
ffox.get('http://localhost:8000/admin/login/')

# pegar o campo de busca onde podemos digitar algum termo
campo_busca = ffox.find_element_by_id('id_username')
campo_busca.send_keys('admin')

campo_busca = ffox.find_element_by_id('id_password')
campo_busca.send_keys('admin')

button = ffox.find_element_by_class_name('grp-button')
button.click()
