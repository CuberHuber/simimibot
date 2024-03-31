import asyncio
from src.config import INTERVAL, BOT_TOKEN, CHAT
from aiogram import Bot
from src.db import Statistic


async def statistic():
    while True:
        bot = Bot(token=BOT_TOKEN)
        toplist = Statistic.toplist()
        if toplist:
            await bot.send_message(CHAT, f'(dev) Тест таймера. Раз в {INTERVAL} sec\nТоп лист кандидатов в повышение:\n{toplist}')
        else:
            await bot.send_message(CHAT, f'(dev) Тест таймера. Раз в {INTERVAL} sec')
        await asyncio.sleep(INTERVAL)
