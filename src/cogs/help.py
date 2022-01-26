import discord
from discord.ext import commands


class help(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.group(invoke_without_command=True, case_insensitive="True")
    async def help(self, ctx):
        embed = discord.Embed(
            title="Help",
            description="Below are the cogs that you can  be helped with."
                        "Just type $help <Cog name>. After that, Aera will send out a "
                        "list of the commands and their syntax and purpose",
            color=discord.Colour.orange()
        )

        embed.add_field(
            name="Moderator",
            value="This cog is for people who have control of the server. Certain things like banning and kicing are "
                  "avaliable "
        )

        embed.add_field(
            name="Music",
            value="This cog has commands that allows Aera to join and play music in voice channels"
        )

        await ctx.send(embed=embed)

    @help.command()
    async def Moderator(self, ctx):
        embed = discord.Embed(
            title="Moderator Commands",
            description="These commands moderate the server by banning, kicking, etc.",
            color=discord.Colour.blue()
        )

        embed.add_field(
            name="Kick",
            value="Kicking kicks the targeted user. Syntax is $kick [targeted member]<reason>"
        )

        embed.add_field(
            name="Ban",
            value="Banning bans the targeted user. Syntax is $ban [targeted member]<reason>"
        )

        embed.add_field(
            name="Purge",
            value="Purging deletes the selected number of messages including the command request. Syntax is "
                  "$purge [message amount] "
        )

        embed.add_field(
            name="Nuke",
            value="Deletes all the messages in a channel. Syntax is $nuke <mention channel>"
        )

        await ctx.send(embed=embed)


def setup(bot):
    bot.add_cog(help(bot))
