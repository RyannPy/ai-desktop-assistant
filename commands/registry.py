import json
import os

# Get the path to commands.json which is located in the root directory
# (one level up from the commands folder)
_current_dir = os.path.dirname(os.path.abspath(__file__))
_root_dir = os.path.dirname(_current_dir)
_commands_file = os.path.join(_root_dir, 'commands.json')

COMMANDS = {}
WINDOW_ALIASES = {}

try:
    with open(_commands_file, 'r', encoding='utf-8') as f:
        _data = json.load(f)
        
    for key, value in _data.items():
        # Preserve original structure where COMMANDS[key] is a list of actions
        COMMANDS[key] = [value["action"]]
        WINDOW_ALIASES[key] = value["window_alias"]

except FileNotFoundError:
    print(f"Error: {_commands_file} not found. Please create it.")
except json.JSONDecodeError:
    print(f"Error: {_commands_file} contains invalid JSON.")
except Exception as e:
    print(f"Error loading commands: {e}")