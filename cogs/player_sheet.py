from ast import Import
from disnake.ext import commands
from disnake.ext.commands import Bot, Command
from services.player_sheet_service import PlayerSheetService



class PlayerSheet(commands.Cog):
    def __init__(self, bot : Bot):
        self.__bot = bot

    @commands.slash_command(name="create", description='create player sheet.', auto_defer=True)
    async def create_player(self, ctx,
        nome_player: str = commands.Param(),
        raca_personagem: str = commands.Param(),
        idade: int= commands.Param(),
        nacionalidade: str  = commands.Param() ,
        tipo_de_corpo: str = commands.Param()
    ):
       player_sheet = PlayerSheetService(ctx, self.__bot)
       await player_sheet.see_player_sheet(nome_player,raca_personagem, idade, nacionalidade, tipo_de_corpo)



def setup(bot):
    bot.add_cog(PlayerSheet(bot))
