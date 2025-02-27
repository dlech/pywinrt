# WARNING: Please don't edit this file. It was generated by Python/WinRT v0.0.0

import datetime
import sys
import types
import typing
import uuid as _uuid
from builtins import property as _property

import winrt._winrt
import winrt.system
import winrt.windows.applicationmodel as windows_applicationmodel
import winrt.windows.foundation as windows_foundation
import winrt.windows.foundation.collections as windows_foundation_collections
import winrt.windows.system as windows_system
import winrt.windows.system.remotesystems as windows_system_remotesystems

from winrt.windows.applicationmodel.appservice import AppServiceClosedStatus, AppServiceConnectionStatus, AppServiceResponseStatus, StatelessAppServiceResponseStatus

Self = typing.TypeVar('Self')

@typing.final
class AppServiceCatalog_Static(type):
    def find_app_service_providers_async(cls, app_service_name: str, /) -> windows_foundation.IAsyncOperation[windows_foundation_collections.IVectorView[windows_applicationmodel.AppInfo]]: ...

@typing.final
class AppServiceCatalog(winrt.system.Object, metaclass=AppServiceCatalog_Static):
    pass

@typing.final
class AppServiceClosedEventArgs(winrt.system.Object):
    @staticmethod
    def _from(obj: winrt.system.Object, /) -> AppServiceClosedEventArgs: ...
    @_property
    def status(self) -> AppServiceClosedStatus: ...

@typing.final
class AppServiceConnection_Static(type):
    def send_stateless_message_async(cls, connection: typing.Optional[AppServiceConnection], connection_request: typing.Optional[windows_system_remotesystems.RemoteSystemConnectionRequest], message: typing.Optional[windows_foundation_collections.ValueSet], /) -> windows_foundation.IAsyncOperation[StatelessAppServiceResponse]: ...

@typing.final
class AppServiceConnection(winrt.system.Object, metaclass=AppServiceConnection_Static):
    def __enter__(self: Self) -> Self: ...
    def __exit__(self, *args) -> None: ...
    @staticmethod
    def _from(obj: winrt.system.Object, /) -> AppServiceConnection: ...
    def __new__(cls: typing.Type[AppServiceConnection]) -> AppServiceConnection: ...
    def close(self) -> None: ...
    def open_async(self) -> windows_foundation.IAsyncOperation[AppServiceConnectionStatus]: ...
    def open_remote_async(self, remote_system_connection_request: typing.Optional[windows_system_remotesystems.RemoteSystemConnectionRequest], /) -> windows_foundation.IAsyncOperation[AppServiceConnectionStatus]: ...
    def send_message_async(self, message: typing.Optional[windows_foundation_collections.ValueSet], /) -> windows_foundation.IAsyncOperation[AppServiceResponse]: ...
    def add_request_received(self, handler: windows_foundation.TypedEventHandler[AppServiceConnection, AppServiceRequestReceivedEventArgs], /) -> windows_foundation.EventRegistrationToken: ...
    def remove_request_received(self, token: windows_foundation.EventRegistrationToken, /) -> None: ...
    def add_service_closed(self, handler: windows_foundation.TypedEventHandler[AppServiceConnection, AppServiceClosedEventArgs], /) -> windows_foundation.EventRegistrationToken: ...
    def remove_service_closed(self, token: windows_foundation.EventRegistrationToken, /) -> None: ...
    @_property
    def package_family_name(self) -> str: ...
    @package_family_name.setter
    def package_family_name(self, value: str) -> None: ...
    @_property
    def app_service_name(self) -> str: ...
    @app_service_name.setter
    def app_service_name(self, value: str) -> None: ...
    @_property
    def user(self) -> typing.Optional[windows_system.User]: ...
    @user.setter
    def user(self, value: typing.Optional[windows_system.User]) -> None: ...

@typing.final
class AppServiceDeferral(winrt.system.Object):
    @staticmethod
    def _from(obj: winrt.system.Object, /) -> AppServiceDeferral: ...
    def complete(self) -> None: ...

@typing.final
class AppServiceRequest(winrt.system.Object):
    @staticmethod
    def _from(obj: winrt.system.Object, /) -> AppServiceRequest: ...
    def send_response_async(self, message: typing.Optional[windows_foundation_collections.ValueSet], /) -> windows_foundation.IAsyncOperation[AppServiceResponseStatus]: ...
    @_property
    def message(self) -> typing.Optional[windows_foundation_collections.ValueSet]: ...

@typing.final
class AppServiceRequestReceivedEventArgs(winrt.system.Object):
    @staticmethod
    def _from(obj: winrt.system.Object, /) -> AppServiceRequestReceivedEventArgs: ...
    def get_deferral(self) -> typing.Optional[AppServiceDeferral]: ...
    @_property
    def request(self) -> typing.Optional[AppServiceRequest]: ...

@typing.final
class AppServiceResponse(winrt.system.Object):
    @staticmethod
    def _from(obj: winrt.system.Object, /) -> AppServiceResponse: ...
    @_property
    def message(self) -> typing.Optional[windows_foundation_collections.ValueSet]: ...
    @_property
    def status(self) -> AppServiceResponseStatus: ...

@typing.final
class AppServiceTriggerDetails(winrt.system.Object):
    @staticmethod
    def _from(obj: winrt.system.Object, /) -> AppServiceTriggerDetails: ...
    def check_caller_for_capability_async(self, capability_name: str, /) -> windows_foundation.IAsyncOperation[bool]: ...
    @_property
    def app_service_connection(self) -> typing.Optional[AppServiceConnection]: ...
    @_property
    def caller_package_family_name(self) -> str: ...
    @_property
    def name(self) -> str: ...
    @_property
    def is_remote_system_connection(self) -> bool: ...
    @_property
    def caller_remote_connection_token(self) -> str: ...

@typing.final
class StatelessAppServiceResponse(winrt.system.Object):
    @staticmethod
    def _from(obj: winrt.system.Object, /) -> StatelessAppServiceResponse: ...
    @_property
    def message(self) -> typing.Optional[windows_foundation_collections.ValueSet]: ...
    @_property
    def status(self) -> StatelessAppServiceResponseStatus: ...

