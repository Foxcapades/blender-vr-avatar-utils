"""
Defines aliases for types that exist in the bpy reference library but do not
exist in the real bpy library such as enum literals or union types.
"""

try:
    from bpy.types import i, o, w
    from bpy import AnyContext

    Context = AnyContext
    Icon = i.Icon
    OperatorReturn = o.OperatorReturn
    WmReportType = w.WmReportType
except Exception:
    import bpy

    Context = type(bpy.context)
    Icon = str
    OperatorReturn = str
    WmReportType = str
