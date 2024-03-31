import asyncio
import logging
import sys

from aiogram import Bot, Dispatcher
from aiogram.enums import ParseMode

from src.middleware import AuthMiddleware, StatsUserMiddleware

try:
    from .config import BOT_TOKEN
    from .routers import root_router, commands_router, general_router, chat_router
except ImportError:
    from config import BOT_TOKEN
    from routers import root_router, commands_router, general_router, chat_router

# Configure logging
logging.basicConfig(level=logging.DEBUG, stream=sys.stdout)


async def main() -> None:
    # Initialize Bot instance with a default parse mode which will be passed to all API calls
    bot = Bot(BOT_TOKEN, parse_mode=ParseMode.HTML)
    dispatcher = Dispatcher()

    # root_router.message.middleware.register(AuthMiddleware())
    # root_router.message.middleware.register(StatsUserMiddleware())
    commands_router.message.middleware.register(AuthMiddleware())
    # commands_router.message.middleware.register(StatsUserMiddleware())
    general_router.message.middleware.register(AuthMiddleware())
    general_router.message.middleware.register(StatsUserMiddleware())
    dispatcher.include_routers(root_router, commands_router, general_router, chat_router)
    print(await bot.get_webhook_info())
    await dispatcher.start_polling(bot, polling_timeout=2)


if __name__ == '__main__':
    asyncio.run(main())
