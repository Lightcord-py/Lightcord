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

"""
Events given by discord.

You can import types like this:
```
import lightcord.events as events

events.Ready
```
(This is still optimized with lazy imports)
"""

# Magnificient Lazy Importing, yes this was vibecoded, may get back to it but I understand how it works and it's great

from typing import TYPE_CHECKING
import importlib

_module_map = { # Where is located a function
    "Ready": "lightcord.events.ready",
    "Message_Delete": "lightcord.events.message_delete",
}

if TYPE_CHECKING: # The IDE thinks were importing it, but when executing, it does SHIT, NOTHING, THIS SHIT IS FUCKING CONFUSING
    from lightcord.events.ready import Ready
    from lightcord.events.message_delete import Message_Delete

__all__ = list(_module_map.keys())

def __getattr__(name: str):
    if name in _module_map:
        module = importlib.import_module(_module_map[name])
        value = getattr(module, name)
        globals()[name] = value # Honestly, it was chatgpt that said this was important, so we don't go though __getattr__ everytime we want something, but i don't know how it works! i'm learning
        return value
    raise AttributeError(f"module 'events' doesn't have the attribute {name}.")

import importlib.util

events_list = [
    "GUILD_BAN_ADD",
    "MESSAGE_UPDATE",
    "GUILD_CREATE",
    "DIRECT_MESSAGE_REACTION_REMOVE_ALL",
    "GUILD_ROLE_CREATE",
    "GUILD_SCHEDULED_EVENT_CREATE",
    "GUILD_DELETE",
    "GUILD_SCHEDULED_EVENT_UPDATE",
    "ALL",
    "MESSAGE_REACTION_REMOVE_ALL",
    "GUILD_MEMBER_REMOVE",
    "INVITE_DELETE",
    "STAGE_INSTANCE_CREATE",
    "DIRECT_CHANNEL_PINS_UPDATE",
    "CHANNEL_DELETE",
    "GUILD_ROLE_UPDATE",
    "DIRECT_MESSAGE_CREATE",
    "DIRECT_MESSAGE_REACTION_REMOVE_EMOJI",
    "MESSAGE_DELETE_BULK",
    "THREAD_UPDATE",
    "MESSAGE_POLL_VOTE_REMOVE",
    "GUILD_SOUNDBOARD_SOUND_DELETE",
    "VOICE_STATE_UPDATE",
    "GUILD_INTEGRATIONS_UPDATE",
    "USER_UPDATE",
    "GUILD_ROLE_DELETE",
    "MESSAGE_REACTION_REMOVE",
    "DIRECT_MESSAGE_UPDATE",
    "MESSAGE_DELETE",
    "GUILD_SCHEDULED_EVENT_DELETE",
    "THREAD_MEMBER_UPDATE",
    "PRESENCE_UPDATE",
    "INTEGRATION_UPDATE",
    "GUILD_SOUNDBOARD_SOUND_CREATE",
    "WEBHOOKS_UPDATE",
    "GUILD_AUDIT_LOG_ENTRY_CREATE",
    "AUTO_MODERATION_RULE_DELETE",
    "READY",
    "AUTO_MODERATION_RULE_UPDATE",
    "THREAD_CREATE",
    "DIRECT_MESSAGE_POLL_VOTE_ADD",
    "RESUMED",
    "INTEGRATION_DELETE",
    "GUILD_UPDATE",
    "THREAD_DELETE",
    "GUILD_SOUNDBOARD_SOUNDS_UPDATE",
    "INVITE_CREATE",
    "MESSAGE_POLL_VOTE_ADD",
    "DIRECT_MESSAGE_REACTION_REMOVE",
    "CHANNEL_PINS_UPDATE",
    "MESSAGE_REACTION_REMOVE_EMOJI",
    "GUILD_MEMBER_UPDATE",
    "GUILD_MEMBER_ADD",
    "CHANNEL_CREATE",
    "VOICE_CHANNEL_EFFECT_SEND",
    "MESSAGE_REACTION_ADD",
    "GUILD_SCHEDULED_EVENT_USER_REMOVE",
    "GUILD_EMOJIS_UPDATE",
    "INTERACTION_CREATE",
    "DIRECT_MESSAGE_POLL_VOTE_REMOVE",
    "CHANNEL_UPDATE",
    "GUILD_BAN_REMOVE",
    "DIRECT_MESSAGE_DELETE",
    "VOICE_SERVER_UPDATE",
    "DIRECT_TYPING_START",
    "AUTO_MODERATION_RULE_CREATE",
    "GUILD_STICKERS_UPDATE",
    "MESSAGE_CREATE",
    "STAGE_INSTANCE_UPDATE",
    "THREAD_LIST_SYNC",
    "GUILD_SCHEDULED_EVENT_USER_ADD",
    "TYPING_START",
    "GUILD_SOUNDBOARD_SOUND_UPDATE",
    "INTEGRATION_CREATE",
    "THREAD_MEMBERS_UPDATE",
    "DIRECT_MESSAGE_REACTION_ADD",
    "AUTO_MODERATION_ACTION_EXECUTION",
    "STAGE_INSTANCE_DELETE"
]

intents = {
   "-1": [
      "READY",
      "RESUMED",
      "VOICE_SERVER_UPDATE",
      "USER_UPDATE",
      "INTERACTION_CREATE",
      "ALL"
   ],
   "0": [
      "GUILD_CREATE",
      "GUILD_UPDATE",
      "GUILD_DELETE",
      "GUILD_ROLE_CREATE",
      "GUILD_ROLE_UPDATE",
      "GUILD_ROLE_DELETE",
      "CHANNEL_CREATE",
      "CHANNEL_UPDATE",
      "CHANNEL_DELETE",
      "CHANNEL_PINS_UPDATE",
      "THREAD_CREATE",
      "THREAD_UPDATE",
      "THREAD_DELETE",
      "THREAD_LIST_SYNC",
      "THREAD_MEMBER_UPDATE",
      "THREAD_MEMBERS_UPDATE",
      "STAGE_INSTANCE_CREATE",
      "STAGE_INSTANCE_UPDATE",
      "STAGE_INSTANCE_DELETE",
      "MESSAGE_CREATE",
      "MESSAGE_UPDATE",
      "MESSAGE_DELETE",
      "MESSAGE_DELETE_BULK",
      "ALL"
   ],
   "1": [
      "GUILD_MEMBER_ADD",
      "GUILD_MEMBER_UPDATE",
      "GUILD_MEMBER_REMOVE",
      "THREAD_MEMBERS_UPDATE",
      "ALL"
   ],
   "2": [
      "GUILD_AUDIT_LOG_ENTRY_CREATE",
      "GUILD_BAN_ADD",
      "GUILD_BAN_REMOVE",
      "ALL"
   ],
   "3": [
      "GUILD_EMOJIS_UPDATE",
      "GUILD_STICKERS_UPDATE",
      "GUILD_SOUNDBOARD_SOUND_CREATE",
      "GUILD_SOUNDBOARD_SOUND_UPDATE",
      "GUILD_SOUNDBOARD_SOUND_DELETE",
      "GUILD_SOUNDBOARD_SOUNDS_UPDATE",
      "ALL"
   ],
   "4": [
      "GUILD_INTEGRATIONS_UPDATE",
      "INTEGRATION_CREATE",
      "INTEGRATION_UPDATE",
      "INTEGRATION_DELETE",
      "ALL"
   ],
   "5": [
      "WEBHOOKS_UPDATE",
      "ALL"
   ],
   "6": [
      "INVITE_CREATE",
      "INVITE_DELETE",
      "ALL"
   ],
   "7": [
      "VOICE_CHANNEL_EFFECT_SEND",
      "VOICE_STATE_UPDATE",
      "ALL"
   ],
   "8": [
      "PRESENCE_UPDATE",
      "ALL"
   ],
   "9": [
      "MESSAGE_CREATE",
      "MESSAGE_UPDATE",
      "MESSAGE_DELETE",
      "MESSAGE_DELETE_BULK",
      "ALL"
   ],
   "10": [
      "MESSAGE_REACTION_ADD",
      "MESSAGE_REACTION_REMOVE",
      "MESSAGE_REACTION_REMOVE_ALL",
      "MESSAGE_REACTION_REMOVE_EMOJI",
      "ALL"
   ],
   "11": [
      "TYPING_START",
      "ALL"
   ],
   "12": [ 
      "DIRECT_MESSAGE_CREATE",
      "DIRECT_MESSAGE_UPDATE",
      "DIRECT_MESSAGE_DELETE",
      "DIRECT_CHANNEL_PINS_UPDATE",
      "ALL"
   ],
   "13": [
      "DIRECT_MESSAGE_REACTION_ADD",
      "DIRECT_MESSAGE_REACTION_REMOVE",
      "DIRECT_MESSAGE_REACTION_REMOVE_ALL",
      "DIRECT_MESSAGE_REACTION_REMOVE_EMOJI",
      "ALL"
   ],
   "14": [
      "DIRECT_TYPING_START",
      "ALL"
   ],
   "15": [
      "MESSAGE_CREATE",
      "MESSAGE_UPDATE",
      "MESSAGE_DELETE",
      "MESSAGE_DELETE_BULK",
      "MESSAGE_POLL_VOTE_ADD",
      "MESSAGE_POLL_VOTE_REMOVE",
      "ALL"
   ],
   "16": [
      "GUILD_SCHEDULED_EVENT_CREATE",
      "GUILD_SCHEDULED_EVENT_UPDATE",
      "GUILD_SCHEDULED_EVENT_DELETE",
      "GUILD_SCHEDULED_EVENT_USER_ADD",
      "GUILD_SCHEDULED_EVENT_USER_REMOVE",
      "ALL"
   ],
   "20": [
      "AUTO_MODERATION_RULE_CREATE",
      "AUTO_MODERATION_RULE_UPDATE",
      "AUTO_MODERATION_RULE_DELETE",
      "ALL"
   ],
   "21": [
      "AUTO_MODERATION_ACTION_EXECUTION",
      "ALL"
   ],
   "24": [
      "MESSAGE_POLL_VOTE_ADD",
      "MESSAGE_POLL_VOTE_REMOVE",
      "ALL"
   ],
   "25": [
      "DIRECT_MESSAGE_POLL_VOTE_ADD",
      "DIRECT_MESSAGE_POLL_VOTE_REMOVE",
      "ALL"
   ]
}

direct_intents = [
    "MESSAGE_CREATE",
    "MESSAGE_UPDATE",
    "MESSAGE_DELETE",
    "MESSAGE_DELETE_BULK",
    "MESSAGE_REACTION_ADD",
    "MESSAGE_REACTION_REMOVE",
    "MESSAGE_REACTION_REMOVE_ALL",
    "MESSAGE_REACTION_REMOVE_EMOJI",
    "TYPING_START",
    "MESSAGE_POLL_VOTE_ADD",
    "MESSAGE_POLL_VOTE_REMOVE",
]

events_alias = {
    "ON_READY": "READY",
    "ON_MESSAGE": "MESSAGE_CREATE",
    "ON_MESSAGE_CREATE": "MESSAGE_CREATE",
    "ON_MESSAGE_UPDATE": "MESSAGE_UPDATE",
    "ON_MESSAGE_EDIT": "MESSAGE_UPDATE",
    "ON_MESSAGE_DELETE": "MESSAGE_DELETE",
    "ON_DIRECT_MESSAGE": "DIRECT_MESSAGE_CREATE",
    "ON_DIRECT_MESSAGE_CREATE": "DIRECT_MESSAGE_CREATE",
    "ON_DIRECT_MESSAGE_UPDATE": "DIRECT_MESSAGE_UPDATE",
    "ON_DIRECT_MESSAGE_EDIT": "DIRECT_MESSAGE_UPDATE",
    "ON_DIRECT_MESSAGE_DELETE": "DIRECT_MESSAGE_DELETE",
    #"ON_ALL_MESSAGE": ["MESSAGE_CREATE", "DIRECT_MESSAGE_CREATE"],
    #"ON_ALL_MESSAGE_CREATE": ["MESSAGE_CREATE", "DIRECT_MESSAGE_CREATE"],
    #"ON_ALL_MESSAGE_UPDATE": ["MESSAGE_UPDATE", "DIRECT_MESSAGE_UPDATE"],
    #"ON_ALL_MESSAGE_EDIT": ["MESSAGE_UPDATE", "DIRECT_MESSAGE_UPDATE"],
    #"ON_ALL_MESSAGE_DELETE": ["MESSAGE_DELETE", "DIRECT_MESSAGE_DELETE"],
}

def find_event(event: str):
    if importlib.util.find_spec(f"lightcord.events.{event.lower()}"):
        module = importlib.import_module(f"lightcord.events.{event.lower()}")
        return (getattr(module, "main"), getattr(module, "__types__"))
    return (None, None)