import discord
from discord.ext import commands
from discord import app_commands
import os
from dotenv import load_dotenv

load_dotenv()

TOKEN = os.getenv("DISCORD_TOKEN")

intents = discord.Intents.default()
intents.message_content = True
intents.members = True
bot = commands.Bot(command_prefix='.', intents=intents, help_command=None)

@bot.event
async def load_cogs():
    for archives in os.listdir('cogs'):
        if archives.endswith('.py'):
            await bot.load_extension(f"cogs.{archives[:-3]}")

@bot.event
async def on_ready():
    await load_cogs()
    print(f'{bot.user.name} is ready')

@bot.command()
async def test(ctx:commands.Context):
    await ctx.reply("<:SSSplus:1223101139617058826>")

@bot.command()
async def urank(ctx:commands.Context):
    await ctx.reply("<:Urank:1223104149126909962>")

@bot.command()
async def sincronize(ctx:commands.Context):
    if ctx.author.id == 232276692629061632:
        sincs = await bot.tree.sync()
        await ctx.reply(f"{len(sincs)} commands are sync.")
    else:
        await ctx.reply("You do not have permission to use this command!", ephemeral=True)

bot.run(TOKEN)