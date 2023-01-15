import typing

from fastapi import HTTPException
from fastapi.requests import Request
from fastapi.responses import Response
from httpx import ConnectError
from starlette import status

from helpers.request import make_request
from helpers.url import generate_url

from ..unzip_data import unzip_data


async def decorated_logic(
    request: Request,
    gateway: str,
    host: str,
    path: typing.Optional[str] = None,
) -> Response:
    content = await unzip_data(request=request)

    try:
        url = generate_url(request=request, gateway=gateway, host=host, path=path)
        _response = await make_request(
            method=request.method.upper(),
            url=url,
            content=content,
            params=request.query_params,
            headers=request.headers,
            cookies=request.cookies,
        )
    except ConnectError:
        raise HTTPException(
            status_code=status.HTTP_503_SERVICE_UNAVAILABLE,
            detail="service is unavailable",
        )

    response = Response(
        content=_response.read(),
        status_code=_response.status_code,
        headers=_response.headers,
    )
    response._cookies = _response.cookies

    return response
