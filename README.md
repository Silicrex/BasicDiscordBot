# BasicDiscordBot

* This is a basic template for creating Discord bots using **discord.py**, a Python wrapper for the **Discord API**
* It was created with discord.py version **2.9.3**, Python version **3.9**
* Read the discord.py documentation at https://discordpy.readthedocs.io/en/stable/index.html

## Basic Overview

* This is not an exhaustive guide for creating Discord bots with the library, it assumes familiarity with it

### Bot Token

* The bot uses a **.env** file for storing the **bot token**. On startup, if the file doesn't exist, it's generated and
  prepared
* **helpers.py** comes with a function for fetching the **bot token** from this file, which **main.py** is already set
  up to use for initializing the bot

### Bot Client

* Our **bot client** is a subclass of **commands.Bot()** implemented in **custom_bot.py**. It comes with a
  **setup_hook()** override for automatically loading all extensions in **cogs/** on startup, as well as commands for
  loading, unloading, and reloading **extensions**
* **Intents** are default aside from **message_content** being enabled, which is a required **Privileged Intent**
* Basic **logging** is set up. If you don't want it, you can just remove that part from **main.py**. It's set to the
  default log_level of logging.INFO

### Cogs/Extensions

* **cogs/** is where implementation of the bot's features is intended to go (the **Cogs** and **Extensions** systems
  offer tremendous modularization and organization; Extensions also allow you to update code or selectively load/unload
  features during runtime)
* It is assumed that all items in **cogs/** are also set up as **extensions**, which can either be an individual
  **Python file** or a **package**. **Extensions** require a **setup()** function (for packages, this would go in the
  **\_\_init__.py** file)
* The **cogs/** folder name is hardcoded into the function for loading extensions. If you want to change the name of the
  folder, you will have to update the references to it
* **Extensions** that have names starting with an **underscore (_)** will be excluded from being loaded on startup

### BotUtility Cog

* Cogs are designated to go in the **cogs/** folder
* A **bot_utility** cog is already created that comes with the following:
    * An **on_ready()** listener which prints the **bot username** as well as **discord.py** version on startup
    * An **on_command_error()** listener which sets up a system for **ignoring already-handled errors** using an
      **error_handled** attr, and provides basic error handling for the extension commands, command cooldowns, and check
      fails (which are ignored). Errors that aren't handled are given a detailed print to the console
    * Regardless of if a local error handler or cog error handler resolves an exception,
      **on_command_error()** will still be called. To avoid redundant error handling, if an error was handled in a
      lower-level handler, set **ctx.error_handled = True** in it
    * A **ping** command

## postgresdb
* There is a **release branch** called **postgresdb** which has a basic **PostgreSQL** (Postgres) database compatibility setup. It uses the asynchronous Postgres/asyncio wrapper **asyncpg** (documentation: https://magicstack.github.io/asyncpg/current/index.html)
* You will need to install **Postgres** (https://www.postgresql.org/) and set up the actual database separately
* The **.env** file has fields for connecting to your database. There are more fields you can add if necessary, see asyncpg docs
* It automatically sets up a **Connection Pool** on bot startup (access it with **bot.pg_pool**) and closes it on bot shutdown. **bot.pg_pool** is what is used to run SQL commands, see asyncpg docs for specifics