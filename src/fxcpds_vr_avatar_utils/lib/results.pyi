import typing

R = typing.TypeVar('R')
E = typing.TypeVar('E')

class Result(typing.Generic[R, E]):
    is_result: bool
    is_error: bool
    value: R
    error: E

    @classmethod
    def of_error(cls, error: E) -> 'Result[R, E]': pass

    @classmethod
    def of_value(cls, value: R) -> 'Result[R, E]': pass
