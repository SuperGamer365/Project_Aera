import discord
from discord import Forbidden, HTTPException
from discord.ext import commands
import typing


class mod(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def kick(self, ctx, member: discord.Member, *, reason: typing.Optional[str]):
        guild = ctx.guild
        if member == ctx.author:
            await ctx.send("You can't kick yourself")

        else:
            try:
                await guild.kick(member, reason=reason)
                await ctx.send("{0} has been kicked for {1}".format(member, reason))

            except Forbidden:
                await ctx.send("You do not have the proper permissions to kick {}".format(member))

            except HTTPException:
                await ctx.send("Kicking {} failed, due to an HTTPException".format(member))

    @commands.command()
    async def ban(self, ctx, member: discord.Member, *, reason: typing.Optional[str]):
        guild = ctx.guild
        if member == ctx.author:
            await ctx.send("You cannot ban yourself")

        else:
            try:
                await guild.ban(member, reason=reason)
                await ctx.send("{0} has been banned for {1}".format(member, reason))

            except Forbidden:
                await ctx.send("You do not have the proper permissions to ban {}".format(member))

            except HTTPException:
                await ctx.send("Banning {} failed, due to an HTTPException".format(member))


  #(Channel commands)-------------------------------------------------------------------------------------------------
    @commands.command()
    async def purge(self, ctx, limit: int):
        try:
            await ctx.channel.purge(limit=limit, bulk=False)

        except Forbidden:
            await ctx.send(
                "You must have the manage_messages permission to delete messages even if they are your own."
                "The read_message_history permission is also needed to retrieve message history."
                )

        except HTTPException:
            await ctx.send("Purging {} messages couldn't work due to an HTTPException".format(limit))


    @commands.command()
    async def nuke(self, ctx, channel: discord.TextChannel = None):
        #some checks
        if channel is None: #checking to see if the instance of the channel is the same as the nonetype, esstentially checking if a channel name was provided
            await ctx.send("Mention a channel to nuke it")
            return
        try:
            await channel.purge(bulk=True)
            await channel.send("{0} purged by {1}".format(channel, ctx.author))
        except Forbidden:
            await ctx.send(
                "You must have the manage_messages permission to delete messages even if they are your own."
                "The read_message_history permission is also needed to retrieve message history."
            )
        except HTTPException:
            await ctx.send("Nuking channel {} couldn't work due to an HTTPException".format(channel))


def setup(bot):
    bot.add_cog(mod(bot))
