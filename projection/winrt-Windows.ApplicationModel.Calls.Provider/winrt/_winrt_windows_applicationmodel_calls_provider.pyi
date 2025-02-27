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
import winrt.windows.storage as windows_storage

Self = typing.TypeVar('Self')

@typing.final
class PhoneCallOrigin(winrt.system.Object):
    @staticmethod
    def _from(obj: winrt.system.Object, /) -> PhoneCallOrigin: ...
    def __new__(cls: typing.Type[PhoneCallOrigin]) -> PhoneCallOrigin: ...
    @_property
    def location(self) -> str: ...
    @location.setter
    def location(self, value: str) -> None: ...
    @_property
    def category_description(self) -> str: ...
    @category_description.setter
    def category_description(self, value: str) -> None: ...
    @_property
    def category(self) -> str: ...
    @category.setter
    def category(self, value: str) -> None: ...
    @_property
    def display_name(self) -> str: ...
    @display_name.setter
    def display_name(self, value: str) -> None: ...
    @_property
    def display_picture(self) -> typing.Optional[windows_storage.StorageFile]: ...
    @display_picture.setter
    def display_picture(self, value: typing.Optional[windows_storage.StorageFile]) -> None: ...

@typing.final
class PhoneCallOriginManager_Static(type):
    def request_set_as_active_call_origin_app_async(cls) -> windows_foundation.IAsyncOperation[bool]: ...
    def set_call_origin(cls, request_id: _uuid.UUID, call_origin: typing.Optional[PhoneCallOrigin], /) -> None: ...
    def show_phone_call_origin_settings_u_i(cls) -> None: ...
    @_property
    def is_current_app_active_call_origin_app(cls) -> bool: ...
    @_property
    def is_supported(cls) -> bool: ...

@typing.final
class PhoneCallOriginManager(winrt.system.Object, metaclass=PhoneCallOriginManager_Static):
    pass

