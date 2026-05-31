from commands.registry import VALID_COMMANDS

def parse_intent(text: str):

    words = text.lower().split()

    tasks = []

    current_command = None

    for word in words:

        if word in VALID_COMMANDS:

            current_command = {
                "command": word,
                "layout": None
            }

            tasks.append(current_command)

        elif word == "kiri":

            if current_command:
                current_command["layout"] = "left"

        elif word == "kanan":

            if current_command:
                current_command["layout"] = "right"

    return tasks