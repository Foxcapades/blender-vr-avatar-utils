from contextlib import contextmanager
from typing import ContextManager, Self

from .xbpy import Context


class FxStateAccessor:
    def __init__(self, context: Context) -> None:
        self.__context = context

    @property
    def context(self) -> Context:
        return self.__context

    @classmethod
    def from_current_context(cls, context: Context) -> Self:
        return cls(context)

    @contextmanager
    def with_override(self, **kwargs) -> ContextManager[Self]:
        with self.context.temp_override(**kwargs) as ctx:
            yield self.from_current_context(ctx)
