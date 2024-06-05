import contextlib
import typing

from . import xbpy

class FxStateAccessor:
    def __init__(self, context: xbpy.Context) -> None: pass

    @property
    def context(self) -> xbpy.Context: pass

    @classmethod
    def from_current_context(cls, context: xbpy.Context) -> typing.Self: pass

    @contextlib.contextmanager
    def with_override(self, **kwargs) -> typing.ContextManager[typing.Self]: pass
