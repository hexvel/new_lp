from vkbottle.user import Message, UserLabeler

from actions.rules import Commands

labeler = UserLabeler()


@labeler.message(Commands(".д", ["ping"]))
async def ping_command(message: Message):
    await message.answer("pong!")
