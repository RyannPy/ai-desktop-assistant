def parse_intent(text: str):
    text = text.lower()

    if "vscode" in text:
        return "vscode"
    
    if "chrome" in text:
        return "chrome"
    
    if "notepad" in text:
        return "notepad"
    
    return None
