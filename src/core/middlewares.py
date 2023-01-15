from __future__ import annotations

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware


def cors_middleware(app: FastAPI) -> None:
    app.add_middleware(
        CORSMiddleware,
        allow_origins=["*"],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )


def register_http_middlewares(app: FastAPI) -> None:
    """
    Sets all middlewares for HTTP

    :param app:
      web app instance
    :return:
      None
    """

    cors_middleware(app=app)


def register_middlewares(app: FastAPI) -> None:
    """
    Sets all middlewares for HTTP and WebSocket

    :param app:
      web app instance
    :return:
      None
    """

    register_http_middlewares(app=app)
