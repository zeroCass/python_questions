import pyautogui
import keyboard
import os
import time
from mouse_control import mouse_info

pyautogui.PAUSE = 5
WIDTH = 800
HEIGHT = 1080
img_folder = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'img')



print('ctrl + x to exit.')
last_time = time.time()

while not keyboard.is_pressed('ctrl + x'):

    if time.time() - last_time >= 3:
        last_time = time.time()
    
        if pyautogui.locateOnScreen(os.path.join(img_folder, 'wpp_inital_screen.png'), confidence=0.5):
            print('Found wpp on screen')
            btn_location = pyautogui.locateOnScreen(os.path.join(img_folder, 'wpp_search.png'), confidence=0.5)
            if not btn_location:
                continue

            pyautogui.click(btn_location[0] + 100, btn_location[1] + 20, duration=0.25)
            time.sleep(0.5)
            print('Clicked on search')
            #mouse_info()
            keyboard.write('May')
            time.sleep(5)
            keyboard.send('enter')
            time.sleep(5)

            may = pyautogui.locateOnScreen(os.path.join(img_folder, 'wpp_may.png'), confidence=0.5)
            if may:
                pyautogui.moveTo(may[0], may[1], duration=0.25)
                pyautogui.click()
                type_screen = pyautogui.locateOnScreen(os.path.join(img_folder, 'wpp_type.png'), confidence=0.5)
                if type_screen:
                    print('Found chat')
                    pyautogui.moveTo(type_screen[0] + 130, type_screen[1] + 30, duration=0.25)
                    pyautogui.click()
                    
                    if pyautogui.locateOnScreen(os.path.join(img_folder, 'wpp_may_chat.png'), confidence=0.5):
                        keyboard.write('Eu te amo')
                        time.sleep(5)
                        keyboard.send('enter')



        else:
            print('Nothing found')


print('program shutdown by user.')