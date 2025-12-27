from lightcord.typedata import TypeData
from typing import Any

class User(TypeData):
    verified: bool
    username: str
    primary_guild: Any
    mfa_enabled: bool
    id: str
    global_name: str
    flags: int
    email: str
    discriminator: str
    clan: Any
    bot: bool
    avatar: Any