from .main import connect
from src.types import SiUser, SiStat, SiPotion
from src.config import TOPLIMIT
import logging


class Potion:

    @classmethod
    def free(cls):

        with connect() as connection:
            cursor = connection.cursor()
            free_potions = cursor.execute('select id, name from main.potion where id not in (select p2.id from main.profile p join main.potion p2 on p2.id = p.potion)', ()).fetchall()
            connection.commit()
            if free_potions:
                potions = []
                for row in free_potions:
                    potions.append(SiPotion(row[0], row[1]))
                return potions

        raise ValueError('No free potions found')

    @classmethod
    def choose(cls, user: SiUser, potion: SiPotion, _update: bool = False):
        """
        Установка Potion для пользователя (либо обновление зелья)
        :param user:
        :param potion:
        :param _update:
        """
        with connect() as connection:
            cursor = connection.cursor()
            is_potion = cursor.execute('select potion from main.profile where uuid = ?', (user.uuid, )).fetchone()
            if (not _update) and is_potion[0]:
                raise KeyError(f'User: {user} already has a potion')
            cursor.execute('update main.profile set potion = ? where uuid = ?', (potion.id, user.uuid)).fetchone()
            logging.debug(f'user: {user} update potion: {potion}')
            connection.commit()

    @classmethod
    def potion(cls, uuid: int) -> SiPotion:
        with connect() as connection:
            cursor = connection.cursor()
            row = cursor.execute('select id, name from main.potion where id = ?', (uuid, )).fetchone()
            if row:
                return SiPotion(row[0], row[1])
            connection.commit()
            raise KeyError(f'Potion with uuid {uuid} not found')
