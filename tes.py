from ai.intent_parser import parse_intent

prompt = "Open youtube and vscode"
tasks = parse_intent(prompt)
print(tasks)