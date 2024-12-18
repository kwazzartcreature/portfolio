from aiogram import Router, F
from aiogram.types import Message

router = Router()


@router.message(F.text == "/start")
async def start_handler(message: Message):
    await message.answer("Hello! I am your Telegram bot.")


@router.message(F.text == "/help")
async def help_handler(message: Message):
    await message.answer(
        "Here are the available commands:\n/start - Start the bot\n/help - Show this help"
    )


@router.message()
async def common_handler(message: Message):
    await message.answer("I received your message: " + message.text)
