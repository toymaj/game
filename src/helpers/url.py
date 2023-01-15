import typing

from fastapi.requests import Request


def generate_url(
    request: Request,
    gateway: str,
    host: str,
    path: typing.Optional[str] = None,
) -> str:
    path_params = request.scope.get("path_params", {})

    _path = f"{host}{gateway}"
    if path:
        _path = f"{host}{path}"

    return _path.format(**path_params)
