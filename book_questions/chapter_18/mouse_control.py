import pyautogui
import keyboard
import time
pyautogui.PAUSE = 1         # this pause the automation to the user assume the control
pyautogui.FAILSAFE = True   # if the mouse goes out the screen, the program will fail




def mouse_square():
    pyautogui.moveTo(100, 100, duration=0.25)
    pyautogui.moveTo(200, 100, duration=0.25)
    pyautogui.moveTo(200, 200, duration=0.25)
    pyautogui.moveTo(100, 200, duration=0.25)
    pyautogui.moveTo(100, 100, duration=0.25)

def mouse_info():
    print(pyautogui.position())


def main():
    while not keyboard.is_pressed('ctrl+x'):
        time.sleep(1)
        mouse_info()

if __name__ == '__main__':
    main()
