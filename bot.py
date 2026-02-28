import discord
from discord.ext import commands
import os

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    print(f"Zalogowano jako {bot.user}")

@bot.command()
async def ping(ctx):
    await ctx.send("Pong! ☁️")

@bot.command()
async def hello(ctx):
    await ctx.send("Hej! Jestem Cloudly ☁️")

# TOKEN z zmiennej środowiskowej (bezpieczne 24/7)
bot.run(os.getenv("TOKEN"))