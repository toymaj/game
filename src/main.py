from fastapi import FastAPI
from starlette import status

from api import api_router
from core import register_middlewares
from enums import BuildEnum
from schemas import ServiceInfo


def create_application() -> FastAPI:
    application = FastAPI(
        openapi_url="/api.main/openapi.json",
        docs_url="/api.main/docs",
        redoc_url="/api.main/redoc",
    )
    application.include_router(api_router, prefix="/api.main")

    @application.on_event(event_type="startup")
    async def startup() -> None:
        ...

    @application.on_event(event_type="shutdown")
    async def shutdown() -> None:
        ...

    register_middlewares(app=application)

    return application


app = FastAPI()


@app.get(
    path="/service.info",
    response_model=ServiceInfo,
    status_code=status.HTTP_200_OK,
)
async def service_info() -> ServiceInfo:
    LATEST_BUILD = BuildEnum.SUCCESSFULLY

    return {
        "name": "main",
        "status": {
            "ready": False,
            "latest_build": LATEST_BUILD,
        },
    }
