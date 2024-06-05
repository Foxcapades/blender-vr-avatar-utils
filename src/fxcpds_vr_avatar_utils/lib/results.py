import typing

R = typing.TypeVar('R')
E = typing.TypeVar('E')


class Result(typing.Generic[R, E]):
    def __init__(self, value: R | None, error: E | None, is_value: bool) -> None:
        self.__value = value
        self.__error = error
        self.__is_value = is_value

    @property
    def is_result(self) -> bool:
        return self.__is_value

    @property
    def is_error(self) -> bool:
        return not self.__is_value

    @property
    def value(self) -> R:
        if self.__is_value:
            return self.__value
        else:
            raise Exception('attempted to unwrap the value of an error result')

    @property
    def error(self) -> E:
        if self.__is_value:
            raise Exception('attempted to unwrap the error of a success result')
        else:
            return self.__error

    @classmethod
    def of_error(cls, error: E) -> 'Result[R, E]':
        return cls(None, error, False)

    @classmethod
    def of_value(cls, value: R) -> 'Result[R, E]':
        return cls(value, None, True)

