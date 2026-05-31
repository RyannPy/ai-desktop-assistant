import pygetwindow as gw

def get_all_windows():
    return [
        window.title
        for window in gw.getAllWindows()
        if window.title.strip()
    ]

def find_window(keyword: str):
    keyword = keyword.lower()
    for window in gw.getAllWindows():
        title = window.title.lower()

        if keyword in title:
            return window
        
    return None

def focus_window(keyword: str):

    window = find_window(keyword)

    if not window:
        return False

    window.activate()

    return True

def maximize_window(keyword: str):

    window = find_window(keyword)

    if not window:
        return False

    window.maximize()

    return True

def minimize_window(keyword: str):

    window = find_window(keyword)

    if not window:
        return False

    window.minimize()

    return True