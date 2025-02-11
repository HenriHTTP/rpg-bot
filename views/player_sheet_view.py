import disnake
from disnake.ui import View

class PlayerSheetView(View):
    def __init__(self, ctx, player_name: str, character_race: str, year_old: int, nationality:str, body_type: str):
        super().__init__()
        self.__ctx = ctx
        self.__player_name = player_name
        self.__character_race = character_race
        self.__year_old = year_old
        self.__nationality = nationality
        self.__money = None
        self.__body_type = body_type

    async def interaction_check(self, interaction: disnake.Interaction):
        return interaction.user == self.__ctx.author

    def to_embed(self):
        embed = disnake.Embed(
            title=f"{self.__player_name}",
            description=(
                f"**raca**: {self.__character_race}\n"
                f"**idade**: {self.__year_old}\n"
                f"**nacionalidade**: {self.__nationality}\n"
                f"**dinheiro**: {self.__money} coins\n"
                f"**tipo de corpo**: {self.__body_type}"
            ),
            color=disnake.Color.blue()
        )
        return embed
