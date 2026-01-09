# Lightcord - A lightweight, modern and optimized Discord API wrapper for Python. 
# Copyright (C) 2025  Jamesfrench_
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <https://www.gnu.org/licenses/>.

from lightcord.typedata import TypeData

from lightcord.variables import Snowflake

class AvatarDecorationData(TypeData):
    asset: str
    sku_id: Snowflake
    expires_at: int
    label: str
    palette: str

class GuildTag(TypeData):
    tag: str
    identity_guild_id: int
    identity_enabled: bool
    badge: str

class Collectibles(TypeData):
    nameplate: AvatarDecorationData

class User(TypeData):
    id: Snowflake
    username: str
    discriminator: str
    display_name: str
    global_name: str
    avatar: str
    clan: GuildTag
    bot: bool
    system: bool
    mfa_enabled: bool
    verified: bool
    email: str
    locale: str
    flags: int
    banner: str
    banner_color: int
    accent_color: int
    premium_type: int
    public_flags: int
    primary_guild: GuildTag
    avatar_decoration_data: AvatarDecorationData

    def __init__(self, data, api = None):
        super().__init__(data, api)
        
        if not self.bot: self.bot = False