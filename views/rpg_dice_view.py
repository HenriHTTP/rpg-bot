import disnake
from disnake.ui import View


class DiceView(View):
    def __init__(self, ctx, message: str, bot, emoji: any):
        super().__init__()
        self.__ctx = ctx
        self.__message = message
        self.__bot = bot
        self.__emoji = emoji

    async def interaction_check(self, interaction: disnake.Interaction):
        return interaction.user == self.__ctx.author

    def to_embed(self):
        embed = disnake.Embed(
            title=self.__bot.user.name,
            description=f"{self.__message} {self.__emoji}",
            color=disnake.Color.blue()
        )
        embed.set_thumbnail(url=self.__bot.user.avatar.url)
        return embed
