import asyncio

from .bot_init import bot, dp
from .handlers import router
from .middlewares import LoggingMiddleware


async def run_polling():
    # Include middlewares
    dp.message.middleware(LoggingMiddleware())

    # Register handlers
    dp.include_router(router)

    # Start polling
    print("Bot is starting with polling...")
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(run_polling())
