from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.alert import Alert
import time

options = webdriver.ChromeOptions()
# options.add_argument('--headless')
#options.add_argument('--ignore-certificate-errors')
#options.add_argument('--ignore-ssl-errors')

browser = webdriver.Chrome(executable_path='C:/Users/05694223101/AppData/Local/Programs/Python/Python310/chromedriver.exe', options=options)
#browser.get('http://root:redhat@10.233.87.11:631/printers/BSHRSAM')
browser.get('https://www.google.com')
try: 
    while True:
        #element = browser.find_element(by=By.XPATH, value='/html/body/table/tbody/tr[1]/td/div[1]/form[2]/select/option[2]')
        #print(element.text)
        #element.click()
        try:
            #obj = browser.switch_to.alert()
            alert = Alert(browser)
            print(alert.text)
            print('---alert appears---')
            #obj.send_keys(keysToSend='root\ue004redhat')
            #obj.accept()
        except Exception as e:
            print('Alert not found')
        #print(browser.current_url)

except KeyboardInterrupt:
    print('Done')
    browser.quit()


