from helpers import get_discord_token
from CustomBot import CustomBot


def main():
    bot = CustomBot()
    discord_token = get_discord_token()
    bot.run(discord_token)


if __name__ == '__main__':
    main()
