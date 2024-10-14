from __future__ import annotations

from typing import TYPE_CHECKING, Any

import rich_click as click

from jellyplex.utils import pass_ctxobj

if TYPE_CHECKING:
    from jellyplex.models import ContextObj


@click.command("sync-posters")
@pass_ctxobj
def command(obj: ContextObj, /, **kwargs: Any) -> None:
    print("ctx", obj)
