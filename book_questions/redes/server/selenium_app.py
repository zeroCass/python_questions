from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import subprocess
import re
import logging
# logging.basicConfig(level=logging.INFO, )

'''
handle release jobs
handle hostname without saude.df.gov.br (check if it is a ubs)
ok handle jobs = 0
ok handle list of jobs decrease
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

# global function
AUTHENT = False
MAIN_BTN_XPATH = '/html/body/table/tbody/tr[1]/td/table[1]/tbody/tr[1]/td[6]'


def goto(current_page, btn_xpath):
    '''this functions take the current_page and the button xpath
    so find the button and click then wait until the url has changed
    '''
    driver.find_element(By.XPATH, btn_xpath).click()
    # this loop is really necessary ?
    while driver.find_element(By.TAG_NAME, 'html').id == current_page.id:
        time.sleep(1)




def ping_printer(hostname):
    '''run the ping command on the console
    returns false if expection was throwed
    obs: this will print the output of the command of console
    if this is no need, use subprocess.call()
    '''
    try:
        subprocess.check_call(['ping', hostname], universal_newlines=True)
        print('Ping sucessed. The host is ONLINE.')
        return True
    except subprocess.CalledProcessError as error:
        print(f'Ping error: {error}')
        return False
    



def cancel_printer_jobs():
    '''find the selection by XPATH then select
    the purge-jobs(cancel jobs) to cancel all jobs of printer
    '''
    global driver

    select_elem = driver.find_element(By.XPATH, '/html/body/table/tbody/tr[1]/td/div[1]/form[1]/select')
    select_obj = Select(select_elem)
    select_obj.select_by_value('purge-jobs')
    


def modify_url_printer(url):
    '''this function will do:
    - find selection on the page and then select it
    - call the check_authn() to make sure that is alreasy authenticated
        - if was not, then return false and nothing happens
    - select radio buttun 'Windows Printer via SAMBA
    - modify printer url, recieve as parameter
    - returns
    '''
    
    # global variable driver (browser)
    global driver

    current_url = driver.current_url
    print(f'current_url: {current_url}, title: {driver.title}')

    # find the selection element - modify-printer
    select_elem = driver.find_element(By.XPATH, '/html/body/table/tbody/tr[1]/td/div[1]/form[2]/select')
    select_obj = Select(select_elem)
    select_obj.select_by_value('modify-printer')
    
    # if was not authn, returns false so the script can redo some the previous steps 
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
    '''remove the authentication keys: user:pass@
    from url, to make comparations more simple
    '''

    print('REMOVE AUTH FUNCTION')
    if '@'  in string:
        string = string.split('@')
        print('REMOVE AUTH: https://' + string[1])
        return 'https://' + string[1]
    return string




def check_authn():
    '''check if the global var AUTHENT is true:
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

    

        

def main():

    driver.get(MAIN_PAGE)
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
                        table_num = 3  # this specify wich table we will serach for in the XPATH's
                    except:
                    # if exist, then the table now it is 3 not 2
                        #'/html/body/table/tbody/tr[1]/td/table[3]/tbody/tr[1]/td[1]/a'
                        table_num = 2
                        
                    printer['name'] = driver.find_element(By.XPATH, f'/html/body/table/tbody/tr[1]/td/table[{table_num}]/tbody/tr[{tr}]/td[1]').text
                    printer['href'] = driver.find_element(By.XPATH, f'/html/body/table/tbody/tr[1]/td/table[{table_num}]/tbody/tr[{tr}]/td[1]/a').get_attribute('href')
                    printer['state'] = driver.find_element(By.XPATH, f'/html/body/table/tbody/tr[1]/td/table[{table_num}]/tbody/tr[{tr}]/td[6]').text

                    
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
                    

                    # call modify_url_printer to make the proper change
                    modified = modify_url_printer(printer['url_set'])
                    print('Url modifed with sucess') if modified  else print('Url modifed FAIL')
                    
                    ping_status = False
                    if modified: ping_status = ping_printer(printer['hostname'])
                    
                    print(f'DRIVER TITLE: {driver.title}\nSLEEPING FOR 3 SECONDS')
                    time.sleep(3)  
                    printer_name_regex = ''
                    # the sleep is for wait for the browser returns to the main page of the printer
                    if driver.title != 'Jobs - CUPS 1.6.3' and driver.title != 'Modify Printer - CUPS 1.6.3':
                        print('ENTROU CONDICAO: ')
                        # create a regex for exclude the numbers of printers name
                        regex = re.compile(r'(\w+)(-\w+)?-(\w+)')
                        printer_name_regex = regex.search(printer['name'])
                        # if printer group is not none, we have to concatenate the name
                        if printer_name_regex.group(2) is None:
                            printer_name_regex = printer_name_regex.group(1)
                        else:
                            printer_name_regex = printer_name_regex.group(1) + printer_name_regex.group(2)


                    print('DEBUG: regex> {} / printername> {}\n'.format(printer_name_regex, printer['name'])) 
                    # cehck if the printer pc is offline, if it is, cancell all jobs
                    if not ping_status and modified and printer_name_regex in driver.title:
                        print('ENTROU CANCELAR JOBS')
                        # if ping faild and url was modiefied, then cancell all jobs
                        cancel_printer_jobs()
                        print('{}: all jobs cancelled.'.format(printer['name']))
                                                

                    print('GOING TO MAIN: {}'.format(MAIN_PAGE))
                    current_page = driver.find_element(By.TAG_NAME, 'html')
                    goto(current_page, MAIN_BTN_XPATH)

                    # get the number of current jobs stuck in the queue
                    jobs_num = driver.find_element(By.XPATH, '/html/body/table/tbody/tr[1]/td/p').text
                    # if there is no jobs, nothing happens, skip the logic
                    if jobs_num == 'No jobs.':
                        break
                    jobs_num = int(jobs_num.split()[1])
                    # if the table is greather than number of jobs, quit the loop
                    if tr > jobs_num:
                        break
                    

                
    except KeyboardInterrupt as e:
        print('Done')
        driver.quit()


main()