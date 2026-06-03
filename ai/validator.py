from commands.registry import COMMANDS

VALID_COMMANDS = set(COMMANDS.keys())

VALID_LAYOUTS = {
    None,
    "left",
    "right"
}

def validate_tasks(tasks):

    valid_tasks = []

    for task in tasks:

        command = task.get("command")
        layout = task.get("layout")
        desktop = task.get("desktop", 1)

        if command not in VALID_COMMANDS:
            continue

        if layout not in VALID_LAYOUTS:
            layout = None

        valid_tasks.append({
            "command": command,
            "layout": layout,
            "desktop": desktop
        })

    return valid_tasks