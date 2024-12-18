from aiogram import BaseMiddleware
from aiogram.types import Message


class LoggingMiddleware(BaseMiddleware):
    async def __call__(self, handler, event: Message, data):
        print(f"Received message: {event.text}")
        return await handler(event, data)
