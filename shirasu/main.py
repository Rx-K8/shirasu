from pathlib import Path

import typer

from shirasu.bot.discordbot import DiscordBot

SHIRASU_FILE = Path.home() / ".shirasu" / "settings.json"

app = typer.Typer()


@app.command()
def setup(
    is_delete: bool = typer.Option(
        False, "--delete", "-d", help="Delete the settings."
    )
):
    """
    Setup.
    """
    if is_delete:
        DiscordBot.delete()
    else:
        token = typer.prompt("Enter your token")
        chnnel_id = int(typer.prompt("Enter your channel"))
        DiscordBot.setup(token, chnnel_id)


@app.command()
def notify(
    command: str,
    enable_discord: bool = typer.Option(
        False, "--discord", "-d", help="Enable discord notification."
    ),
):
    """
    Notify that the command execution is complete.
    """
    if enable_discord:
        discordbot = DiscordBot.load()
        discordbot.run(command)


if __name__ == "__main__":
    app()
