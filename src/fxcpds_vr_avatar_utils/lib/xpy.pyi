import typing

CT = typing.TypeVar('CT')
VT = typing.TypeVar('VT')

class classproperty(typing.Generic[CT, VT]):
    def __init__(self, getter: typing.Callable[[type[CT]], VT]) -> None: pass
