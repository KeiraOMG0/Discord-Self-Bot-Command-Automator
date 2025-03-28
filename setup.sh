#!/bin/bash

#  Set your virtual environment name
VENV_DIR="./venv"

#  Check if venv exists
if [ -d "$VENV_DIR" ]; then
    echo -e "\e[1;35m Virtual environment found. Launching self-bot... \e[0m"
else
    echo -e "\e[1;34m No venv found! Creating a new one... \e[0m"
    python3 -m venv venv

    # Activate the venv
    source "$VENV_DIR/bin/activate"

    # Install discord.py-self and colorama
    echo -e "\e[1;33m Installing dependencies... \e[0m"
    pip install git+https://github.com/dolfies/discord.py-self.git
    pip install aiohttp
    
    echo -e "\e[1;32m Setup complete! Running your self-bot now. \e[0m"
fi

# 💜 Activate the venv
source "$VENV_DIR/bin/activate"

#  Run your self-bot
echo -e "\e[1;36m Starting your self-bot... \e[0m"
python3 main.py

#  When you close the bot, deactivate venv
deactivate
echo -e "\e[1;31m Self-bot stopped. Type ./run.sh to restart. \e[0m"

