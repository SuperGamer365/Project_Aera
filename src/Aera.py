import discord
from discord.ext import commands
import Bot_token
from cogs import music

bot = commands.Bot(command_prefix="$", intents=discord.Intents.all())

cogs = [music]

for i in range(len(cogs)):
    cogs[i].setup(bot)


@bot.event
async def on_ready():
    print("Started up as {}".format(bot.user))


bot.run(Bot_token.token)
