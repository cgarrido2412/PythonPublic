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
    pyautogui.typewrite('chrome')
    time.sleep(5)
    pyautogui.moveTo(225, 512, duration=0.25)
    pyautogui.click()
    time.sleep(5)
    pyautogui.typewrite('https://youtu.be/dQw4w9WgXcQ')
