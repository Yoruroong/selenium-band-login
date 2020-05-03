from selenium import webdriver
import time

driver = webdriver.Chrome("F:\ChromeDriver\chromedriver.exe")

driver.implicitly_wait(0.07)

driver.get('https://auth.band.us/email_login?keep_login=false')

driver.find_element_by_name('email').send_keys('이메일')
driver.find_element_by_css_selector('.uBtn.-tcType.-confirm').click()

driver.find_element_by_name('password').send_keys('비밀번호')
driver.find_element_by_css_selector('.uBtn.-tcType.-confirm').click()
