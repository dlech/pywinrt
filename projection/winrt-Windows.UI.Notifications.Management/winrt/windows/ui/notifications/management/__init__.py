# WARNING: Please don't edit this file. It was generated by Python/WinRT v0.0.0

import enum

import winrt.system
from winrt import _winrt_windows_ui_notifications_management

__all__ = [
    "UserNotificationListenerAccessStatus",
    "UserNotificationListener",
]

class UserNotificationListenerAccessStatus(enum.IntEnum):
    UNSPECIFIED = 0
    ALLOWED = 1
    DENIED = 2

UserNotificationListener = _winrt_windows_ui_notifications_management.UserNotificationListener
