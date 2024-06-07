from . import ephemeral


def register() -> None:
    ephemeral.EphemeralPropertyContainer.register_class()


def unregister() -> None:
    ephemeral.EphemeralPropertyContainer.unregister_class()
