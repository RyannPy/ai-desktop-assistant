from ai.validator import VALID_COMMANDS

def parse_intent(text: str):

    words = text.lower().split()

    tasks = []

    current_command = None

    for i, word in enumerate(words):

        if word in VALID_COMMANDS:

            current_command = {
                "command": word,
                "layout": None,
                "desktop": 1
            }

            tasks.append(current_command)

        elif word == "kiri":

            if current_command:
                current_command["layout"] = "left"

        elif word == "kanan":

            if current_command:
                current_command["layout"] = "right"

        elif word == "desktop":
            
            if i + 1 < len(words):
                try:
                    current_command["desktop"] = int(words[i + 1])
                except:
                    pass

    return tasks