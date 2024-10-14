from __future__ import annotations

from functools import cached_property
from os import environ

from plexapi.server import PlexServer
from pydantic import BaseModel, HttpUrl, SecretStr
from pydantic_settings import BaseSettings, SettingsConfigDict
from pydantic_settings.sources import PydanticBaseSettingsSource, YamlConfigSettingsSource

from .logging import logger

JELLYPLEX_CONFIG_FILE = environ.get("JELLYPLEX_CONFIG_FILE", "config.yaml")


class PlexSettings(BaseModel):
    url: HttpUrl
    token: SecretStr

    @cached_property
    def client(self) -> PlexServer:
        try:
            return PlexServer(baseurl, token, session=self.session)
        except Exception as e:
            logger.error(f"Plex: Failed to login, Error: {e}")
            raise e


class JellyfinSettings(BaseModel):
    url: HttpUrl
    apikey: SecretStr


class Settings(BaseSettings):
    plex: PlexSettings
    jellyfin: JellyfinSettings

    ssl_verify: bool = True

    model_config = SettingsConfigDict(
        env_prefix="jellyplex_",
        env_nested_delimiter="__",
        yaml_file=JELLYPLEX_CONFIG_FILE,
    )

    @classmethod
    def settings_customise_sources(
        cls,
        settings_cls: type[BaseSettings],
        init_settings: PydanticBaseSettingsSource,
        env_settings: PydanticBaseSettingsSource,
        dotenv_settings: PydanticBaseSettingsSource,
        *sources: PydanticBaseSettingsSource,
    ) -> tuple[PydanticBaseSettingsSource, ...]:
        return (
            init_settings,
            env_settings,
            dotenv_settings,
            YamlConfigSettingsSource(settings_cls),
        )
