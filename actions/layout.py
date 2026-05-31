import pyautogui

def apply_layout(layout):
    match layout:
        
        case "right":
            pyautogui.hotkey("win", "right")

        case "left":
            pyautogui.hotkey("win", "left")

        case _:
            print(f"Unknown layout: {layout}")