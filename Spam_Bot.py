import pyautogui
import time


time.sleep(5)

with open("/home/kaor/PycharmProjects/Qwark/Download_by_PY/Examples/spaming_text.txt") as file:
    for word in file:
        pyautogui.typewrite(word)
        pyautogui.press("enter")
