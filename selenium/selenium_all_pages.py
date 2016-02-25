import time
from selenium import webdriver
# from selenium.webdriver.common.keys import Keys

# page = webdriver.Firefox()
page = webdriver.Chrome(executable_path='/home/rg3915/Downloads/chromedriver')
page.maximize_window()
time.sleep(0.5)

pages = [
    'http://localhost:8000/',
    'http://localhost:8000/proposal/entry/',
    'http://localhost:8000/proposal/entry/1/',
    'http://localhost:8000/proposal/entry/1/json/',
    'http://localhost:8000/proposal/entry/add/',
    'http://localhost:8000/proposal/proposal/',
    'http://localhost:8000/proposal/proposal/1/',
    'http://localhost:8000/proposal/contract/',
    'http://localhost:8000/proposal/contract/1/',
    'http://localhost:8000/crm/customer/',
    # 'http://localhost:8000/crm/customer/1/',
    'http://localhost:8000/crm/customer/add/',
    'http://localhost:8000/proposal/work/',
    # 'http://localhost:8000/proposal/work/1/',
    'http://localhost:8000/proposal/work/add/',
    'http://localhost:8000/crm/person/',
    # 'http://localhost:8000/crm/person/1/',
    'http://localhost:8000/crm/person/add/',
]

for p in pages:
    page.get(p)
    print(p)
    time.sleep(1)

print('Done')
