import pyautogui
import time

def prank():
    #to rick roll someone 
    pyautogui.size()

    #Windows button
    #pyautogui.position()
    #Point(x=22, y=1064)
    pyautogui.moveTo(22, 1064, duration=0.25)
    pyautogui.click()
    time.sleep(3)
    pyautogui.typewrite('chrome')
    time.sleep(3)
    pyautogui.moveTo(225, 512, duration=0.25)
    pyautogui.click()
    time.sleep(3)
    pyautogui.typewrite('https://youtu.be/dQw4w9WgXcQ')
    time.sleep(1)
    pyautogui.typewrite(['enter'])

def brave_prank():
    #experimenting with keyboard shortcuts
    pyautogui.typewrite(['winleft'])
    time.sleep(1)
    pyautogui.typewrite('run')
    time.sleep(1)
    pyautogui.typewrite(['enter'])
    time.sleep(1)
    pyautogui.typewrite('brave')
    time.sleep(1)
    pyautogui.typewrite(['enter'])
    time.sleep(1)
    pyautogui.typewrite('https://youtu.be/dQw4w9WgXcQ')
    time.sleep(1)
    pyautogui.typewrite(['enter'])
    time.sleep(1) 
