from views.player_sheet_view import PlayerSheetView

class PlayerSheetService:
    def __init__(self, ctx, bot):
        self.__ctx = ctx
        self.__bot = bot

    async def see_player_sheet(self,player_name: str,character_race: str, year_old: int, nationality: str, body_type: str):
        try:
            print(player_name,character_race, year_old, nationality, body_type)
            await self.__send_player_sheet_on_message(player_name,character_race, year_old, nationality, body_type)
        except Exception as error:
            print(f"Erro ao gerar a ficha: {error}")


    async def __send_player_sheet_on_message(self, player_name: str,character_race: str, year_old: int, nationality: str, body_type: str):
        player_sheet_view = PlayerSheetView(
            self.__ctx,
            player_name,
            character_race,
            year_old,
            nationality,
            body_type
        )
        embed = player_sheet_view.to_embed()

        try:
            message = await self.__ctx.send(embed=embed, ephemeral=False)
            player_sheet_view.message = message
        except Exception as error:
            print(f"Erro ao enviar a mensagem: {error}")
