from .... import properties

class SyncPropertyGroup(properties.EphemeralProperties):
    ignore_muted: bool
    ignore_locked: bool
    skp_only_from_selected: bool
    skp_only_to_selected: bool
