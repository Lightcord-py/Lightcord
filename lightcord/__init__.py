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

* **Github Page:** https://github.com/lightcord-py/Lightcord
* **License:** [GPL-3.0](https://www.gnu.org/licenses/gpl-3.0.fr.html)"""

from lightcord.gateway import Gateway
from lightcord.handlers import Handlers
from lightcord.literals import Events
from lightcord.events import events_list, events_alias
from typing import Callable
from inspect import iscoroutinefunction
import asyncio
from lightcord.rest_api import RestAPI

#    __ _       _     _                    _ 
#   / /(_) __ _| |__ | |_ ___ ___  _ __ __| |
#  / / | |/ _` | '_ \| __/ __/ _ \| '__/ _` |
# / /__| | (_| | | | | || (_| (_) | | | (_| |
# \____/_|\__, |_| |_|\__\___\___/|_|  \__,_|
#         |___/                              

import logging
logger = logging.getLogger(__name__).addHandler(logging.NullHandler())

class Client():
    def __init__(self, token: str = None, intents: int | str = 0):
        """Define a discord client.
        
        :param token: Your private token. You can get it on your Developer Portal.
        :type token: Optional[`str`]
        :param intents: The intents to send over to discord.
        :type intents: Optional[`int | str`]
        """
        self.intents = int(intents)

        self.rest_api = RestAPI(token)
        self.handlers = Handlers(self.rest_api)
        self.gateway = Gateway(token, intents)

    async def start_async(self, token: str = None, intents: int | str = 0):
        """Start your client, making it online and able to receive events from discord.
        
        :param token: Your private token. You can get it on your Developer Portal.
        :type token: Optional[`str`]
        :param intents: The intents to send over to discord.
        :type intents: Optional[`int | str`]
        """
        if token: self.gateway.token = token; self.rest_api.token = token
        if intents: self.gateway.intents = intents

        # Adding events in class, for using lightcord with a class.
        for value in self.__dir__():
            function_name = value.upper()

            if function_name in events_list:
                self.on(function_name, getattr(self, function_name))
            elif function_name in events_alias:
                self.on(events_alias[function_name], getattr(self, function_name))

        self.gateway.handlers = self.handlers
        
        await self.gateway.start()

    def start(self, token: str = None, intents: int | str = 0):
        """Start your client, making it online and able to receive events from discord.
        
        :param token: Your private token. You can get it on your Developer Portal.
        :type token: Optional[`str`]
        :param intents: The intents to send over to discord.
        :type intents: Optional[`int | str`]
        """
        
        asyncio.run(self.start_async(token=token, intents=intents))
        
    async def stop(self) -> None:
        """Stop your client gracefully, making it offline and unable to receive events from discord."""
        await self.gateway.stop()
        await self.rest_api.close()
        
    def on(self, event: Events = None, function: Callable = None, *, once: bool = False):
        """
        Will call `function` when `event` happen. Will automatically add needed intents if intents are not defined by the user.
        
        Can be used as a decorator: 
        ```
        @bot.on("READY")
        async def on_ready():
            print("READY!")
        ```
        :param event: The event that will trigger the defined function. Function name will be used if not given.
        :type event: Optional[`str`]
        :param function: The function that will be called when the defined event happen.
        :type function: Optional[`Callable`]
        :param once: Will make the function be triggered once when event happens, making others occurrences be ignored.
        :type once: Optional[`bool`]
        """
        def decorator(fn):
            if iscoroutinefunction(fn):
                # Checking if we can use the name of the function as the event
                if event is None:
                    function_name = fn.__name__.upper()

                    if function_name in events_list:
                        eventname = function_name
                    elif function_name in events_alias:
                        eventname = events_alias[function_name]
                    else:
                        raise ValueError(f'{fn.__name__} is not a valid event.')
                else:
                    eventname = event


                # Making the function an handler
                self.handlers.add_handler(eventname, fn, once)
            else:
                raise ValueError(f'{fn} is not a coroutine!')
        if function is not None: return decorator(function)
        else: return decorator
        
    def once(self, event: Events = None, function: Callable = None):
        """
        Will call `function` once when `event` happen. Will automatically add needed intents if intents are not defined by the user. 
        
        The `function` will be called once, others occurrences of the `event` will be ignored.
        
        Can be used as a decorator: 
        ```
        @bot.once("READY")
        async def on_ready():
            print("READY!")
        ```
        :param event: The event that will trigger the defined function. Function name will be used if not given.
        :type event: Optional[`str`]
        :param function: The function that will be called when the defined event happen.
        :type function: Optional[`Callable`]
        """
        def decorator(fn):
            self.on(event = event, function = fn, once = True)
        if function is not None: return decorator(function)
        else: return decorator