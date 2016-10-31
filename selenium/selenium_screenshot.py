import time
from decouple import config
from selenium import webdriver

HOME = config('HOME')
# page = webdriver.Firefox()
page = webdriver.Chrome(executable_path=HOME + '/chromedriver/chromedriver')
page.maximize_window()
time.sleep(0.5)

page.get('http://localhost:8000/')
time.sleep(1)
page.save_screenshot('img/index.png')

page.get('http://localhost:8000/inscricao/')
time.sleep(1)
page.save_screenshot('img/inscricao.png')

page.get('http://localhost:8000/bemvindo/')
time.sleep(1)
page.save_screenshot('img/bemvindo.png')

page.get('http://localhost:8000/dashboard/')
time.sleep(3)
page.save_screenshot('img/dashboard.png')

page.get('http://localhost:8000/status/')
time.sleep(1)
page.save_screenshot('img/status.png')

page.get('http://localhost:8000/crm/person/')
time.sleep(1)
page.save_screenshot('img/person_list.png')

page.get('http://localhost:8000/crm/person/add/')
search = page.find_element_by_id('id_username')
search.send_keys('regis')

search = page.find_element_by_id('id_password')
search.send_keys('1')

button = page.find_element_by_xpath("//input[@type='submit']")
button.click()

time.sleep(1)
page.save_screenshot('img/person_form.png')

page.get('http://localhost:8000/crm/person/regis-da-silva/edit/')
time.sleep(1)
page.save_screenshot('img/person_update.png')

page.get('http://localhost:8000/crm/person/regis-da-silva/')
time.sleep(1)
page.save_screenshot('img/person_detail.png')

page.get('http://localhost:8000/crm/customer/')
time.sleep(1)
page.save_screenshot('img/customer_list.png')

page.get('http://localhost:8000/crm/customer/add/')
time.sleep(1)
page.save_screenshot('img/customer_form.png')

page.get('http://localhost:8000/crm/customer/eugene-johnson/edit/')
time.sleep(1)
page.save_screenshot('img/customer_update.png')

page.get('http://localhost:8000/crm/customer/eugene-johnson/')
time.sleep(1)
page.save_screenshot('img/customer_detail.png')

page.get('http://localhost:8000/crm/employee/add/')
time.sleep(1)
page.save_screenshot('img/employee_form.png')

page.get('http://localhost:8000/proposal/entry/')
time.sleep(1)
page.save_screenshot('img/entry_list.png')

page.get('http://localhost:8000/proposal/entry/1/')
time.sleep(1)
page.save_screenshot('img/entry_detail.png')

page.get('http://localhost:8000/proposal/entry/1/edit/')
time.sleep(1)
page.save_screenshot('img/entry_update.png')

page.get('http://localhost:8000/proposal/entry/add/')
time.sleep(1)
page.save_screenshot('img/entry_form.png')

page.get('http://localhost:8000/proposal/proposal/')
time.sleep(1)
page.save_screenshot('img/proposal_list.png')

page.get('http://localhost:8000/proposal/proposal/42/')
time.sleep(1)
page.save_screenshot('img/proposal_detail.png')

page.get('http://localhost:8000/proposal/proposal/42/edit/')
time.sleep(1)
page.save_screenshot('img/proposal_update.png')

page.get('http://localhost:8000/proposal/contract/')
time.sleep(1)
page.save_screenshot('img/contract_list.png')

page.get('http://localhost:8000/proposal/contract/6/')
time.sleep(1)
page.save_screenshot('img/contract_detail.png')

page.get('http://localhost:8000/proposal/contract/6/edit/')
time.sleep(1)
page.save_screenshot('img/contract_update.png')

page.get('http://localhost:8000/proposal/work/')
time.sleep(1)
page.save_screenshot('img/work_list.png')

page.get('http://localhost:8000/proposal/work/add/')
time.sleep(1)
page.save_screenshot('img/work_form.png')

page.get('http://localhost:8000/proposal/work/boavista-shopping/edit/')
time.sleep(1)
page.save_screenshot('img/work_update.png')

page.get('http://localhost:8000/proposal/work/boavista-shopping/')
time.sleep(1)
page.save_screenshot('img/work_detail.png')

page.quit()
