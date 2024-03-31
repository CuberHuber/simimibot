from src.types import SiProfile


def profileForm(profile: SiProfile) -> str:
    text = ''
    if profile.user:
        text += f'(dev) Имя: {profile.user.name}'

    if profile.card:
        text += f'\nКарта: {profile.card}'
    else:
        text += f'\nКарта не выдана системой'

    if profile.rank:
        text += f'\nРанг: {profile.rank.level}\n({profile.rank.name})'
    else:
        text += f'\nПуть не выбран игроком'

    return text
