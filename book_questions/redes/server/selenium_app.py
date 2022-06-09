from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import sys
#import win32com.client as comclient


#PATH = 'C:\Program Files (x86)\chromedriver.exe'
PATH = r'C:\Users\05694223101\AppData\Roaming\Python\Python310\chromedriver.exe'
MAIN_PAGE = 'https://10.233.87.11:631/jobs/'
options = webdriver.ChromeOptions()
options.add_argument('--headless')
options.add_argument('--ignore-certificate-errors')
options.add_argument('--allow-running-insecure-content')
options.add_argument('--window-size=1920,1080')
options.add_argument('--ignore-ssl-errors')
options.add_argument('--disable-extensions')
options.add_argument('--disable-dev-shm-usage')
options.add_argument('--no-sandbox')
options.add_argument('--disable-gpu')
options.add_argument('--start-maximized')
options.add_argument('--proxy-bypass-list=*')
options.add_argument("--proxy-server='direct://'")
driver = webdriver.Chrome(PATH, options=options)
driver.get(MAIN_PAGE)

# list to control the previous page[0] and the current page[1]
url_control = ['', MAIN_PAGE]
AUTHENT = False
MAIN_BTN_XPATH = '/html/body/table/tbody/tr[1]/td/table[1]/tbody/tr[1]/td[6]'


def goto(current_page, btn_xpath):
    driver.find_element(By.XPATH, btn_xpath).click()
    while driver.find_element(By.TAG_NAME, 'html').id == current_page.id:
        time.sleep(1)
    # try:
    #     elem = driver.find_element(By.XPATH, '/html/body/table/tbody/tr[1]/td/p').text
    #     print(elem) 
    #     WebDriverWait(driver, 10).until(EC.presence_of_element_located(By.XPATH, '/html/body/table/tbody/tr[1]/td/p'))
    #     print('LOCATED ID')
    # except:
    #     print('ID NOT FOUND')
    #     sys.exit(1)



def modify_url_printer():
    global driver
    select_elem = driver.find_element(By.XPATH, '/html/body/table/tbody/tr[1]/td/div[1]/form[2]/select')
    select_obj = Select(select_elem)
    driver.get_screenshot_as_file('screenshot9.png')
    select_obj.select_by_value('modify-printer')
    driver.get_screenshot_as_file('screenshot10.png')
    if not check_authn():
        return False
    return True
    


    
def remove_auth(string: str):
    if '@'  in string:
        string = string.split('@')
        return 'https://' + string[1]
    return string


# def change_url():
#     # w = comclient.Dispatch('WScript.Shell')
#     # w.AppActivate('Chrome')
#     # w.sendkeys('^l')
#     # w.sendkeys(url)
#     # print(url)
#     # w.sendkeys('{ENTER}')


def check_authn():
    global AUTHENT
    print(driver.title, driver.current_url)
    if not(len(driver.title) > 1) and not AUTHENT:
        print('Authentication...')
        driver.get_screenshot_as_file('auth.png')
        url = driver.current_url
        url = url.split('//')
        print(url)
        url[1] = 'root:redhat@' + url[1]
        url = '//'.join(url)
        AUTHENT = True
        driver.get(url)
        driver.find_element(By.XPATH, '/html/body/table/tbody/tr[1]/td/table[1]/tbody/tr[1]/td[6]').click()
        return False
    return True

    

        


try:
    while True:
        # debug propurse
        print(f'\nname: {driver.title}')

        if driver.title == 'Erro de privacidade':
            driver.find_element(By.ID, 'details-button').click()
            driver.find_element(By.ID, 'proceed-link').click()

        # check for authentication
        check_authn()

        if driver.current_url == MAIN_PAGE:
            print('---------------------------------------------------')
            
            printer = {}
            jobs_num = driver.find_element(By.XPATH, '/html/body/table/tbody/tr[1]/td/p').text
            jobs_num = int(jobs_num.split()[1])
            print(f'number of jobs: {jobs_num}')

            for tr in range(1, jobs_num + 1):

                printer['name'] = driver.find_element(By.XPATH, f'/html/body/table/tbody/tr[1]/td/table[2]/tbody/tr[{tr}]/td[1]').text
                printer['href'] = driver.find_element(By.XPATH, f'/html/body/table/tbody/tr[1]/td/table[2]/tbody/tr[{tr}]/td[1]/a').get_attribute('href')
                printer['state'] = driver.find_element(By.XPATH, f'/html/body/table/tbody/tr[1]/td/table[2]/tbody/tr[{tr}]/td[6]').text
                
        
                # driver.execute_script("window.open('')")
                # driver.switch_to.window(driver.window_handles[-1])
                #driver.get(printer['href'])
                driver.get_screenshot_as_file('screenshot.png')
                current_page = driver.find_element(By.TAG_NAME, 'html')
                goto(current_page, f'/html/body/table/tbody/tr[1]/td/table[2]/tbody/tr[{tr}]/td[1]/a')
                driver.get_screenshot_as_file('screenshot0.png')

                if not(modify_url_printer()):
                    print('NOT SUCESSED')
                    
                    #driver.get(printer['href'])

                time.sleep(5)

                driver.get_screenshot_as_file('screenshot1.png')
                print('GOING TO {}'.format(MAIN_PAGE))
                current_page = driver.find_element(By.TAG_NAME, 'html')
                goto(current_page, MAIN_BTN_XPATH)


                #driver.find_element(By.XPATH, '/html/body/table/tbody/tr[1]/td/table[1]/tbody/tr[1]/td[6]').click()
                # driver.close()
                # driver.switch_to.window(driver.window_handles[0])
                

            
except KeyboardInterrupt as e:
    print('Done')
    driver.quit()
