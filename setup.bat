@echo off
:: Check if venv directory exists
if exist venv (
    echo Virtual environment already exists. Skipping venv creation.
) else (
    :: Create a virtual environment if it doesn't exist
    echo Creating virtual environment...
    python -m venv venv
)

:: Activate the virtual environment
call venv\Scripts\activate.bat

:: Install the required packages
echo Installing dependencies...
pip install git+https://github.com/dolfies/discord.py-self.git
pip install aiohttp

:: Run main.py
echo Running main.py...
python main.py

:: Deactivate the virtual environment after running main.py
deactivate

:: Notify the user that the script has completed
echo Script execution complete.
pause
