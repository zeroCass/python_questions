from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.alert import Alert
import time

PATH = 'C:\Program Files (x86)\chromedriver.exe'
driver = webdriver.Chrome(PATH)
#driver.get('https://www.hyrtutorials.com/p/alertsdemo.html')
#driver.get('https://admin:admin@the-internet.herokuapp.com/basic_auth')
driver.get('https://the-internet.herokuapp.com/')
current_url = 'https://the-internet.herokuapp.com/'


try:
    while True:
        try:
            alert = Alert(driver)
            print(alert.text)
            time.sleep(3)
            #alert.accept()
        except:
            pass
        if current_url != driver.current_url:
            url = driver.current_url
            url_list = url.split('//')
            url_list[1] = 'admin:admin@' + url_list[1]
            url = '//'.join(url_list)
            current_url = url
            driver.get(url)

except KeyboardInterrupt as e:
    print('Done')