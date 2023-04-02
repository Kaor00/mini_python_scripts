import pyautogui


screenWidth, screenHeight = pyautogui.size()
print(screenWidth, screenHeight)

currentMouseX, currentMouseY = pyautogui.position()
print(currentMouseX, currentMouseY)

pyautogui.moveTo(100, 150)
pyautogui.click()
pyautogui.click(100, 200)
pyautogui.click('button.png')
