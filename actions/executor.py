from actions.case import execute_action
from commands.registry import COMMANDS

def run_command(cmd_key: str):
    actions = COMMANDS.get(cmd_key)

    if not actions:
        return "Command tidak ditemukan"
    
    for action in actions:
        execute_action(action)

    return f"Berhasil menjalankan {cmd_key}"