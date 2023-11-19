import time
import pyautogui

message = "suppp"

nth = 100

for i in range(nth):
    pyautogui.typewrite(message + '\n')