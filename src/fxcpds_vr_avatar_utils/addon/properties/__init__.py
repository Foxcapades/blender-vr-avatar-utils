from .ephemeral import EphemeralProperties, EphemeralPropertyContainer
del ephemeral


def register():
    EphemeralPropertyContainer.register()


def unregister():
    EphemeralPropertyContainer.unregister()
