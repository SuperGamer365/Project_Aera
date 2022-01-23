import discord
from discord import Forbidden
from discord import HTTPException
from discord.ext import commands
import typing


class mod(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    @commands.has_permissions(kick_members=True)
    async def kick(self, ctx, member: discord.Member, *, reason: typing.Optional[str]):
        guild = ctx.guild
        if member == ctx.author:
            await ctx.send("You can't kick yourself")

        else:
            try:
                await guild.kick(user=member, reason=reason)

            except Forbidden:
                await ctx.send("You do not have the proper permissions to kick {}".format(member))

            except HTTPException:
                await ctx.send("Kicking {} failed, due to an HTTPException".format(member))

    @commands.command()
    async def ban(self, ctx, member: discord.Member, *, reason: str, delete_days: typing.Optional[int]):
        guild = ctx.guild
        if member == ctx.author:
            await ctx.send("You cannot ban yourself")

        else:
            try:
                await guild.ban(user=member, reason=reason, delete_message_days=delete_days)

            except Forbidden:
                await ctx.send("You do not have the proper permissions to ban {}".format(member))

            except HTTPException:
                await ctx.send("Banning {} failed, due to an HTTPException".format(member))

    @commands.command()
    async def unban(self, ctx, member: discord.Member):
        guild = ctx.guild
        try:
            await guild.unban(user=member)

        except Forbidden:
            await ctx.send("You do not have the proper permissions to unban {}".format(member))

        except HTTPException:
            await ctx.send("Unbanning {} failed, due to an HTTPException".format(member))


def setup(bot):
    bot.add_cog(mod(bot))
