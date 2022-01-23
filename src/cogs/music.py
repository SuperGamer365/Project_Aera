import discord
from discord.ext import commands
import youtube_dl


class music(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def join(self, ctx):
        # checking to see if the person who sent the message is in a voice channel
        if ctx.author.voice is None:
            await ctx.send("You need to be in a voice channel for this to work")

        voice_channel = ctx.author.voice.channel
        # checking to see if the bot is already in a voice channel
        if ctx.voice_client is None:
            await voice_channel.connect()

        # if it is in a voice channel, connect
        else:
            await ctx.voice_client.move_to(voice_channel)

    @commands.command()
    async def disconnect(self, ctx):
        if ctx.voice_client is not None:
            await ctx.voice_client.disconnect()

    @commands.command()
    async def play(self, ctx, url):
        ctx.voice_client.stop()
        FFMPEG_OPTIONS = {'before_options': '-reconnect 1 -reconnect_streamed 1 -reconnect_delay_max 5',
                          'options': '-vn'}
        YDL_OPTIONS = {"format": "bestaudio"}

        # this line allows us to use this module easier
        with youtube_dl.YoutubeDL(YDL_OPTIONS) as ydl:
            info = ydl.extract_info(url, download=False)
            url2 = info["formats"][0][
                "url"]  # creating a second url that has all the information to play the song in the
            # channel
            source = await discord.FFmpegOpusAudio.from_probe(url2, **FFMPEG_OPTIONS)

            ctx.voice_client.play(source)

    @commands.command()
    async def pause(self, ctx):
        await ctx.voice_client.pause()
        await ctx.send("Paused the song")

    @commands.command()
    async def resume(self, ctx):
        await ctx.voice_client.resume()
        await ctx.send("resumed the song")


def setup(bot):
    bot.add_cog(music(bot))
