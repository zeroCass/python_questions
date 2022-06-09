from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import sys
#import win32com.client as comclient


'''
handle release jobs
handle jobs = 0
'''

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
driver = webdriver.Chrome(PATH)
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



def modify_url_printer(url):
    

    global driver

    current_url = driver.current_url
    print(f'current_url: {current_url}')

    # find the selection element - modify-printer
    select_elem = driver.find_element(By.XPATH, '/html/body/table/tbody/tr[1]/td/div[1]/form[2]/select')
    select_obj = Select(select_elem)
    driver.get_screenshot_as_file('screenshot9.png')
    select_obj.select_by_value('modify-printer')
    driver.get_screenshot_as_file('screenshot10.png')
    
    # if was not authn, returns false so the script can redo some steps 
    if not check_authn():
        return False
    
    if driver.title == 'Modify Printer - CUPS 1.6.3':
        # find radio button
        driver.find_element(By.XPATH, '/html/body/table/tbody/tr[1]/td/div/form/table/tbody/tr[5]/td/input[8]').click()
        # find continue button for validate the selection
        driver.find_element(By.XPATH, '/html/body/table/tbody/tr[1]/td/div/form/table/tbody/tr[6]/td[2]/input').click()
        continue_btn = driver.find_element(By.XPATH, '/html/body/table/tbody/tr[1]/td/div/form/table/tbody/tr[1]/td/input')

        new_url = url + continue_btn.get_attribute('value').split('//')[1]
        print(new_url)

        continue_btn.clear()
        
        continue_btn.send_keys(new_url)
        # find continue button and click
        driver.find_element(By.XPATH, '/html/body/table/tbody/tr[1]/td/div/form/table/tbody/tr[3]/td[2]/input').click()
        driver.find_element(By.XPATH, '/html/body/table/tbody/tr[1]/td/div/form/table/tbody/tr[6]/td[2]/input').click()
        # find modify printer button and click
        driver.find_element(By.XPATH, '/html/body/table/tbody/tr[1]/td/div/form/table/tbody/tr[8]/td[2]/input').click()
        
        # while driver.current_url != remove_auth(current_url):
        #     time.sleep(1)
        print('CHANGED WITH SUCESS')

    return True
    


    
def remove_auth(string: str):
    print('REMOVE AUTH FUNCTION')
    print('@' in string)
    if '@'  in string:
        string = string.split('@')
        print('REMOVE AUTH: https://' + string[1])
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
    '''
        check if the global var AUTHENT is true:
        if it is: returns True indicating that alredy is authenticated
        if it is not: change the url to credencials and authenticate. then go to MAINPAGE (JOBS)
        returns False indicating that was not authenticated yet
    '''


    global AUTHENT
    print(driver.title, driver.current_url)
    if (not(len(driver.title) > 1) or driver.title == 'Unauthorized - CUPS v1.6.3') and not AUTHENT:
        print('Authentication...')
        driver.get_screenshot_as_file('auth.png')
        url = driver.current_url
        url = url.split('//')
        print(url)
        url[1] = 'root:redhat@' + url[1]
        url = '//'.join(url)
        AUTHENT = True
        driver.get(url)

        # find the button JOBS and click. Now the scripts are AUTHeNTICATED, i can use driver.get(url) anymore
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

        if remove_auth(driver.current_url) == MAIN_PAGE:
            print('---------------------------------------------------')
            
            printer = {}
            # get the number of current jobs stuck in the queue
            jobs_num = driver.find_element(By.XPATH, '/html/body/table/tbody/tr[1]/td/p').text
            
            # if there is no jobs, nothing happens, skip the logic
            if jobs_num == 'No jobs.':
                print(jobs_num)
                continue
            
            jobs_num = int(jobs_num.split()[1])
            print(f'number of jobs: {jobs_num}')
            #table_num = 2
            for tr in range(1, jobs_num + 1):
                
                # chek if exists more than one page
                try:
                    driver.find_element(By.XPATH, '/html/body/table/tbody/tr[1]/td/table[2]/tbody/tr/td[2]/form/input[5]').size != 0
                    table_num = 3
                except:
                # if exist, then the table now it is 3 not 2
                    #'/html/body/table/tbody/tr[1]/td/table[3]/tbody/tr[1]/td[1]/a'
                    table_num = 2
                    
                printer['name'] = driver.find_element(By.XPATH, f'/html/body/table/tbody/tr[1]/td/table[{table_num}]/tbody/tr[{tr}]/td[1]').text
                printer['href'] = driver.find_element(By.XPATH, f'/html/body/table/tbody/tr[1]/td/table[{table_num}]/tbody/tr[{tr}]/td[1]/a').get_attribute('href')
                printer['state'] = driver.find_element(By.XPATH, f'/html/body/table/tbody/tr[1]/td/table[{table_num}]/tbody/tr[{tr}]/td[6]').text

                
                # driver.execute_script("window.open('')")
                # driver.switch_to.window(driver.window_handles[-1])
                #driver.get(printer['href'])
                
                driver.get_screenshot_as_file('screenshot.png')
                current_page = driver.find_element(By.TAG_NAME, 'html')
                # go to printer page
                goto(current_page, f'/html/body/table/tbody/tr[1]/td/table[2]/tbody/tr[{tr}]/td[1]/a')
                
                # get the hostname of the printer
                printer['hostname'] = driver.find_element(By.XPATH, '/html/body/table/tbody/tr[1]/td/div[1]/table/tbody/tr[4]/td').text.split('/')[2]
                # based on domain, change the url settings
                if 'saude.df.gov.br' in printer['hostname']:
                    printer['url_set'] = r'smb://saude\user_print:trakcare@'
                else:
                    printer['url_set'] = r'smb://ihb.local\user_print:trakcare@'
                print(printer['hostname'])
                driver.get_screenshot_as_file('screenshot0.png')

                if not(modify_url_printer(printer['url_set'])):
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
