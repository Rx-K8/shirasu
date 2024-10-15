import json
import sys
from typing import Callable

import discord
import rich
from discord.ext import commands

from shirasu.config import SHIRASU_FILE
from shirasu.io.utils import make_directory
from shirasu.logger_config import setup_logger

logger = setup_logger(__name__, "discordbot.log")


class DiscordBot:
    def __init__(
        self,
        token: str,
        channel_id: int,
    ):
        self.token = token
        self.channel_id = channel_id
        self.intents = discord.Intents.all()
        self.bot = commands.Bot(command_prefix="!", intents=self.intents)

    @staticmethod
    def setup(token: str, channel_id: int):
        settings = {"discord": {"token": token, "channel_id": channel_id}}
        make_directory(SHIRASU_FILE.parent)
        with open(SHIRASU_FILE, "w", encoding="utf-8") as json_file:
            json.dump(settings, json_file, ensure_ascii=False, indent=4)

    @staticmethod
    def load():
        settings = {}
        try:
            with open(SHIRASU_FILE, "r", encoding="utf-8") as json_file:
                settings = json.load(json_file)
        except FileNotFoundError:
            logger.error(f"Settings file({SHIRASU_FILE}) not found.")
            rich.print(
                f"\n** Please setup DiscordBot first. Command: $shirasu setup **"
            )
            sys.exit(1)

        token = settings["discord"]["token"]
        channel_id = settings["discord"]["channel_id"]
        return DiscordBot(token=token, channel_id=channel_id)

    def run(self, exec: Callable[[], None]):
        @self.bot.event
        async def on_ready():
            try:
                exec()
                await self.send_message("Hello, world!")
            finally:
                await self.close()

        self.bot.run(self.token)

    async def send_message(self, message: str):
        channel = self.bot.get_channel(self.channel_id)
        await channel.send(message)

    async def close(self):
        await self.bot.close()
