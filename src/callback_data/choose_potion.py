from aiogram.filters.callback_data import CallbackData


class ChoosePotionAction(CallbackData, prefix="potion"):
    user_id: int
    potion_id: int
    is_update: bool
