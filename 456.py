import pyautogui
import time
a=(1)
for step in range(a):
    pyautogui.moveTo(150, 1055)
    pyautogui.click()
    pyautogui.moveTo(350, 900)
    pyautogui.hotkey('ctrl','shift','n')
    pyautogui.moveTo(400, 550)
    time.sleep(1)
    pyautogui.write('polkjoi')
    pyautogui.hotkey('enter')