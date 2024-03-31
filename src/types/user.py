from dataclasses import dataclass


@dataclass
class SiUser:

    uuid: int  # like a telegram user id
    name: str
    config: str | None
