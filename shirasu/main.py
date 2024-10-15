import asyncio
from pathlib import Path

import typer

from shirasu.bot.discordbot import DiscordBot

SHIRASU_FILE = Path.home() / ".shirasu" / "settings.json"

app = typer.Typer()


@app.command()
def setup(is_delete: bool = typer.Option(False, "--delete", "-d")):
    if is_delete:
        DiscordBot.delete()
    else:
        token = typer.prompt("Enter your token")
        chnnel_id = int(typer.prompt("Enter your channel"))
        DiscordBot.setup(token, chnnel_id)


@app.command()
def send(command: str, enable_discord: bool = typer.Option(False, "--discord", "-d")):
    if enable_discord:
        discordbot = DiscordBot.load()
        discordbot.run(command)


if __name__ == "__main__":
    app()
