def parse_intent(text):
    text = text.lower()

    command = None
    layout = None

    if "youtube" in text:
        command = "youtube"

    elif "vscode" in text:
        command = "vscode"

    elif "chrome" in text:
        command = "chrome"

    elif "nextjs" in text:
        command = "nextjs"

    if "kanan" in text:
        layout = "right"

    elif "kiri" in text:
        layout = "left"

    return {
        "command": command,
        "layout": layout
    }