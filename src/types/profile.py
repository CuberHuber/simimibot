from dataclasses import dataclass

from src.types.rank import SiRank
from src.types.user import SiUser
from src.types.potion import SiPotion


@dataclass
class SiProfile:

    user: SiUser  # like a telegram user id
    card: int | None
    rank: SiRank | None
    potion: SiPotion | None
