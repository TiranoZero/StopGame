import discord
from discord import Intents
from discord.ext import commands
from decouple import config as key

intents = Intents.all()

bot = commands.Bot(command_prefix="Gm ", case_insensitive=True, intents=intents)
tocken=key("TK")

@bot.event
async def on_ready():
  nome = bot.user.name
  banner = f"Bot:{nome}\nStatus:Online"

bot.run(tocken)

