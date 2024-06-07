from .... import properties

class RenamePropertyGroup(properties.ephemeral.EphemeralProperties):
    rename_from: str
    rename_to: str
