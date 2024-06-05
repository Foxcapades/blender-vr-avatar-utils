from typing import Any, Callable, Generic, TypeVar

CT = TypeVar('CT')
VT = TypeVar('VT')


class classproperty(Generic[CT, VT]):
    def __init__(self, getter: Callable[[type[CT]], VT]) -> None:
        self.__getter = getter
        self.__name = ''

    def __get__(self, _: CT, owner: type[CT] = None) -> VT:
        return self.__getter(owner)

    def __set__(self, instance: CT, value: VT) -> None:
        raise AttributeError('cannot update this attribute')

    def __delete__(self, _: CT) -> None:
        raise AttributeError('cannot delete this attribute')

    def __set_name__(self, _: Any, name: str) -> None:
        self.__name = name

    @property
    def __wrapped__(self) -> Callable[[type[CT]], VT]:
        return self.__getter

    @property
    def __func__(self) -> Callable[[type[CT]], VT]:
        return self.__getter

    @property
    def __isabstractmethod__(self) -> bool:
        if hasattr(self.__getter, '__isabstractmethod__'):
            return self.__getter.__isabstractmethod__
        else:
            return False
