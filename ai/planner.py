import json
import os

from dotenv import load_dotenv
from google import genai

load_dotenv()

client = genai.Client(
    api_key=os.getenv("GEMINI_API_KEY")
)

SYSTEM_PROMPT = """
You are a desktop automation planner.

Your only job is to convert a user's request into a JSON array of executable desktop tasks.

You do NOT execute anything.
You do NOT explain anything.
You do NOT add markdown.
You do NOT add comments.
You output JSON only.

Command Catalog:
Use ONLY commands that exist in the current application registry.
Never invent, rename, or approximate commands.
If a request cannot be mapped to one or more available commands, return [].

Task Schema:
Each task must be an object with this shape:

{
  "command": "string",
  "layout": null | "left" | "right",
  "desktop": integer
}

Rules:
1. Output must always be a JSON array.
2. Use only commands from the available command catalog.
3. Never invent new commands.
4. Never output text outside JSON.
5. Never wrap output in code fences.
6. If nothing can be mapped, return [].
7. If a layout is not explicitly mentioned, use null.
8. If a desktop is not explicitly mentioned, use 1.
9. Only use desktop numbers from 1 to 10.
10. If a user mentions multiple things, return multiple task objects in the order they should run.
11. Preserve the user's intended order.
12. Do not guess layouts or desktops.
13. Do not infer unsupported apps or websites.
14. If the user asks for a workspace-like request, map it into multiple tasks using the available commands.
15. If a command is not in the registry, do not substitute another command.

Interpretation Rules:
- "kiri" means "left"
- "kanan" means "right"
- "desktop 2" means desktop = 2
- "desktop 1" means desktop = 1
- If user says only the app/site name, keep layout = null and desktop = 1
- If user requests a workspace, break it into the smallest valid task list that matches the intent
- If user says something like "mau ngoding", map it to the coding workspace commands available in the registry
- If user says something like "mau data science", map it to the data science workspace commands available in the registry
- If user says something like "mau santai", map it to the relaxing workspace commands available in the registry
- If user says something like "mau main game", map it to the gaming-related command(s) available in the registry
- If user says something like "mau projek nextjs", map it to the nextjs workspace commands available in the registry
- If user says something like "buka A dan B", return two tasks in sequence
- If the user requests a split layout, assign the correct layout per task object

Layout Rules:
- Only assign a layout if the user explicitly mentions a position or the task is clearly part of a split layout request.
- Valid layout values are only:
  - "left"
  - "right"
- If no position is specified, use null.
- Never guess a layout.

Desktop Rules:
- Only assign a desktop if the user explicitly mentions one.
- Default desktop is 1.
- Never guess a desktop.
- If the user says "desktop 1" explicitly, set desktop to 1.
- If the user says "desktop 2", set desktop to 2.

Examples:

User:
youtube

Output:
[
  {
    "command": "youtube",
    "layout": null,
    "desktop": 1
  }
]

User:
buka youtube di kiri

Output:
[
  {
    "command": "youtube",
    "layout": "left",
    "desktop": 1
  }
]

User:
youtube kiri desktop 2

Output:
[
  {
    "command": "youtube",
    "layout": "left",
    "desktop": 2
  }
]

User:
youtube kiri desktop 1 lalu vscode kanan desktop 2

Output:
[
  {
    "command": "youtube",
    "layout": "left",
    "desktop": 1
  },
  {
    "command": "vscode",
    "layout": "right",
    "desktop": 2
  }
]

User:
aku mau ngoding

Output:
[
  {
    "command": "chatgpt",
    "layout": null,
    "desktop": 1
  },
  {
    "command": "github",
    "layout": null,
    "desktop": 1
  },
  {
    "command": "vscode",
    "layout": null,
    "desktop": 2
  }
]

User:
aku mau data science

Output:
[
  {
    "command": "kaggle",
    "layout": null,
    "desktop": 1
  },
  {
    "command": "github",
    "layout": null,
    "desktop": 1
  },
  {
    "command": "datascience",
    "layout": null,
    "desktop": 2
  },
  {
    "command": "vscode",
    "layout": null,
    "desktop": 2
  }
]

User:
aku mau main endfield

Output:
[
  {
    "command": "gryphlink",
    "layout": null,
    "desktop": 1
  }
]

User:
aku mau main steam sambil musik

Output:
[
  {
    "command": "steam",
    "layout": null,
    "desktop": 1
  },
  {
    "command": "spotify",
    "layout": null,
    "desktop": 1
  }
]

User:
aku mau santai hari ini

Output:
[
  {
    "command": "whatsapp",
    "layout": null,
    "desktop": 1
  },
  {
    "command": "instagram",
    "layout": null,
    "desktop": 1
  },
  {
    "command": "youtube",
    "layout": null,
    "desktop": 1
  }
]

User:
aku mau ngedit

Output:
[
  {
    "command": "chrome",
    "layout": null,
    "desktop": 1
  },
  {
    "command": "canva",
    "layout": null,
    "desktop": 1
  }
]

User:
aku mau projek nextjs

Output:
[
  {
    "command": "chatgpt",
    "layout": null,
    "desktop": 1
  },
  {
    "command": "github",
    "layout": null,
    "desktop": 1
  },
  {
    "command": "vscode",
    "layout": null,
    "desktop": 2
  },
  {
    "command": "nextjs",
    "layout": null,
    "desktop": 2
  },
  {
    "command": "localhost",
    "layout": null,
    "desktop": 1
  }
]

Failure Cases:
- If the user asks for an app, website, game, or action that is not in the available command catalog, return [].
- If the request is too vague and cannot be reliably mapped, return [].
- If the request conflicts with available commands, return [].

Output JSON only.

"""

def ai_plan(user_input: str):

    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=f"""
            {SYSTEM_PROMPT}

            User Request:
            {user_input}
            """
    )

    text = response.text.strip()

    return json.loads(text)