# WARNING: Please don't edit this file. It was generated by Python/WinRT v0.0.0

import datetime
import sys
import types
import typing
import uuid as _uuid
from builtins import property as _property

import winrt._winrt
import winrt.system
import winrt.windows.applicationmodel.appointments as windows_applicationmodel_appointments
import winrt.windows.applicationmodel.contacts as windows_applicationmodel_contacts
import winrt.windows.applicationmodel.email as windows_applicationmodel_email
import winrt.windows.applicationmodel.userdatatasks as windows_applicationmodel_userdatatasks
import winrt.windows.foundation as windows_foundation
import winrt.windows.foundation.collections as windows_foundation_collections
import winrt.windows.storage.streams as windows_storage_streams
import winrt.windows.system as windows_system

from winrt.windows.applicationmodel.userdataaccounts import UserDataAccountContentKinds, UserDataAccountOtherAppReadAccess, UserDataAccountStoreAccessType

Self = typing.TypeVar('Self')

@typing.final
class UserDataAccount(winrt.system.Object):
    @staticmethod
    def _from(obj: winrt.system.Object, /) -> UserDataAccount: ...
    def delete_async(self) -> windows_foundation.IAsyncAction: ...
    def find_appointment_calendars_async(self) -> windows_foundation.IAsyncOperation[windows_foundation_collections.IVectorView[windows_applicationmodel_appointments.AppointmentCalendar]]: ...
    def find_contact_annotation_lists_async(self) -> windows_foundation.IAsyncOperation[windows_foundation_collections.IVectorView[windows_applicationmodel_contacts.ContactAnnotationList]]: ...
    def find_contact_groups_async(self) -> windows_foundation.IAsyncOperation[windows_foundation_collections.IVectorView[windows_applicationmodel_contacts.ContactGroup]]: ...
    def find_contact_lists_async(self) -> windows_foundation.IAsyncOperation[windows_foundation_collections.IVectorView[windows_applicationmodel_contacts.ContactList]]: ...
    def find_email_mailboxes_async(self) -> windows_foundation.IAsyncOperation[windows_foundation_collections.IVectorView[windows_applicationmodel_email.EmailMailbox]]: ...
    def find_user_data_task_lists_async(self) -> windows_foundation.IAsyncOperation[windows_foundation_collections.IVectorView[windows_applicationmodel_userdatatasks.UserDataTaskList]]: ...
    def save_async(self) -> windows_foundation.IAsyncAction: ...
    def try_show_create_contact_group_async(self) -> windows_foundation.IAsyncOperation[str]: ...
    @_property
    def user_display_name(self) -> str: ...
    @user_display_name.setter
    def user_display_name(self, value: str) -> None: ...
    @_property
    def other_app_read_access(self) -> UserDataAccountOtherAppReadAccess: ...
    @other_app_read_access.setter
    def other_app_read_access(self, value: UserDataAccountOtherAppReadAccess) -> None: ...
    @_property
    def icon(self) -> typing.Optional[windows_storage_streams.IRandomAccessStreamReference]: ...
    @icon.setter
    def icon(self, value: typing.Optional[windows_storage_streams.IRandomAccessStreamReference]) -> None: ...
    @_property
    def device_account_type_id(self) -> str: ...
    @_property
    def id(self) -> str: ...
    @_property
    def package_family_name(self) -> str: ...
    @_property
    def is_protected_under_lock(self) -> bool: ...
    @is_protected_under_lock.setter
    def is_protected_under_lock(self, value: bool) -> None: ...
    @_property
    def enterprise_id(self) -> str: ...
    @_property
    def display_name(self) -> str: ...
    @display_name.setter
    def display_name(self, value: str) -> None: ...
    @_property
    def explict_read_access_package_family_names(self) -> typing.Optional[windows_foundation_collections.IVector[str]]: ...
    @_property
    def can_show_create_contact_group(self) -> bool: ...
    @can_show_create_contact_group.setter
    def can_show_create_contact_group(self, value: bool) -> None: ...
    @_property
    def provider_properties(self) -> typing.Optional[windows_foundation_collections.IPropertySet]: ...

@typing.final
class UserDataAccountManager_Static(type):
    def get_for_user(cls, user: typing.Optional[windows_system.User], /) -> typing.Optional[UserDataAccountManagerForUser]: ...
    def request_store_async(cls, store_access_type: UserDataAccountStoreAccessType, /) -> windows_foundation.IAsyncOperation[UserDataAccountStore]: ...
    def show_account_error_resolver_async(cls, id: str, /) -> windows_foundation.IAsyncAction: ...
    def show_account_settings_async(cls, id: str, /) -> windows_foundation.IAsyncAction: ...
    def show_add_account_async(cls, content_kinds: UserDataAccountContentKinds, /) -> windows_foundation.IAsyncOperation[str]: ...

@typing.final
class UserDataAccountManager(winrt.system.Object, metaclass=UserDataAccountManager_Static):
    pass

@typing.final
class UserDataAccountManagerForUser(winrt.system.Object):
    @staticmethod
    def _from(obj: winrt.system.Object, /) -> UserDataAccountManagerForUser: ...
    def request_store_async(self, store_access_type: UserDataAccountStoreAccessType, /) -> windows_foundation.IAsyncOperation[UserDataAccountStore]: ...
    @_property
    def user(self) -> typing.Optional[windows_system.User]: ...

@typing.final
class UserDataAccountStore(winrt.system.Object):
    @staticmethod
    def _from(obj: winrt.system.Object, /) -> UserDataAccountStore: ...
    @typing.overload
    def create_account_async(self, user_display_name: str, /) -> windows_foundation.IAsyncOperation[UserDataAccount]: ...
    @typing.overload
    def create_account_async(self, user_display_name: str, package_relative_app_id: str, /) -> windows_foundation.IAsyncOperation[UserDataAccount]: ...
    @typing.overload
    def create_account_async(self, user_display_name: str, package_relative_app_id: str, enterprise_id: str, /) -> windows_foundation.IAsyncOperation[UserDataAccount]: ...
    def find_accounts_async(self) -> windows_foundation.IAsyncOperation[windows_foundation_collections.IVectorView[UserDataAccount]]: ...
    def get_account_async(self, id: str, /) -> windows_foundation.IAsyncOperation[UserDataAccount]: ...
    def add_store_changed(self, handler: windows_foundation.TypedEventHandler[UserDataAccountStore, UserDataAccountStoreChangedEventArgs], /) -> windows_foundation.EventRegistrationToken: ...
    def remove_store_changed(self, token: windows_foundation.EventRegistrationToken, /) -> None: ...

@typing.final
class UserDataAccountStoreChangedEventArgs(winrt.system.Object):
    @staticmethod
    def _from(obj: winrt.system.Object, /) -> UserDataAccountStoreChangedEventArgs: ...
    def get_deferral(self) -> typing.Optional[windows_foundation.Deferral]: ...

