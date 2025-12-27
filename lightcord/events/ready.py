from lightcord.typedata import TypeData
from typing import Any

from lightcord.types.User import User
from lightcord.types.Guild import Guild
from lightcord.types.Application import Application

class Ready(TypeData):
    v: int
    user_settings: dict
    user: User
    session_type: str
    session_id: str
    resume_gateway_url: str
    relationships: list
    private_channels: list
    presences: list
    guilds: list[Guild]
    guild_join_requests: list
    geo_ordered_rtc_regions: list[str]
    game_relationships: list
    auth: dict
    application: Application