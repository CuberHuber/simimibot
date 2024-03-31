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

from src.events import messageEvent
from src.filters import ChatTypeFilter
from src.keyboards import potion_keyboard
from src.types import SiUser, SiStat
from src.db import User, Potion
from src.config import dev
from src.config import AUTODELETE, AUTODELETECOMMAND

general_router = Router()
general_router.message.filter(ChatTypeFilter(chat_type=["group", "supergroup"]))


@general_router.chat_member(
    ChatMemberUpdatedFilter(IS_MEMBER >> IS_NOT_MEMBER),
)
async def on_user_leave(event: ChatMemberUpdated, si_user: SiUser):
    potions = Potion.free()
    await event.answer(
        f'(dev) new user: {event.from_user.full_name}\nВыбери свое зелье',
        reply_markup=potion_keyboard(tuple(potions), si_user, False)
    )


@general_router.message(
    F.text,
)
async def echo(message: Message, si_user: SiUser, si_stats: SiStat) -> None:
    logging.debug(f"(dev) User: {si_user}, stats: {si_stats}, message: {message.text}")
    check = await messageEvent(si_user, message.text)
    if check:
        _rep = await message.reply(f'Вот это норм сообщение. держи кошкожену')
    else:
        _rep = await message.reply(f'.. Хватит спамить')
    await asyncio.sleep(AUTODELETECOMMAND)
    await _rep.delete()
