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
import winrt.windows.phone.personalinformation as windows_phone_personalinformation
import winrt.windows.storage.streams as windows_storage_streams

Self = typing.TypeVar('Self')

@typing.final
class ContactPartnerProvisioningManager_Static(type):
    def associate_network_account_async(cls, store: typing.Optional[windows_phone_personalinformation.ContactStore], network_name: str, network_account_id: str, /) -> windows_foundation.IAsyncAction: ...
    def associate_social_network_account_async(cls, store: typing.Optional[windows_phone_personalinformation.ContactStore], network_name: str, network_account_id: str, /) -> windows_foundation.IAsyncAction: ...
    def import_vcard_to_system_async(cls, stream: typing.Optional[windows_storage_streams.IInputStream], /) -> windows_foundation.IAsyncAction: ...

@typing.final
class ContactPartnerProvisioningManager(winrt.system.Object, metaclass=ContactPartnerProvisioningManager_Static):
    pass

@typing.final
class MessagePartnerProvisioningManager_Static(type):
    def import_mms_to_system_async(cls, incoming: bool, read: bool, subject: str, sender: str, recipients: windows_foundation_collections.IVectorView[str], delivery_time: datetime.datetime, attachments: windows_foundation_collections.IVectorView[windows_foundation_collections.IMapView[str, winrt.system.Object]], /) -> windows_foundation.IAsyncAction: ...
    def import_sms_to_system_async(cls, incoming: bool, read: bool, body: str, sender: str, recipients: windows_foundation_collections.IVectorView[str], delivery_time: datetime.datetime, /) -> windows_foundation.IAsyncAction: ...

@typing.final
class MessagePartnerProvisioningManager(winrt.system.Object, metaclass=MessagePartnerProvisioningManager_Static):
    pass

