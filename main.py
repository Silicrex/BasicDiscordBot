import logging
from pathlib import Path
from datetime import datetime
import discord
from helpers import get_discord_token
from custom_bot import CustomBot


def main():
    # Logging config
    Path('logs/').mkdir(exist_ok=True)  # Make sure the Logs folder exists
    log_name = datetime.now().strftime("%Y-%b")
    log_handler = logging.FileHandler(filename=f'logs/{log_name}.log', encoding='utf-8', mode='a')

    # Intents
    intents = discord.Intents.default()
    intents.message_content = True

    # Bot setup
    discord_token = get_discord_token()
    bot = CustomBot(command_prefix='$', intents=intents, case_insensitive=True)
    bot.run(discord_token, log_handler=log_handler)


if __name__ == '__main__':
    main()
