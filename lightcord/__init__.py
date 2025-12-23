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

"""Lightcord is a python library for interacting with the discord API and Gateway.

* **Documentation:** https://dispy.gitbook.io/docs
* **Github Page:** https://github.com/git-jamesfrench/Lightcord
* **License:** [GPL-3.0](https://www.gnu.org/licenses/gpl-3.0.fr.html)"""

from lightcord.gateway import Gateway
from lightcord.literals import Events
from typing import Callable

class Client():
    def __init__(self, token: str, intents: int | str = None):
        """Define a discord client.
        
        :param token: Your private token. You can get it on your Developer Portal.
        :type token: `str`
        :param intents: The intents to send over to discord, this is optional because Lightcord already generate an intents.
        :type intents: Optional `int | str`"""
        # Main Variables
        self.token = token
        if intents: self.intents = int(intents)
        
        # Modules
        self.gateway = Gateway(token=self.token, intents=self.intents)
        
        # Functionalites
        self.handler = {}
        
    async def start(self):
        """Start your client, make it online and able to receive events from discord."""
        await self.gateway.start()
        
    async def on(self, eventname: Events = None, function: Callable = None, *, once: bool = False) -> None:
        """
        Add a function to call when a specific event is dispatched.
        """
        def decorator(fn):
            pass
        if function is not None: return decorator(function)
        else: return decorator