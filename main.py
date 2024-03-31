import asyncio

from dotenv import load_dotenv

# Загрузка переменных среды
load_dotenv('.env')

from src.background.statistic import statistic
from src.tgbot import main

if __name__ == '__main__':
    # asyncio.run(main())
    try:
        loop = asyncio.get_event_loop()
        task = loop.create_task(statistic())
        bot = loop.create_task(main())
        loop.run_until_complete(task)
        loop.run_until_complete(bot)
    except asyncio.CancelledError:
        pass
