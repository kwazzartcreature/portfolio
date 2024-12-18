from aiogram import Dispatcher, types
from aiogram.webhook.aiohttp_server import SimpleRequestHandler, setup_application
from aiohttp import web

from bot_init import bot, dp
from config import WEBHOOK_URL, WEBHOOK_PATH, WEBAPP_PORT, WEBAPP_HOST
from handlers import router
from .middlewares import LoggingMiddleware


async def on_startup(bot):
    await bot.set_webhook(WEBHOOK_URL + WEBHOOK_PATH)
    print("Webhook set successfully!")


async def run_webhooks():
    # Include middlewares and handlers
    dp.message.middleware(LoggingMiddleware())
    dp.include_router(router)

    # Initialize aiohttp app
    app = web.Application()
    webhook_requests_handler = SimpleRequestHandler(dispatcher=dp, bot=bot)
    webhook_requests_handler.register(app, path=WEBHOOK_PATH)

    setup_application(app, dp, bot=bot)

    # Run the server
    print("Starting webhook server...")
    await on_startup(bot)
    return app


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(run_webhooks, host=WEBAPP_HOST, port=WEBAPP_PORT)
