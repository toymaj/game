import functools
import typing

from fastapi import params
from fastapi.datastructures import Default
from fastapi.requests import Request
from fastapi.responses import JSONResponse, Response
from fastapi.routing import BaseRoute

from _types import MethodHTTPT

from ._decorated import decorated_logic


def route(
    method: MethodHTTPT,
    gateway: str,
    host: str,
    path: typing.Optional[str] = None,
    response_model: typing.Optional[typing.Type[typing.Any]] = None,
    status_code: typing.Optional[int] = None,
    tags: typing.Optional[typing.List[str]] = None,
    dependencies: typing.Optional[typing.Sequence[params.Depends]] = None,
    summary: typing.Optional[str] = None,
    description: typing.Optional[str] = None,
    response_description: str = "Successful Response",
    responses: typing.Optional[
        typing.Dict[typing.Union[int, str], typing.Dict[str, typing.Any]]
    ] = None,
    deprecated: typing.Optional[bool] = None,
    operation_id: typing.Optional[str] = None,
    response_model_include: typing.Optional[typing.Union[typing.Any, typing.Any]] = None,
    response_model_exclude: typing.Optional[typing.Union[typing.Any, typing.Any]] = None,
    response_model_by_alias: bool = True,
    response_model_exclude_unset: bool = False,
    response_model_exclude_defaults: bool = False,
    response_model_exclude_none: bool = False,
    include_in_schema: bool = True,
    response_class: typing.Type[Response] = Default(JSONResponse),
    name: typing.Optional[str] = None,
    callbacks: typing.Optional[typing.List[BaseRoute]] = None,
    openapi_extra: typing.Optional[typing.Dict[str, typing.Any]] = None,
) -> typing.Callable[[typing.Callable[[typing.Any], typing.Any]], typing.Any]:
    endpoint = method(
        path=gateway,
        response_model=response_model,
        status_code=status_code,
        tags=tags,
        dependencies=dependencies,
        summary=summary,
        description=description,
        response_description=response_description,
        responses=responses,
        deprecated=deprecated,
        operation_id=operation_id,
        response_model_include=response_model_include,
        response_model_exclude=response_model_exclude,
        response_model_by_alias=response_model_by_alias,
        response_model_exclude_unset=response_model_exclude_unset,
        response_model_exclude_defaults=response_model_exclude_defaults,
        response_model_exclude_none=response_model_exclude_none,
        include_in_schema=include_in_schema,
        response_class=response_class,
        name=name,
        callbacks=callbacks,
        openapi_extra=openapi_extra,
    )

    def wrapper(function: typing.Callable[[typing.Any], typing.Any]) -> typing.Any:
        # noinspection PyUnusedLocal
        @endpoint
        @functools.wraps(function)
        async def decorated(
            request: Request,
            **kwargs: typing.Dict[str, typing.Any],
        ) -> Response:
            response = await decorated_logic(
                request=request,
                gateway=gateway,
                host=host,
                path=path,
            )
            return response

    return wrapper
