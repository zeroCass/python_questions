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
MAIN_PAGE = 'https://10.233.87.11:631/jobs/'
options = webdriver.ChromeOptions()
options.add_argument('--headless')
options.add_argument('--ignore-certificate-errors')
options.add_argument('--ignore-ssl-errors')
driver = webdriver.Chrome(PATH, options=options)
driver.get(MAIN_PAGE)

# list to control the previous page[0] and the current page[1]
url_control = ['', MAIN_PAGE]
AUTHENT = False

try:
    while True:
        # debug propurse
        print(f'\nname: {driver.title}')


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
        
        table = driver.find_elements(By.XPATH, '/html/body/table/tbody/tr[1]/td/table[2]/tbody/tr')
        '/html/body/table/tbody/tr[1]/td/table[2]/tbody/tr[2]'
        for count, row in enumerate(table):
            print(f'{count}: {row.text}')

            
except KeyboardInterrupt as e:
    print('Done')
    driver.quit()