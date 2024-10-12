from pathlib import Path

import rich
import typer

from shirasu.io.json_handler import write_json

SHIRASU_FILE = Path.home() / ".shirasu" / "settings.json"

app = typer.Typer()


@app.command()
def setup(is_delete: bool = typer.Option(False, "--delete", "-d")):
    if is_delete:
        try:
            SHIRASU_FILE.unlink()
        except FileNotFoundError:
            rich.print(f"{SHIRASU_FILE} not found")
            exit(1)
        rich.print(f"Settings deleted from {SHIRASU_FILE}")
    else:
        user_name = typer.prompt("Enter your name")
        token = typer.prompt("Enter your token")
        chnnel_id = typer.prompt("Enter your channel")
        settings = {
            "discord": {"user_name": user_name, "token": token, "channel_id": chnnel_id}
        }
        write_json(SHIRASU_FILE, settings)
        rich.print(f"Settings saved to {SHIRASU_FILE}")


if __name__ == "__main__":
    app()
