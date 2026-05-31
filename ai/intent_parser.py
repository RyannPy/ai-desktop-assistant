def parse_intent(text: str):
    text = text.lower()

    tasks = []

    if "youtube" in text:
        tasks.append({
            "command": "youtube",
            "layout": None
        })

    if "vscode" in text:
        tasks.append({
            "command": "vscode",
            "layout": None
        })

    if "chrome" in text:
        tasks.append({
            "command": "chrome",
            "layout": None
        })

    if "nextjs" in text:
        tasks.append({
            "command": "nextjs",
            "layout": None
        })

    return tasks