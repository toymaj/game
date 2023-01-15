import typing

from httpx import AsyncClient, Response

from enums import HTTPMethod


async def make_request(
    method: HTTPMethod,
    **kwargs: typing.Dict[str, typing.Any],
) -> Response:
    async with AsyncClient() as client:
        response = await client.request(
            method=method,
            **kwargs,
        )

    return response
