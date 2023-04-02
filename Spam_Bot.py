import pyautogui
import time


time.sleep(5)

with open("/полный путьt.txt") as file:
    for word in file:
        pyautogui.typewrite(word)
        pyautogui.press("enter")
