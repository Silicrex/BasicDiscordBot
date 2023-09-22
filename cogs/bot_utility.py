import discord
from discord.ext import commands
import time


class BotUtility(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    async def cog_load(self):
        print(f'{self.__class__.__name__} loaded!')

    async def cog_unload(self):
        print(f'{self.__class__.__name__} unloaded!')

    @commands.Cog.listener()
    async def on_ready(self):
        print(f'Logged in as {self.bot.user} on discord.py version {discord.__version__}!')

    @commands.Cog.listener()
    async def on_command_error(self, ctx, error):
        if hasattr(ctx, 'error_handled'):
            return
        if isinstance(error, commands.CommandInvokeError):
            error = error.original

        if isinstance(error, commands.CommandOnCooldown):
            await ctx.send(f'{ctx.command} is on cooldown for another {error.retry_after:.2f} seconds')
        elif isinstance(error, commands.ExtensionNotFound):
            await ctx.send('Extension not found')
        elif isinstance(error, commands.ExtensionAlreadyLoaded):
            await ctx.send('Extension is already loaded')
        elif isinstance(error, commands.ExtensionNotLoaded):
            await ctx.send('Extension is not loaded')
        else:
            print(error)

    @commands.command()
    @commands.cooldown(rate=1, per=5, type=commands.BucketType.user)
    async def ping(self, ctx):
        start = time.perf_counter()
        message = await ctx.send("Ping..")
        end = time.perf_counter()
        duration = (end - start) * 1000
        await message.edit(content=f'Pong! {duration:.2f}ms')


async def setup(bot):
    await bot.add_cog(BotUtility(bot))