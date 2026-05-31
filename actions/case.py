import subprocess
import webbrowser
import time
import pyautogui

def execute_action(action):
    action_type = action["type"]

    match action_type:
        case "open_app":
            subprocess.Popen(action["app"], shell=True)

        case "open_url":
            webbrowser.open(action["url"])

        case "open_folder":
            subprocess.Popen(f'explorer "{action["path"]}"')

        case "delay":
            time.sleep(action["seconds"])

        case "hotkey":
            pyautogui.hotkey(*action["keys"])

        case _:
            print(f"Unknown action: {action_type}")
    