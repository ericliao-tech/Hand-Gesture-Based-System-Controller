# system_control.py
import pyautogui

def volume_up():
    for _ in range(5):
        pyautogui.press("volumeup")

def volume_down():
    for _ in range(5):
        pyautogui.press("volumedown")

def scroll_up():
    pyautogui.scroll(300)

def scroll_down():
    pyautogui.scroll(-300)
