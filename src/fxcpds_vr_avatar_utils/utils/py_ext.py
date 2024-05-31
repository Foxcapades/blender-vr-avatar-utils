from typing import Any, Callable, Generic, Type, TypeVar

R = TypeVar('R')


class StaticProperty(Generic[R]):
    def __init__(self, getter: Callable[[], R]) -> None:
        self.__getter = getter

    def __get__(self, instance: Any, owner: Type) -> R:
        return self.__getter()

    @staticmethod
    def __call__(self, fn: Callable[[], R]) -> 'StaticProperty[R]':
        return StaticProperty(fn)
