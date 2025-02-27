# WARNING: Please don't edit this file. It was generated by Python/WinRT v0.0.0

import datetime
import sys
import types
import typing
import uuid as _uuid
from builtins import property as _property

import winrt._winrt
import winrt.system
import winrt.windows.applicationmodel.wallet as windows_applicationmodel_wallet
import winrt.windows.foundation as windows_foundation
import winrt.windows.foundation.collections as windows_foundation_collections
import winrt.windows.storage.streams as windows_storage_streams

from winrt.windows.applicationmodel.wallet.system import WalletItemAppAssociation

Self = typing.TypeVar('Self')

@typing.final
class WalletItemSystemStore(winrt.system.Object):
    @staticmethod
    def _from(obj: winrt.system.Object, /) -> WalletItemSystemStore: ...
    def delete_async(self, item: typing.Optional[windows_applicationmodel_wallet.WalletItem], /) -> windows_foundation.IAsyncAction: ...
    def get_app_status_for_item(self, item: typing.Optional[windows_applicationmodel_wallet.WalletItem], /) -> WalletItemAppAssociation: ...
    def get_items_async(self) -> windows_foundation.IAsyncOperation[windows_foundation_collections.IVectorView[windows_applicationmodel_wallet.WalletItem]]: ...
    def import_item_async(self, stream: typing.Optional[windows_storage_streams.IRandomAccessStreamReference], /) -> windows_foundation.IAsyncOperation[windows_applicationmodel_wallet.WalletItem]: ...
    def launch_app_for_item_async(self, item: typing.Optional[windows_applicationmodel_wallet.WalletItem], /) -> windows_foundation.IAsyncOperation[bool]: ...
    def add_items_changed(self, handler: windows_foundation.TypedEventHandler[WalletItemSystemStore, winrt.system.Object], /) -> windows_foundation.EventRegistrationToken: ...
    def remove_items_changed(self, cookie: windows_foundation.EventRegistrationToken, /) -> None: ...

@typing.final
class WalletManagerSystem_Static(type):
    def request_store_async(cls) -> windows_foundation.IAsyncOperation[WalletItemSystemStore]: ...

@typing.final
class WalletManagerSystem(winrt.system.Object, metaclass=WalletManagerSystem_Static):
    pass

