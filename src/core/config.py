import typing

from pydantic import BaseSettings


class ServicesSettings(BaseSettings):
    ...


def _setup_config(config: typing.Any) -> None:
    config(ServicesSettings, "services_settings")
