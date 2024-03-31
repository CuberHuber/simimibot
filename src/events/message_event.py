from src.db import Statistic
from src.types import SiUser
from src.config import WORD_FOR_TRUE_MESSAGE


async def messageEvent(user: SiUser, message: str) -> bool:
    """
    Событие нового сообщения
    :param user:
    :param message:
    :return:
    """
    check = message and len(message.split()) > WORD_FOR_TRUE_MESSAGE
    Statistic.update(user, check)
    return check
