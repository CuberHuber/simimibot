import logging

from aiogram import BaseMiddleware
from aiogram.dispatcher.event.bases import SkipHandler

from src.db import User, Statistic
from src.types import SiUser


class AuthMiddleware(BaseMiddleware):
    async def __call__(self, handler, event, data):
        try:
            user = User.auth(event.from_user)
            logging.debug(f"Authorized user: {user}")
            data["si_user"] = user
        except Exception as e:
            logging.warning(
                f"No authorized user={event.from_user.username} id={event.from_user.id}"
            )
            raise SkipHandler()
        return await handler(event, data)


class StatsUserMiddleware(BaseMiddleware):

    async def __call__(self, handler, event, data):
        try:
            user: SiUser = data.get('si_user')
            if user:
                # Statistic.update(user)
                stats = Statistic.info(user)
                data["si_stats"] = stats
            else:
                logging.warning(
                    f"User not found id={event.from_user.id}"
                )

        except Exception as e:
            logging.warning(
                f"No update stats user={event.from_user.username} id={event.from_user.id}. Error: {e}"
            )
            raise SkipHandler()
        return await handler(event, data)



# class UsersPrivilegeFilter(BaseMiddleware):
#
#     def __init__(self, privilege: str | tuple[str]):
#         self.privilege = privilege
#
#     async def __call__(self, handler, event, data) -> bool:
#         """
#         Проверка на соответствие праву пользователя
#         :param message:
#         :param spp_user:
#         :return:
#         """
#         if isinstance(self.privilege, str):
#             # Одна роль
#             if self.privilege in data.get("spp_user").privilege.get('bot'):
#                 return await handler(event, data)
#
#         elif isinstance(self.privilege, tuple):
#             # несколько ролей
#             for priv in self.privilege:
#                 if priv not in data.get("spp_user").privilege.get('bot'):
#                     break
#             else:
#                 return await handler(event, data)
#
#         logging.warning(
#             f"User={event.from_user.username} id={event.from_user.id} hasn't authorized privilege={self.privilege}"
#         )
#         # raise CancelHandler()
#         raise SkipHandler()
