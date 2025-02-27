# WARNING: Please don't edit this file. It was generated by Python/WinRT v0.0.0

import datetime
import sys
import types
import typing
import uuid as _uuid
from builtins import property as _property

import winrt._winrt
import winrt.system
import winrt.windows.foundation as windows_foundation

from winrt.windows.applicationmodel.extendedexecution.foreground import ExtendedExecutionForegroundReason, ExtendedExecutionForegroundResult, ExtendedExecutionForegroundRevokedReason

Self = typing.TypeVar('Self')

@typing.final
class ExtendedExecutionForegroundRevokedEventArgs(winrt.system.Object):
    @staticmethod
    def _from(obj: winrt.system.Object, /) -> ExtendedExecutionForegroundRevokedEventArgs: ...
    @_property
    def reason(self) -> ExtendedExecutionForegroundRevokedReason: ...

@typing.final
class ExtendedExecutionForegroundSession(winrt.system.Object):
    def __enter__(self: Self) -> Self: ...
    def __exit__(self, *args) -> None: ...
    @staticmethod
    def _from(obj: winrt.system.Object, /) -> ExtendedExecutionForegroundSession: ...
    def __new__(cls: typing.Type[ExtendedExecutionForegroundSession]) -> ExtendedExecutionForegroundSession: ...
    def close(self) -> None: ...
    def request_extension_async(self) -> windows_foundation.IAsyncOperation[ExtendedExecutionForegroundResult]: ...
    def add_revoked(self, handler: windows_foundation.TypedEventHandler[winrt.system.Object, ExtendedExecutionForegroundRevokedEventArgs], /) -> windows_foundation.EventRegistrationToken: ...
    def remove_revoked(self, token: windows_foundation.EventRegistrationToken, /) -> None: ...
    @_property
    def reason(self) -> ExtendedExecutionForegroundReason: ...
    @reason.setter
    def reason(self, value: ExtendedExecutionForegroundReason) -> None: ...
    @_property
    def description(self) -> str: ...
    @description.setter
    def description(self, value: str) -> None: ...

