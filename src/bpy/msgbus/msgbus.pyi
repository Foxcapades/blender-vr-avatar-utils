import typing


# noinspection PyUnusedLocal
def clear_by_owner(owner: typing.Any) -> None: pass


# noinspection PyUnusedLocal
def publish_rna(key: typing.Any) -> None: pass


# noinspection PyUnusedLocal,PyDefaultArgument
def subscribe_rna(
    key: typing.Any,
    owner: typing.Any, args: tuple[typing.Any, ...] | tuple[()] | None,
    notify: typing.Callable,
    options: set[typing.Literal['PERSISTENT']] = set(),
) -> None: pass
