import discord
import asyncio
from discord.ext import commands



class my_bot(commands.Bot):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    @classmethod
    def create(cls) -> "my_bot":
        loop = asyncio.get_event_loop()
        intents = discord.Intents.all()
        return cls(
            loop=loop,
            intents=intents,
            command_prefix=commands.when_mentioned_or("$"),
            activity=discord.Game(name="Commands: $help"),
            case_insensitive=True,
        )

    def load_extensions(self):
        import Load_stuff.load_exts

        extentions = list(Load_stuff.load_exts.EXTENSIONS) # creating a list for the qualified extensions

        for extention in extentions:
            self.load_extension(extention)

    def remove_command(self, name: str):
        command = super().remove_command(name) # using this to check if this exist
        if command is None:
            return # the command doesn't exist and we don't do anything
        return command # remove the command



    async def on_ready(self):
       print("Started up as {}".format(self.user))

    async def login(self, *args, **kwargs):
        await super().login(*args, **kwargs)
