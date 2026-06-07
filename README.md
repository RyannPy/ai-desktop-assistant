<a id="readme-top"></a>

[![Contributors][contributors-shield]][contributors-url]
[![Forks][forks-shield]][forks-url]
[![Stargazers][stars-shield]][stars-url]
[![Issues][issues-shield]][issues-url]
[![MIT License][license-shield]][license-url]

<h3 align="center">AI Desktop Assistant</h3>

<p align="center">
  A personal Telegram bot that controls your Windows desktop using natural language, powered by Google Gemini.
  <br />
  <a href="https://github.com/github_username/ai-desktop-assistant/issues/new?labels=bug">Report Bug</a>
  &middot;
  <a href="https://github.com/github_username/ai-desktop-assistant/issues/new?labels=enhancement">Request Feature</a>
</p>

---

<!-- TABLE OF CONTENTS -->
<details>
  <summary>Table of Contents</summary>
  <ol>
    <li><a href="#about-the-project">About The Project</a>
      <ul>
        <li><a href="#built-with">Built With</a></li>
      </ul>
    </li>
    <li><a href="#getting-started">Getting Started</a>
      <ul>
        <li><a href="#prerequisites">Prerequisites</a></li>
        <li><a href="#installation">Installation</a></li>
      </ul>
    </li>
    <li><a href="#usage">Usage</a></li>
    <li><a href="#project-structure">Project Structure</a></li>
    <li><a href="#autostart-on-boot">Autostart on Boot</a></li>
    <li><a href="#adding-commands">Adding Commands</a></li>
    <li><a href="#roadmap">Roadmap</a></li>
    <li><a href="#license">License</a></li>
  </ol>
</details>

---

## About The Project

AI Desktop Assistant is a lightweight personal automation tool that lets you control your Windows PC remotely through a Telegram bot. Send a natural language message like *"open YouTube on the left"* or *"I want to code"*, and the bot will plan and execute the appropriate desktop actions — opening apps, launching URLs, switching virtual desktops, and snapping windows into position.

The bot is strictly private: only a single, configured Telegram user ID is allowed to interact with it.

**Key capabilities:**

- Open applications, websites, and folders via natural language
- Switch between Windows virtual desktops automatically (creates new ones if needed)
- Snap windows left or right using Windows snap layout
- Map a single user intent (e.g. *"I want to do data science"*) into a full multi-step workspace setup
- Extensible command registry via a simple JSON file — no code changes needed to add new commands

<p align="right">(<a href="#readme-top">back to top</a>)</p>

### Built With

- [![Python][Python-badge]][Python-url]
- [![Google Gemini][Gemini-badge]][Gemini-url]
- [![Telegram][Telegram-badge]][Telegram-url]

<p align="right">(<a href="#readme-top">back to top</a>)</p>

---

## Getting Started

### Prerequisites

- Python 3.11+
- A Telegram bot token (create one via [@BotFather](https://t.me/BotFather))
- A Google Gemini API key ([Google AI Studio](https://aistudio.google.com/))
- Your Telegram user ID (use [@userinfobot](https://t.me/userinfobot) to find it)
- Windows 10/11 (required for virtual desktop and window snapping features)

### Installation

1. Clone the repository

   ```sh
   git clone https://github.com/github_username/ai-desktop-assistant.git
   cd ai-desktop-assistant
   ```

2. Create and activate a virtual environment

   ```sh
   python -m venv .venv
   .venv\Scripts\activate
   ```

3. Install dependencies

   ```sh
   pip install -r requirements.txt
   ```

4. Set up your environment variables

   Copy `.env.example` to `.env` and fill in your credentials:

   ```sh
   copy .env.example .env
   ```

   ```env
   TELEGRAM_TOKEN=your_telegram_bot_token
   ALLOWED_USER_ID=your_telegram_user_id
   GEMINI_API_KEY=your_gemini_api_key
   ```

5. Configure your commands

   Edit `commands.json` to add the apps, folders, and URLs relevant to your machine. See [Adding Commands](#adding-commands) for the schema.

6. Run the bot

   ```sh
   python main.py
   ```

<p align="right">(<a href="#readme-top">back to top</a>)</p>

---

## Usage

Once the bot is running, open Telegram and send a message to your bot. Only your configured `ALLOWED_USER_ID` can interact with it.

**Example prompts:**

| Prompt | What happens |
|---|---|
| `youtube` | Opens YouTube in the browser |
| `open youtube on the left` | Opens YouTube and snaps the window to the left |
| `youtube left, vscode right on desktop 2` | Opens YouTube snapped left, then VS Code snapped right on virtual desktop 2 |
| `I want to code` | Opens ChatGPT, GitHub, and VS Code across desktops |
| `I want to do data science` | Opens Kaggle, GitHub, the data science folder, and VS Code |
| `I want to relax` | Opens WhatsApp, Instagram, and YouTube |
| `open steam and spotify` | Opens both apps in sequence |

The AI planner (Gemini) converts your message into a structured task list. Each task specifies a command, an optional window layout (`left` / `right`), and a target virtual desktop number. The bot then executes each task in order.

If a command is not in the registry or the request is too vague, the bot replies with an appropriate message without taking any action.

<p align="right">(<a href="#readme-top">back to top</a>)</p>

---

## Project Structure

```
ai-desktop-assistant/
├── main.py                  # Entry point
├── commands.json            # Command registry (apps, URLs, folders)
├── .env                     # Environment variables (not committed)
├── .env.example             # Environment variable template
│
├── bot/
│   └── telegram_bot.py      # Telegram bot handlers and main loop
│
├── ai/
│   ├── planner.py           # Gemini prompt → task list (JSON)
│   ├── validator.py         # Validates AI output against the registry
│   └── responses.py         # Randomized bot response strings
│
├── actions/
│   ├── executor.py          # Resolves command keys and runs actions
│   ├── case.py              # Action type handlers (app, url, folder, hotkey)
│   └── layout.py            # Window snap via Win+Left / Win+Right
│
├── commands/
│   └── registry.py          # Loads commands.json into COMMANDS and WINDOW_ALIASES
│
├── services/
│   ├── desktop_service.py   # Virtual desktop switching and creation (pyvda)
│   ├── layout_service.py    # Resolves window alias and applies snap layout
│   ├── window_service.py    # Window focus and snap helpers
│   └── loading_service.py   # Telegram loading message lifecycle
│
└── config/
    ├── settings.py          # Loads environment variables
    └── logger.py            # Application logger
```

<p align="right">(<a href="#readme-top">back to top</a>)</p>

---

## Autostart on Boot

To have the bot start automatically when Windows boots:

1. Press `Win + R`, type `shell:startup`, and press Enter. This opens the Startup folder.
2. Create a shortcut to `pythonw.exe` (use `pythonw` to run without a console window) pointing to `main.py`.

   Alternatively, create a `.bat` file with the following content and place the shortcut in the Startup folder:

   ```bat
   @echo off
   cd /d "D:\path\to\ai-desktop-assistant"
   .venv\Scripts\pythonw.exe main.py
   ```

3. The bot will now start silently in the background on every login.

The bot uses a Windows named mutex to prevent multiple instances from running at the same time — so restarting Windows will not create duplicate processes.

<p align="right">(<a href="#readme-top">back to top</a>)</p>

---

## Adding Commands

All commands are defined in `commands.json` at the project root. No Python code changes are needed to add new entries.

**Schema:**

```json
"command_key": {
  "action": {
    "type": "open_app | open_url | open_folder | hotkey | delay",
    "app": "executable or path (for open_app)",
    "url": "https://... (for open_url)",
    "path": "C:\\... (for open_folder)"
  },
  "window_alias": "window title keyword for snapping"
}
```

**Example — adding Notion:**

```json
"notion": {
  "action": {
    "type": "open_url",
    "url": "https://notion.so"
  },
  "window_alias": "google chrome"
}
```

After adding a new command, restart the bot. The Gemini planner will automatically be able to use it once it appears in the registry.

<p align="right">(<a href="#readme-top">back to top</a>)</p>

---

## Roadmap

- [ ] Multi-step action sequences per command (e.g. open app then run a hotkey)
- [ ] Screenshot and screen status reporting back to Telegram
- [ ] Voice message input support
- [ ] Web dashboard for managing the command registry

<p align="right">(<a href="#readme-top">back to top</a>)</p>

---

## License

Distributed under the MIT License. See `LICENSE` for more information.

<p align="right">(<a href="#readme-top">back to top</a>)</p>

---

<!-- MARKDOWN LINKS & BADGES -->
[contributors-shield]: https://img.shields.io/github/contributors/github_username/ai-desktop-assistant.svg?style=for-the-badge
[contributors-url]: https://github.com/github_username/ai-desktop-assistant/graphs/contributors
[forks-shield]: https://img.shields.io/github/forks/github_username/ai-desktop-assistant.svg?style=for-the-badge
[forks-url]: https://github.com/github_username/ai-desktop-assistant/network/members
[stars-shield]: https://img.shields.io/github/stars/github_username/ai-desktop-assistant.svg?style=for-the-badge
[stars-url]: https://github.com/github_username/ai-desktop-assistant/stargazers
[issues-shield]: https://img.shields.io/github/issues/github_username/ai-desktop-assistant.svg?style=for-the-badge
[issues-url]: https://github.com/github_username/ai-desktop-assistant/issues
[license-shield]: https://img.shields.io/github/license/github_username/ai-desktop-assistant.svg?style=for-the-badge
[license-url]: https://github.com/github_username/ai-desktop-assistant/blob/master/LICENSE

[Python-badge]: https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white
[Python-url]: https://www.python.org/
[Gemini-badge]: https://img.shields.io/badge/Google%20Gemini-8E75B2?style=for-the-badge&logo=googlegemini&logoColor=white
[Gemini-url]: https://aistudio.google.com/
[Telegram-badge]: https://img.shields.io/badge/Telegram-2CA5E0?style=for-the-badge&logo=telegram&logoColor=white
[Telegram-url]: https://core.telegram.org/bots
