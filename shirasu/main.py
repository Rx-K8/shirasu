from pathlib import Path

import rich
import typer

from shirasu.io.json_handler import write_json

SHIRASU_FILE = Path.home() / ".shirasu" / "settings.json"

app = typer.Typer()


@app.command()
def setting():
    user_name = typer.prompt("Enter your name")
    token = typer.prompt("Enter your token")
    settings = {"discord": {"user_name": user_name, "token": token}}
    write_json(SHIRASU_FILE, settings)
    rich.print(f"Settings saved to {SHIRASU_FILE}")


@app.command()
def discord():
    print("Discord")


if __name__ == "__main__":
    app()
