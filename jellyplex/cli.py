from __future__ import annotations

from typing import TYPE_CHECKING, Any

import rich_click as click
from pydantic import ValidationError

from . import __name__, __version__
from .config import Settings
from .logging import configure_logging

if TYPE_CHECKING:
    pass


click.rich_click.USE_RICH_MARKUP = True
click.rich_click.USE_MARKDOWN = True


@click.command(
    help="Miscellaneous tools for migrating from Plex to Jellyfin",
)
@click.help_option("-h", "--help")
@click.option(
    "-v",
    "--verbose",
    count=True,
    help="Increase logging verbosity (use multiple times)",
)
@click.version_option(
    __version__,
    "-V",
    "--version",
    prog_name=__name__,
)
@click.pass_context
def main(ctx: click.RichContext, /, **kwargs: Any) -> int:
    configure_logging(kwargs["verbose"])
    try:
        settings = Settings()
    except ValidationError as exc:
        raise click.BadParameter(f"Invalid settings: {exc}") from exc
    except KeyboardInterrupt as exc:  # pragma: no cover
        raise click.Abort("Interrupted by user") from exc
    except FileNotFoundError as exc:
        raise click.Abort(exc) from exc
    return 0


if __name__ == "__main__":
    main.main(prog_name=__name__)
