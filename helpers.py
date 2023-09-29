import os
from pathlib import Path
from dotenv import load_dotenv


def read_env():
    if not Path('.env').is_file():
        with open('.env', 'w') as file:
            file.write('# Tokens\n'
                       'DISCORD_TOKEN=\n\n'
                       '# Postgres\n'
                       'PG_DATABASE=\n'
                       'PG_USER=\n'
                       'PG_PASSWORD=')
        print('Generated .env file, stopping')
        quit()
    load_dotenv()


def get_discord_token():
    return os.getenv('DISCORD_TOKEN')
