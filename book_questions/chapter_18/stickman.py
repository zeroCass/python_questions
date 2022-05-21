import pyautogui
import keyboard
import os
import time

pyautogui.PAUSE = 1

img_folder = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'img')

print('ctrl + c to exit')
while True:
    if keyboard.is_pressed('ctrl+c'):
        print('program shutdown by ctrl + c')
        break
    #print(pyautogui.displayMousePosition())
    if pyautogui.locateOnScreen(os.path.join(img_folder, 'luffy.png'), confidence=0.5):
        print('I can see the luffy on screen')
        time.sleep(0.5)
    elif pyautogui.locateOnScreen(os.path.join(img_folder, 'zoro.png'), confidence=0.5):
        print('I can see the zoro on screen')
        time.sleep(0.5)
    else:
        print('I see anything important on screen')
        time.sleep(0.5)