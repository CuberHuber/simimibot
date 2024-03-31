import asyncio
import logging

from aiogram import F, Router
from aiogram.filters import Command
from aiogram.filters.callback_data import CallbackData
from aiogram.fsm.context import FSMContext
from aiogram.types import (
    Message,
    ReplyKeyboardRemove, CallbackQuery, )

from src.filters import ChatTypeFilter
from src.forms import profileForm
from src.types import SiUser, SiStat, SiPotion
from src.db import User, Potion
from src.config import AUTODELETE, AUTODELETECOMMAND
from src.keyboards.potion import potion_keyboard
from src.callback_data import ChoosePotionAction

commands_router = Router()
commands_router.message.filter(ChatTypeFilter(chat_type=["group", "supergroup"]))


@commands_router.message(Command("rank"))
async def user_info_handler(message: Message, si_user: SiUser, si_stats: SiStat = None) -> None:
    """
    Allow user to cancel any action
    """
    print(si_user)
    if si_user:
        try:
            profile = User.profile(si_user)
            _message = await message.reply(profileForm(profile))
            await asyncio.sleep(AUTODELETE)
            await _message.delete()
        except Exception as e:
            logging.warning('Profile not found. Reason: ' + str(e))

    # await asyncio.sleep(10)
    await message.delete()

    # await handle_help(message)


@commands_router.message(Command("add_card"))
async def put_card(message: Message, si_user: SiUser) -> None:
    potions = Potion.free()
    await message.reply(f'{potions}')


@commands_router.message(Command("choose"))
async def put_card(message: Message, si_user: SiUser) -> None:
    potions = Potion.free()
    mes = await message.reply(f'Выбери свой путь, самурай', reply_markup=potion_keyboard(tuple(potions), si_user, False))
    await asyncio.sleep(AUTODELETE)
    await mes.delete()


@commands_router.message(Command('help'))
async def help(message: Message, si_user: SiUser = None, si_stats: SiStat = None) -> None:
    resp = await message.answer('(dev) Привет игрок, это система\nТебе нужно качаться и повышать ранг\nУДАЧИ')
    await asyncio.sleep(AUTODELETE)
    await resp.delete()
    await message.delete()


@commands_router.callback_query(ChoosePotionAction.filter())
async def callback_choose_potion(query: CallbackQuery, callback_data: CallbackData) -> None:
    messages = []

    if query.from_user.id != callback_data.user_id:
        messages.append(await query.message.answer(f'Кто ты такой?'))
        return
    try:
        user = User.auth(query.from_user)
        profile = User.profile(user)
        potion = Potion.potion(callback_data.potion_id)
        is_update = callback_data.is_update
        if (not is_update) and profile.potion:
            messages.append(await query.message.reply(f'You cannot update your potion'))
            # raise KeyError('You cannot update your potion')
            return
        messages.append(await query.message.reply(f'Ты выбрал свой путь, боец\nТы {potion.name}'))
        Potion.choose(user, potion)
    except Exception as e:
        logging.warning(e)
        messages.append(await query.message.answer(f'Братан, не делай то, что тебе не по силам'))

    if messages:
        await asyncio.sleep(AUTODELETECOMMAND)
        for message in messages:
            await message.delete()
