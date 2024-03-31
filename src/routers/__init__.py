from .root import root_router
from .commands import commands_router
from .general import general_router
from .chat import chat_router

__all__ = [
    "root_router",
    "commands_router",
    "general_router",
    "chat_router",
]
