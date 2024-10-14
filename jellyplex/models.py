from __future__ import annotations

from pydantic import BaseModel

from jellyplex.config import Settings  # noqa: TCH001


class ContextObj(BaseModel):
    settings: Settings
