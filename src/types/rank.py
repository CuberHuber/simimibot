from dataclasses import dataclass


@dataclass
class SiRank:
    potion: int
    level: int
    name: str | None
