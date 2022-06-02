from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.alert import Alert
import time
import win32com.client as comclient



def remove_auth(string: str):
    if '@'  in string:
        string = string.split('@')
        return 'https://' + string[1]
    return string

#PATH = 'C:\Program Files (x86)\chromedriver.exe'
PATH = r'C:\Users\05694223101\AppData\Roaming\Python\Python310\chromedriver.exe'
MAIN_PAGE = 'https://10.233.87.11:631/admin'
driver = webdriver.Chrome(PATH)
#driver.get('https://www.hyrtutorials.com/p/alertsdemo.html')
#driver.get('https://admin:admin@the-internet.herokuapp.com/basic_auth')
driver.get(MAIN_PAGE)

# list to control the previous page[0] and the current page[1]
url_control = ['', MAIN_PAGE]
AUTHENT = False

try:
    while True:
        # debug propurse
        print(f'name: {driver.title}')

        if not(len(driver.title) > 1) and not AUTHENT:
            print('Authentication...')
            #time.sleep(3)
            url = driver.current_url
            url = url.split('//')
            print(url)
            url[1] = 'root:redhat@' + url[1]
            url = '//'.join(url)
            AUTHENT = True
            driver.get(url)

            # w = comclient.Dispatch('WScript.Shell')
            # w.AppActivate('Chrome')
            # w.sendkeys('^l')
            # w.sendkeys(url)
            # print(url)
            # w.sendkeys('{ENTER}')
        if driver.title == 'Erro de privacidade':
            driver.find_element(By.ID, 'details-button').click()
            driver.find_element(By.ID, 'proceed-link').click()
            
except KeyboardInterrupt as e:
    print('Done')
    driver.quit()