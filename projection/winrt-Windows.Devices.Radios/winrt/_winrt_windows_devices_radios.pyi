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
import winrt.windows.foundation.collections as windows_foundation_collections

from winrt.windows.devices.radios import RadioAccessStatus, RadioKind, RadioState

Self = typing.TypeVar('Self')

@typing.final
class Radio_Static(type):
    def from_id_async(cls, device_id: str, /) -> windows_foundation.IAsyncOperation[Radio]: ...
    def get_device_selector(cls) -> str: ...
    def get_radios_async(cls) -> windows_foundation.IAsyncOperation[windows_foundation_collections.IVectorView[Radio]]: ...
    def request_access_async(cls) -> windows_foundation.IAsyncOperation[RadioAccessStatus]: ...

@typing.final
class Radio(winrt.system.Object, metaclass=Radio_Static):
    @staticmethod
    def _from(obj: winrt.system.Object, /) -> Radio: ...
    def set_state_async(self, value: RadioState, /) -> windows_foundation.IAsyncOperation[RadioAccessStatus]: ...
    def add_state_changed(self, handler: windows_foundation.TypedEventHandler[Radio, winrt.system.Object], /) -> windows_foundation.EventRegistrationToken: ...
    def remove_state_changed(self, event_cookie: windows_foundation.EventRegistrationToken, /) -> None: ...
    @_property
    def kind(self) -> RadioKind: ...
    @_property
    def name(self) -> str: ...
    @_property
    def state(self) -> RadioState: ...

