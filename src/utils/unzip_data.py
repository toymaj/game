from fastapi.requests import Request


async def unzip_data(request: Request) -> bytes:
    data = b""

    try:
        data = await request.body()
    finally:
        return data
