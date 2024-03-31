from typing import Tuple

from .main import connect
from src.types import SiUser, SiStat
from src.config import TOPLIMIT


class Statistic:

    @classmethod
    def update(cls, user: SiUser, _true: bool = False):

        with connect() as connection:
            cursor = connection.cursor()
            if _true:
                cursor.execute(
                    'INSERT INTO statistic (uuid, messages, true_messages) VALUES (?, ?, ?) ON CONFLICT (uuid) DO '
                    'UPDATE SET messages = messages + 1, true_messages = true_messages + 1', (user.uuid, 0, 0)).fetchone()
            else:
                cursor.execute(
                    'INSERT INTO statistic (uuid, messages) VALUES (?, ?) ON CONFLICT (uuid) DO UPDATE SET messages = messages + 1',
                    (user.uuid, 0)).fetchone()
            connection.commit()

    @classmethod
    def info(cls, user: SiUser) -> SiStat | ValueError:
        with connect() as connection:
            cursor = connection.cursor()
            row = cursor.execute('SELECT uuid, messages, true_messages FROM statistic WHERE uuid = ?', (user.uuid, )).fetchone()
            connection.commit()
            if row:
                stats = SiStat(row[0], row[1], row[2])
                return stats

        raise ValueError('No statistic for user {}, {}'.format(user.uuid, user.name))

    @classmethod
    def toplist(cls) -> tuple[SiStat] | ValueError:
        """select uuid, true_messages from statistic where true_messages > 0 order by true_messages desc limit 3;"""
        with connect() as connection:
            cursor = connection.cursor()
            top_list = cursor.execute('select uuid, messages, true_messages from statistic where true_messages > 0 order by true_messages desc limit ?', (TOPLIMIT, )).fetchall()
            connection.commit()
            if top_list:
                stats = []
                for el in top_list:
                    stats.append(SiStat(el[0], el[1], el[2]))
                return tuple(stats)

        raise ValueError('No candidate for top list')