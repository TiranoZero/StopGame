import discord
from discord import Intents, Member, utils, Embed, File
from discord.ext import commands
from decouple import config as key

intents = Intents.all()

bot = commands.Bot(command_prefix="Gm ", case_insensitive=True, intents=intents)
tocken=key("TK")

@bot.event
async def on_ready():
  nome = bot.user.name
  banner = f"Bot:{nome}\nStatus:Online"


@bot.event
async def on_member_join(m:Member):
    nome = m.name
    channel = utils.get(m.guild.channels, name="entrada")
    banner = Embed(title="Bem viado",
                   description="seja bem vindo ao lado de fora",
                   color=0xFF0000)
    foto = absolute.abcinema(nome)
    file = File(foto)
    banner.set_image(url=f"attachment://{foto}")
    await channel.send(file=file, embed=banner)

bot.run(tocken)

