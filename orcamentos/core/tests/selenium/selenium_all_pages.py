# -*- coding: utf-8 -*
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

# page = webdriver.Firefox()
page = webdriver.Chrome(executable_path='/home/rg3915/Downloads/chromedriver')
page.maximize_window()
time.sleep(0.5)
page.get('http://localhost:8000/')
print('index OK')
time.sleep(1)

page.get('http://localhost:8000/entry/')
print('entry/')
time.sleep(1)
page.get('http://localhost:8000/entry/1/')
print('entry/1/')
time.sleep(1)
page.get('http://localhost:8000/entry/1/json/')
print('entry/1/json/')
time.sleep(1)

page.get('http://localhost:8000/proposal/')
print('proposal/')
time.sleep(1)
page.get('http://localhost:8000/proposal/1/')
print('proposal/1/')
time.sleep(1)

page.get('http://localhost:8000/contract/')
print('contract/')
time.sleep(1)
page.get('http://localhost:8000/contract/1/')
print('contract/1/')
time.sleep(1)

page.get('http://localhost:8000/customer/')
print('customer/')
time.sleep(1)
page.get('http://localhost:8000/customer/1/')
print('customer/1/')
time.sleep(1)

page.get('http://localhost:8000/work/')
print('work/')
time.sleep(1)
page.get('http://localhost:8000/work/1/')
print('work/1/')
time.sleep(1)

page.get('http://localhost:8000/person/')
print('person/')
time.sleep(1)
page.get('http://localhost:8000/person/1/')
print('person/1/')
print('Done')
