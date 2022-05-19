


from selenium import webdriver
import time

browser = webdriver.Firefox(executable_path='C:/Users/05694223101/AppData/Local/Programs/Python/Python310/geckodriver.exe')
print(type(browser))
browser.get('http://inventwithpython.com/')

try:
    web_element = browser.find_element_by_class_name('card-img-top')
    print('Found <%s> element with that class name!' % (web_element.tag_name))
except:
    print('Was not able to find an element with that name.')

link_elem = browser.find_element_by_link_text('Read Online for Free')
link_elem.click()


browser.get('https://outlook.live.com/')
sigin = browser.find_element_by_link_text('Entrar')
sigin.click()
email_elem = browser.find_element_by_id('i0116')
email_elem.send_keys('email@outlook.com')
browser.find_element_by_id('idSIButton9').click()
time.sleep(3)
browser.find_element_by_id('idSIButton9').click()
time.sleep(3)
pwd_elem = browser.find_element_by_id('i0118').send_keys('senha123')
time.sleep(3)
browser.find_element_by_id('idSIButton9').click()
