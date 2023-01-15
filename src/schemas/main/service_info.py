from utilslib.schemas import Model

from enums import BuildEnum


class Status(Model):
    ready: bool
    latest_build: BuildEnum


class ServiceInfo(Model):
    name: str
    status: Status
