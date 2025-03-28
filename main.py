import random
import aiohttp
import asyncio
import discord
from discord.ext import commands, tasks

# Your token (self-bot token)
TOKEN = "token here"

# The custom bot's application ID and command ID
application_id = "the bots applcation id"
command_id = "the bots command id"  # Replace with your command ID
command_name = "command name"  # Your custom command name
version = 1051151064008769576
# Initialize bot
bot = commands.Bot(command_prefix="$", self_bot=True)

session_id = "".join(random.choice('0123456789abcdef') for _ in range(32))


async def trigger_command():
    """Simulate triggering the /bump command remotely via Discord API."""
   

    # The header with the user token
    headers = {
        'Authorization': f' {TOKEN}',  # Use token for authorization 
        'Content-Type': 'application/json'
    }

    payload = {
        "type": 2,  # Type 2 is for invoking a command
        "application_id": application_id,
        "guild_id": "guilds id",  # Replace with your guild ID
        "channel_id": "channel id",  # Replace with your channel ID
        "session_id": session_id,
        "data": {
            "version": version,
            "id": command_id, # i think this isnt needed but idk
            "name": command_name,
            "type": 1,  # This represents the type of application command
            "options": []  # Empty options if none are needed
        }
    }

    async with aiohttp.ClientSession() as session:
        async with session.post(
            f'https://discord.com/api/v9/interactions',
            headers=headers,
            json=payload
        ) as response:
            if response.status == 204:
                print("Successfully triggered the / command.")
            else:
                print(f"Failed to trigger the / command: {response.status}")
                print(await response.text())

@bot.event
async def on_ready():
    print(f"{bot.user} is now online.")
    repeat.start()

@bot.command()
async def start(ctx):
    repeat.start()
    ctx.send("Started task!")

@bot.command()
async def stop(ctx):
    repeat.stop()
    ctx.send("Stopped task!")


@tasks.loop() # set time example @tasks.loop(hours=5)
async def repeat():    
    await trigger_command()

bot.run(TOKEN)
