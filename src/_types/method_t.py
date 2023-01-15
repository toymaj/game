import typing

from fastapi.responses import Response
from fastapi.routing import APIRoute, BaseRoute

DictIntStrAny = typing.Dict[typing.Union[int, str], typing.Any]
SetIntStr = typing.Set[typing.Union[int, str]]

MethodHTTPT = typing.TypeVar(
    "MethodHTTPT",
    bound=typing.Callable[
        [
            str,
            typing.Any,
            typing.Optional[int],
            typing.Optional[typing.List[typing.Union[str, typing.Any]]],
            typing.Optional[str],
            str,
            typing.Optional[typing.Dict[typing.Union[int, str], typing.Dict[str, typing.Any]]],
            typing.Optional[bool],
            typing.Optional[str],
            typing.Optional[typing.Union[SetIntStr, DictIntStrAny]],
            typing.Optional[typing.Union[SetIntStr, DictIntStrAny]],
            bool,
            bool,
            bool,
            bool,
            bool,
            typing.Type[Response],
            typing.Optional[str],
            typing.Optional[typing.List[BaseRoute]],
            typing.Optional[typing.Dict[str, typing.Any]],
            typing.Callable[[APIRoute], str],
        ],
        typing.Callable[[typing.Any], typing.Any],
    ],
)
