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
import winrt.windows.system.threading as windows_system_threading

from winrt.windows.system.threading.core import SignalHandler

Self = typing.TypeVar('Self')

@typing.final
class PreallocatedWorkItem(winrt.system.Object):
    @staticmethod
    def _from(obj: winrt.system.Object, /) -> PreallocatedWorkItem: ...
    @typing.overload
    def __new__(cls: typing.Type[PreallocatedWorkItem], handler: typing.Optional[windows_system_threading.WorkItemHandler]) -> PreallocatedWorkItem: ...
    @typing.overload
    def __new__(cls: typing.Type[PreallocatedWorkItem], handler: typing.Optional[windows_system_threading.WorkItemHandler], priority: windows_system_threading.WorkItemPriority) -> PreallocatedWorkItem: ...
    @typing.overload
    def __new__(cls: typing.Type[PreallocatedWorkItem], handler: typing.Optional[windows_system_threading.WorkItemHandler], priority: windows_system_threading.WorkItemPriority, options: windows_system_threading.WorkItemOptions) -> PreallocatedWorkItem: ...
    def run_async(self) -> windows_foundation.IAsyncAction: ...

@typing.final
class SignalNotifier_Static(type):
    @typing.overload
    def attach_to_event(cls, name: str, handler: typing.Optional[SignalHandler], /) -> typing.Optional[SignalNotifier]: ...
    @typing.overload
    def attach_to_event(cls, name: str, handler: typing.Optional[SignalHandler], timeout: datetime.timedelta, /) -> typing.Optional[SignalNotifier]: ...
    @typing.overload
    def attach_to_semaphore(cls, name: str, handler: typing.Optional[SignalHandler], /) -> typing.Optional[SignalNotifier]: ...
    @typing.overload
    def attach_to_semaphore(cls, name: str, handler: typing.Optional[SignalHandler], timeout: datetime.timedelta, /) -> typing.Optional[SignalNotifier]: ...

@typing.final
class SignalNotifier(winrt.system.Object, metaclass=SignalNotifier_Static):
    @staticmethod
    def _from(obj: winrt.system.Object, /) -> SignalNotifier: ...
    def enable(self) -> None: ...
    def terminate(self) -> None: ...

