from __future__ import annotations

import typing

_T = typing.TypeVar("_T")


class SupportsGetItem(typing.Protocol[_T]):
    def __getitem__(self, item: typing.Any) -> _T:
        ...


def update_forward_refs(
    _globals: SupportsGetItem[typing.Any], __all__: typing.Iterable[str]
) -> None:
    for _entity_name in __all__:
        _entity = _globals[_entity_name]
        if not hasattr(_entity, "update_forward_refs"):
            continue
        _entity.update_forward_refs(
            **{k: v for k, v in globals().items() if k in __all__},
            **{"Optional": typing.Optional},
        )
