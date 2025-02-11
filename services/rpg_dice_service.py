from views.rpg_dice_view import DiceView
import random

class RpgDiceService:
    def __init__(self, ctx, bot):
        self.__ctx = ctx
        self.__bot = bot

    async def get_random_number(self, sided: int):
        try:
            random_number = random.randint(1, sided)
            await self.__send_result_number_message(str(random_number))
        except Exception as error:
            print(f"Erro ao gerar o número aleatório: {error}")

    async def __send_result_number_message(self, number):
        data_emoji = "\U0001F3B2"
        data_view = DiceView(
            self.__ctx,
            number,
            self.__bot,
            data_emoji
        )
        embed = data_view.to_embed()

        try:
            message = await self.__ctx.send(embed=embed, ephemeral=False)
            data_view.__message = message
        except Exception as error:
            print(f"Erro ao enviar a mensagem: {error}")
