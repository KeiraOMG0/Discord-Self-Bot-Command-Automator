# Discord Self-Bot Command Automator

This self-bot automatically triggers a specified `/command` at a set interval using Discord's API. It can be used to automate tasks like bumping a server or executing custom commands.

## Features

- Automates sending a specific slash command (`/command`).
- Uses Discord API to trigger commands remotely.
- Runs as a self-bot.
- Supports start/stop commands for manual control.
- Utilizes Discord's `tasks.loop()` for periodic execution.

## Requirements

- Python 3.8+
- `aiohttp`
- `discord.py-self`

## Installation

1. Clone the repository: [https://github.com/KeiraOMG0/Discord-Self-Bot-Command-Automator.git](https://github.com/KeiraOMG0/Discord-Self-Bot-Command-Automator.git)

   ```sh
   git clone https://github.com/KeiraOMG0/Discord-Self-Bot-Command-Automator.git
   cd Discord-Self-Bot-Command-Automator
   ```

2. **Create a Virtual Environment (Recommended)**

Creating a virtual environment helps keep dependencies isolated.

If you want to skip Step 2 and Step 3, simply run the provided setup script:

**- Windows: `setup.bat`**

**- Mac/Linux: `setup.sh`**

For macOS/Linux users:  
Before running the setup script, you'll need to make it executable:

```sh
chmod +x setup.sh
```

Then run the script:

```sh
./setup.sh
```

If you prefer to set up manually, follow these steps:

Windows (Command Prompt / PowerShell)

```sh
python -m venv venv
venv\Scripts\activate
```

Mac / Linux (Terminal)

```sh
python3 -m venv venv
source venv/bin/activate
```

3. Install dependencies:

   ```sh
   pip install -r requirements.txt
   ```

4. Edit the script (`main.py`) and replace placeholders:
   - `TOKEN` → Your Discord self-bot token.
   - `application_id` → The ID of the bot application.
   - `command_id` → The ID of the command.
   - `command_name` → The name of the command.
   - `guild_id` → The server ID where the command is used.
   - `channel_id` → The channel ID where the command is executed.

## Usage

Run the script with:

```sh
python main.py
```

### Commands

- `$start` → Starts the automated execution of the command.
- `$stop` → Stops the automation.

## License

This project is licensed under the Creative Commons Zero v1.0 Universal (CC0 1.0) license. This means:

- You can use, modify, and distribute the code for free.
- You cannot make it paid.
- The license itself cannot be changed.
- Anyone can fork and use it freely.

## Disclaimer

This project is for educational purposes only. Using self-bots violates Discord's Terms of Service and may result in account termination. Use at your own risk.
