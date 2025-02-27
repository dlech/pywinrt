# WARNING: Please don't edit this file. It was generated by Python/WinRT v0.0.0

import datetime
import sys
import types
import typing
import uuid as _uuid
from builtins import property as _property

import winrt._winrt
import winrt.system
import winrt.windows.devices.geolocation as windows_devices_geolocation
import winrt.windows.foundation as windows_foundation

from winrt.windows.devices.geolocation.provider import LocationOverrideStatus

Self = typing.TypeVar('Self')

@typing.final
class GeolocationProvider(winrt.system.Object):
    @staticmethod
    def _from(obj: winrt.system.Object, /) -> GeolocationProvider: ...
    def __new__(cls: typing.Type[GeolocationProvider]) -> GeolocationProvider: ...
    def clear_override_position(self) -> None: ...
    def set_override_position(self, new_position: windows_devices_geolocation.BasicGeoposition, position_source: windows_devices_geolocation.PositionSource, accuracy_in_meters: winrt.system.Double, /) -> LocationOverrideStatus: ...
    def add_is_overridden_changed(self, handler: windows_foundation.EventHandler[winrt.system.Object], /) -> windows_foundation.EventRegistrationToken: ...
    def remove_is_overridden_changed(self, token: windows_foundation.EventRegistrationToken, /) -> None: ...
    @_property
    def is_overridden(self) -> bool: ...

