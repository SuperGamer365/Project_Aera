import discord
from discord.ext import commands
import Bot_token
from cogs import music, mod, help, util
import bot

#bot = commands.Bot(command_prefix="$", intents=discord.Intents.all(), activity=discord.Game(name="Commands: $help"))
#bot.remove_command('help')

#cogs = [music, mod, help, util]

#for i in range(len(cogs)):
#    cogs[i].setup(bot)


#@bot.event
#async def on_ready():
#    print("Started up as {}".format(bot.user))


#bot.run(Bot_token.token)

Aera = bot.my_bot.create()
Aera.remove_command("help")
Aera.load_extensions()
Aera.run(Bot_token.token)
