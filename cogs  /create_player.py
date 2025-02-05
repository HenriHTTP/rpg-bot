from disnake.ext import commands
from disnake.ext.commands import Bot


class Create_player(commands.Cog):
    def __init__(self, bot):
        self.__bot = bot


def setup(bot):
    bot.add_cog(Create_player(bot))
