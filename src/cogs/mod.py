import discord
from discord import Forbidden
from discord import HTTPException
from discord.ext import commands
import typing


class mod(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command
    async def kick(self, ctx, member: discord.Member, *, reason: typing.Optional[str]):
        guild = ctx.guild
        if member == ctx.author:
            await ctx.send("You can't kick yourself")

        else:
            try:
                await guild.kick(user=member, reason=reason)

            except Forbidden as e:
                await ctx.send("You do not have the proper permissions to kick {}".format(member))

            except HTTPException as e:
                await ctx.send("Kicking {} failed, due to an HTTPException".format(member))


def setup(bot):
    bot.add_cog(mod(bot))
