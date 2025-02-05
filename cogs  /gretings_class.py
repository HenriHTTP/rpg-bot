from disnake.ext import commands
from disnake.ext.commands import Bot


class Greetings(commands.Cog):
    def __init__(self, bot):
        self.__bot = bot

    @commands.Cog.listener()
    async def on_message(self, ctx):
        ...

    @commands.Cog.listener()
    async def on_member_join(self, member):
        ...

    @commands.slash_command(name="hello", description='greetings to user.')
    async def greet_user(self, ctx):
        ...


def setup(bot):
    bot.add_cog(Greetings(bot))
