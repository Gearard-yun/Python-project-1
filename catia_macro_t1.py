import pyautogui
import sys
import time
import keyboard

time.sleep(1)

def macro1():
    for i in range(10):
        pyautogui.hotkey("alt","enter",interval=0.1)
        pyautogui.write("test-massege",interval=0.1)
        pyautogui.press("enter",interval=0.1)


keyboard.add_hotkey("F8", macro1) # 사용자가 F8키를 누르면 매크로 100번시작

keyboard.wait("esc") 