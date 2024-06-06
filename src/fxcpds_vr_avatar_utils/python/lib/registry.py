import abc


class Registrable(abc.ABC):
    @classmethod
    @abc.abstractmethod
    def register(cls) -> None: pass

    @classmethod
    @abc.abstractmethod
    def unregister(cls) -> None: pass
