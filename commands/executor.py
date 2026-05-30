import subprocess
from .registry import COMMANDS

def run_command(cmd_key: str):
    if cmd_key not in COMMANDS:
        return f"Command `{cmd_key}` tidak dapat dilakukan."
    
    command = COMMANDS[cmd_key]

    try:
        subprocess.Popen(command, shell=True)
        return f"Berhasil menjalankan {cmd_key}"
    except Exception as e:
        print(e)
        return f"Error: {str(e)}"