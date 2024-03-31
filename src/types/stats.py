from dataclasses import dataclass


@dataclass
class SiStat:

    uuid: int  # like a telegram user id
    all: int | None
    trues: int | None
