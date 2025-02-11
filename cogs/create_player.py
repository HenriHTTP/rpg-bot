from disnake.ext import commands
from disnake.ext.commands import Bot


class Create_player(commands.Cog):
    def __init__(self, bot: Bot):
        self.__bot = bot

    @commands.Cog.listener()
    async def on_message(self, ctx):
      ...


def setup(bot):
    bot.add_cog(Create_player(bot))
