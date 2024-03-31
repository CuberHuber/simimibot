from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton

from ..types import SiPotion, SiUser
from ..utils.list2matrix import list2matrix
from ..callback_data import ChoosePotionAction


def potion_keyboard(_potions: tuple[SiPotion], _user: SiUser, is_update: bool) -> InlineKeyboardMarkup:
    keyboards = []

    for potion in _potions:
        keyboards.append(InlineKeyboardButton(
            text=potion.name,
            callback_data=ChoosePotionAction(
                user_id=_user.uuid,
                potion_id=potion.id,
                is_update=is_update
            ).pack()
        ))

    return InlineKeyboardMarkup(inline_keyboard=list2matrix(keyboards, 2))