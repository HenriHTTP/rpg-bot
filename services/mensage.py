from disnake.ext.commands import Context, Bot


class Message:
    def __init__(self,  ctx: Context, message: str, bot: Bot) -> None:
        ...

async def send_message(self) -> bool :
    try:
        ...
        return True
    except Exception as error:
        ...
        return False

async def reply_message_user(self) -> bool :
    try:
        ...
        return True
    except Exception as error:
        ...
        return False

async def reply_mention_message(self) -> bool :
    try:
        ...
        return True
    except Exception as error:
        ...
        return False
