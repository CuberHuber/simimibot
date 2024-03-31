import asyncio
import logging

from aiogram import Router
from aiogram.filters import CommandStart
from aiogram.types import Message
from aiogram.utils.markdown import hbold, hcode

from src.filters import ChatTypeFilter
from src.routers.chat import help as chat_help
from src.routers.commands import help as group_help
from src.db import Statistic
from src.types import SiUser, SiStat
from src.config import AUTODELETE

root_router = Router()


@root_router.message(
    CommandStart(),
    ChatTypeFilter(chat_type=["group", "supergroup"])
)
async def handle_start(message: Message, si_user: SiUser = None) -> None:
    _new_message = await message.answer(f'Система повелителя тайн. Начни свое возвышение в тени...')
    await message.reply(f'{message.chat.id}\n{message.chat.full_name}')
    await group_help(message)
    await asyncio.sleep(AUTODELETE)
    await message.delete()
    await _new_message.delete()


@root_router.message(CommandStart())
async def handle_start(message: Message, si_user: SiUser = None) -> None:
    _new_message = await message.answer(f'hello {message.chat.full_name}')
    await chat_help(message)
