import pyautogui
import time
n=int(input('Введите число'))
pyautogui.moveTo(200, 1055)
pyautogui.click()
for step in range(n+1):
    pyautogui.moveTo(200, 1000)
    pyautogui.hotkey('ctrl','t')
