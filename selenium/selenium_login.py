# -*- coding: utf-8 -*-
from selenium import webdriver
# from selenium.webdriver.common.keys import Keys

page = webdriver.Chrome(executable_path='/home/rg3915/Downloads/chromedriver')
# page = webdriver.Firefox()
page.get('http://localhost:8000/admin/login/')

# pegar o campo de busca onde podemos digitar algum termo
campo_busca = page.find_element_by_id('id_username')
campo_busca.send_keys('admin')

campo_busca = page.find_element_by_id('id_password')
campo_busca.send_keys('demodemo')

# button = page.findElement(By.cssSelector("input[type='submit']"))
button = page.find_element_by_xpath("//input[@type='submit']")
button.click()
