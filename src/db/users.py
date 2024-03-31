from aiogram.types import User as tUser

from .main import connect
from src.types import SiUser, SiProfile, SiRank, SiPotion


class User:

    @classmethod
    def auth(cls, _user: tUser) -> SiUser:
        """

        :param _user: 
        :return:
        """
        with connect() as connection:
            cursor = connection.cursor()
            row = cursor.execute('SELECT telegram, name, config  FROM users WHERE telegram = ?', (_user.id,)).fetchone()
            print('row:', row)
            if row:
                user = SiUser(row[0], row[1], row[2])
            else:
                nu = cursor.execute('INSERT INTO users (telegram, name) VALUES (?, ?) RETURNING (telegram)', (_user.id, _user.full_name)).fetchone()
                print(nu)
                cursor.execute('INSERT INTO profile (uuid, card, rank) VALUES (?, ?, ?)', (_user.id, None, 9)).fetchone()
                user = SiUser(nu[0], _user.full_name, None)
            connection.commit()
        print(user)
        return user

    @classmethod
    def profile(cls, _user: SiUser) -> SiProfile:
        with connect() as connection:
            cursor = connection.cursor()
            row = cursor.execute('SELECT p.uuid, p.card, p2.id, p2.name, r.level, r.name FROM profile p left join main.potion p2 on p2.id = p.potion left join main.rank r on r.potion = p.potion and r.level = p.level WHERE p.uuid = ?', (_user.uuid, )).fetchone()
            if row:
                profile = SiProfile(_user, row[1], None, None)
                if row[2]:
                    profile.potion = SiPotion(row[2], row[3])
                if row[2] and row[4]:
                    profile.rank = SiRank(row[2], row[4], row[5])

                return profile

        raise ValueError('No Profile for user {}, {}'.format(_user.uuid, _user.name))
