import discord
from discord.ext import commands
import os


class SetupCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    async def cog_check(self, ctx):
        return await ctx.bot.is_owner(ctx.author)

    @commands.command()
    async def load(self, ctx, extension):
        await self.bot.load_extension(f'cogs.{extension}')
        await ctx.send(f'{extension} loaded!')

    @commands.command()
    async def unload(self, ctx, extension):
        await self.bot.unload_extension(f'cogs.{extension}')
        await ctx.send(f'{extension} unloaded!')

    @commands.command()
    async def reload(self, ctx, extension):
        try:
            await self.bot.reload_extension(f'cogs.{extension}')
        except commands.ExtensionNotLoaded:
            await self.load(ctx, extension)
            return
        await ctx.send(f'{extension} reloaded!')


class CustomBot(commands.Bot):
    def __init__(self):
        intents = discord.Intents.default()
        intents.message_content = True
        super().__init__(command_prefix='$', intents=intents, case_insensitive=True)

    async def setup_hook(self):
        await self.add_cog(SetupCog(self))
        for filename in os.listdir('cogs'):  # Load all extensions
            if filename.endswith('.py'):
                await self.load_extension(f'cogs.{filename[:-3]}')  # Remove file extension
