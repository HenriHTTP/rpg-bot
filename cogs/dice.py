from disnake.ext import commands
from disnake.ext.commands import Bot
from services.rpg_dice_service import RpgDiceService


class RpgDice(commands.Cog):
    def __init__(self, bot: Bot):
        self.__bot = bot

    @commands.slash_command(name="roll20", description="Roll RPG dice (20-sided).")
    async def roll_dice_twenty(self, ctx):
        roll_dice = RpgDiceService(ctx, self.__bot)
        await roll_dice.get_random_number(20)

    @commands.slash_command(name="roll12", description="Roll RPG dice (12-sided).")
    async def roll_dice_twelve(self, ctx):
        roll_dice = RpgDiceService(ctx, self.__bot)
        await roll_dice.get_random_number(12)

    @commands.slash_command(name="roll8", description="Roll RPG dice (8-sided).")
    async def roll_dice_eight(self, ctx):
        roll_dice = RpgDiceService(ctx, self.__bot)
        await roll_dice.get_random_number(8)

def setup(bot):
    bot.add_cog(RpgDice(bot))
