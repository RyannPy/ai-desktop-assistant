import pyautogui
import time

def switch_to_desktop(desktop: int):
    # sementara asumsi mulai dari desktop 1

    pyautogui.hotkey("win", "ctrl", "left")

    time.sleep(0.5)

    pyautogui.hotkey("win", "ctrl", "left")

    time.sleep(0.5)

    pyautogui.hotkey("win", "ctrl", "left")

    time.sleep(0.5)

    for _ in range(desktop - 1):
        pyautogui.hotkey("win", "ctrl", "right")
        time.sleep(0.5)