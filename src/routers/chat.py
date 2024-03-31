import asyncio
import logging
import time

from aiogram import F, Router
from aiogram.filters import MagicData
from aiogram.filters import Command, ChatMemberUpdatedFilter, IS_MEMBER, IS_NOT_MEMBER
from aiogram.fsm.context import FSMContext
from aiogram.types import (
    Message,
    ReplyKeyboardRemove, ChatMemberUpdated, )

from src.filters import ChatTypeFilter
from src.types import SiUser, SiStat
from src.db import User
from src.config import dev
from src.config import AUTODELETE

chat_router = Router()


@chat_router.message(Command('help'))
async def help(message: Message) -> None:
    resp = await message.answer("Бот системы повелителя тайн\n"
                                "Чтобы качаться - перейди в канал, в котором он активирован")
    await asyncio.sleep(10)
    await message.delete()
    await resp.delete()


@chat_router.message(Command('stats'))
async def stats(message: Message) -> None:
    ...


@chat_router.message()
async def echo(message: Message, si_user: SiUser = None, si_stats: SiStat = None) -> None:
    resp = await message.reply('/help перейди в канал, для которого активирован этот бот')
    await asyncio.sleep(10)
    await resp.delete()
    await message.delete()
