from __future__ import annotations

from typing import TYPE_CHECKING

import rich_click as click

if TYPE_CHECKING:
    from jellyplex.models import ContextObj


class Context(click.RichContext):
    obj: ContextObj
