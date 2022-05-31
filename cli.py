import logging
from pathlib import Path
from app.models import Language
from app.file import FileStory
from click.core import Context, Option
from typing import Optional

import click


CURRENT_PATH = Path(__file__)
logging.basicConfig(level=logging.INFO, format="%(asctime)s %(levelname)s %(name)s: %(message)s")


def prompt_file(ctx: Context, param: Option, is_file: bool) -> Optional[list[str]]:
    if is_file:
        value = ctx.params.get("path")
        if not value:
            value = click.prompt("Story's path")
        return value


def prompt_wattpad(ctx: Context, param: Option, is_wattpad: bool) -> Optional[list[str]]:
    if is_wattpad:
        value = ctx.params.get("url")
        if not value:
            value = click.prompt("Wattpad story's url")
        return value


@click.group()
def cli():
    pass


@cli.command()
@click.option(
    "--language",
    type=click.Choice(Language.list()),
    default=Language.SPANISH,
    prompt="Story's language",
    help="""Story's language.
        Available languages:
        SPANISH = "es-ES"
        ENGLISH = "en-US"
        GERMAN = "de-DE"
    """,
)
@click.option("--file/--no-file", is_flag=True, default=False, callback=prompt_file)
@click.option("--wattpad/--no-wattpad", is_flag=True, default=False, callback=prompt_wattpad)
def run(language, wattpad, file) -> None:
    """ Runs the tts for the given story"""
    if file:
        story = FileStory(file, language)
        story.run()


if __name__ == "__main__":
    cli()