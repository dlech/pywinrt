# WARNING: Please don't edit this file. It was generated by Python/WinRT v0.0.0

import enum

import winrt.system
from winrt import _winrt_windows_applicationmodel_datatransfer_dragdrop

__all__ = [
    "DragDropModifiers",
]

class DragDropModifiers(enum.IntFlag):
    NONE = 0x0
    SHIFT = 0x1
    CONTROL = 0x2
    ALT = 0x4
    LEFT_BUTTON = 0x8
    MIDDLE_BUTTON = 0x10
    RIGHT_BUTTON = 0x20

