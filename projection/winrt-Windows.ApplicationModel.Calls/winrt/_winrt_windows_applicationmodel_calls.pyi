# WARNING: Please don't edit this file. It was generated by Python/WinRT v0.0.0

import datetime
import sys
import types
import typing
import uuid as _uuid
from builtins import property as _property

import winrt._winrt
import winrt.system
import winrt.windows.applicationmodel.contacts as windows_applicationmodel_contacts
import winrt.windows.devices.enumeration as windows_devices_enumeration
import winrt.windows.foundation as windows_foundation
import winrt.windows.foundation.collections as windows_foundation_collections
import winrt.windows.system as windows_system
import winrt.windows.ui as windows_ui

from winrt.windows.applicationmodel.calls import CellularDtmfMode, DtmfKey, DtmfToneAudioPlayback, PhoneAudioRoutingEndpoint, PhoneCallAudioDevice, PhoneCallDirection, PhoneCallHistoryEntryMedia, PhoneCallHistoryEntryOtherAppReadAccess, PhoneCallHistoryEntryQueryDesiredMedia, PhoneCallHistoryEntryRawAddressKind, PhoneCallHistorySourceIdKind, PhoneCallHistoryStoreAccessType, PhoneCallMedia, PhoneCallOperationStatus, PhoneCallStatus, PhoneLineNetworkOperatorDisplayTextLocation, PhoneLineOperationStatus, PhoneLineTransport, PhoneLineWatcherStatus, PhoneNetworkState, PhoneSimState, PhoneVoicemailType, TransportDeviceAudioRoutingStatus, VoipCallControlDeviceKind, VoipPhoneCallMedia, VoipPhoneCallRejectReason, VoipPhoneCallResourceReservationStatus, VoipPhoneCallState

Self = typing.TypeVar('Self')

@typing.final
class AcceptedVoipPhoneCallOptions(winrt.system.Object):
    @staticmethod
    def _from(obj: winrt.system.Object, /) -> AcceptedVoipPhoneCallOptions: ...
    @typing.overload
    def __new__(cls: typing.Type[AcceptedVoipPhoneCallOptions], associated_device_ids: typing.Iterable[str]) -> AcceptedVoipPhoneCallOptions: ...
    @typing.overload
    def __new__(cls: typing.Type[AcceptedVoipPhoneCallOptions]) -> AcceptedVoipPhoneCallOptions: ...
    @_property
    def service_name(self) -> str: ...
    @service_name.setter
    def service_name(self, value: str) -> None: ...
    @_property
    def media(self) -> VoipPhoneCallMedia: ...
    @media.setter
    def media(self, value: VoipPhoneCallMedia) -> None: ...
    @_property
    def context(self) -> str: ...
    @context.setter
    def context(self, value: str) -> None: ...
    @_property
    def contact_number(self) -> str: ...
    @contact_number.setter
    def contact_number(self, value: str) -> None: ...
    @_property
    def contact_name(self) -> str: ...
    @contact_name.setter
    def contact_name(self, value: str) -> None: ...
    @_property
    def associated_device_ids(self) -> typing.Optional[windows_foundation_collections.IVector[str]]: ...

@typing.final
class AppInitiatedVoipPhoneCallOptions(winrt.system.Object):
    @staticmethod
    def _from(obj: winrt.system.Object, /) -> AppInitiatedVoipPhoneCallOptions: ...
    @typing.overload
    def __new__(cls: typing.Type[AppInitiatedVoipPhoneCallOptions], associated_device_ids: typing.Iterable[str]) -> AppInitiatedVoipPhoneCallOptions: ...
    @typing.overload
    def __new__(cls: typing.Type[AppInitiatedVoipPhoneCallOptions]) -> AppInitiatedVoipPhoneCallOptions: ...
    @_property
    def service_name(self) -> str: ...
    @service_name.setter
    def service_name(self, value: str) -> None: ...
    @_property
    def media(self) -> VoipPhoneCallMedia: ...
    @media.setter
    def media(self, value: VoipPhoneCallMedia) -> None: ...
    @_property
    def context(self) -> str: ...
    @context.setter
    def context(self, value: str) -> None: ...
    @_property
    def contact_number(self) -> str: ...
    @contact_number.setter
    def contact_number(self, value: str) -> None: ...
    @_property
    def contact_name(self) -> str: ...
    @contact_name.setter
    def contact_name(self, value: str) -> None: ...
    @_property
    def associated_device_ids(self) -> typing.Optional[windows_foundation_collections.IVector[str]]: ...

@typing.final
class CallAnswerEventArgs(winrt.system.Object):
    @staticmethod
    def _from(obj: winrt.system.Object, /) -> CallAnswerEventArgs: ...
    @_property
    def accepted_media(self) -> VoipPhoneCallMedia: ...
    @_property
    def source_device_id(self) -> str: ...

@typing.final
class CallRejectEventArgs(winrt.system.Object):
    @staticmethod
    def _from(obj: winrt.system.Object, /) -> CallRejectEventArgs: ...
    @_property
    def reject_reason(self) -> VoipPhoneCallRejectReason: ...

@typing.final
class CallStateChangeEventArgs(winrt.system.Object):
    @staticmethod
    def _from(obj: winrt.system.Object, /) -> CallStateChangeEventArgs: ...
    @_property
    def state(self) -> VoipPhoneCallState: ...

@typing.final
class IncomingVoipPhoneCallOptions(winrt.system.Object):
    @staticmethod
    def _from(obj: winrt.system.Object, /) -> IncomingVoipPhoneCallOptions: ...
    @typing.overload
    def __new__(cls: typing.Type[IncomingVoipPhoneCallOptions], associated_device_ids: typing.Iterable[str]) -> IncomingVoipPhoneCallOptions: ...
    @typing.overload
    def __new__(cls: typing.Type[IncomingVoipPhoneCallOptions]) -> IncomingVoipPhoneCallOptions: ...
    @_property
    def service_name(self) -> str: ...
    @service_name.setter
    def service_name(self, value: str) -> None: ...
    @_property
    def ringtone(self) -> typing.Optional[windows_foundation.Uri]: ...
    @ringtone.setter
    def ringtone(self, value: typing.Optional[windows_foundation.Uri]) -> None: ...
    @_property
    def ring_timeout(self) -> datetime.timedelta: ...
    @ring_timeout.setter
    def ring_timeout(self, value: datetime.timedelta) -> None: ...
    @_property
    def media(self) -> VoipPhoneCallMedia: ...
    @media.setter
    def media(self, value: VoipPhoneCallMedia) -> None: ...
    @_property
    def context(self) -> str: ...
    @context.setter
    def context(self, value: str) -> None: ...
    @_property
    def contact_remote_id(self) -> str: ...
    @contact_remote_id.setter
    def contact_remote_id(self, value: str) -> None: ...
    @_property
    def contact_number(self) -> str: ...
    @contact_number.setter
    def contact_number(self, value: str) -> None: ...
    @_property
    def contact_name(self) -> str: ...
    @contact_name.setter
    def contact_name(self, value: str) -> None: ...
    @_property
    def contact_image(self) -> typing.Optional[windows_foundation.Uri]: ...
    @contact_image.setter
    def contact_image(self, value: typing.Optional[windows_foundation.Uri]) -> None: ...
    @_property
    def call_details(self) -> str: ...
    @call_details.setter
    def call_details(self, value: str) -> None: ...
    @_property
    def branding_image(self) -> typing.Optional[windows_foundation.Uri]: ...
    @branding_image.setter
    def branding_image(self, value: typing.Optional[windows_foundation.Uri]) -> None: ...
    @_property
    def associated_device_ids(self) -> typing.Optional[windows_foundation_collections.IVector[str]]: ...

@typing.final
class LockScreenCallEndCallDeferral(winrt.system.Object):
    @staticmethod
    def _from(obj: winrt.system.Object, /) -> LockScreenCallEndCallDeferral: ...
    def complete(self) -> None: ...

@typing.final
class LockScreenCallEndRequestedEventArgs(winrt.system.Object):
    @staticmethod
    def _from(obj: winrt.system.Object, /) -> LockScreenCallEndRequestedEventArgs: ...
    def get_deferral(self) -> typing.Optional[LockScreenCallEndCallDeferral]: ...
    @_property
    def deadline(self) -> datetime.datetime: ...

@typing.final
class LockScreenCallUI(winrt.system.Object):
    @staticmethod
    def _from(obj: winrt.system.Object, /) -> LockScreenCallUI: ...
    def dismiss(self) -> None: ...
    def add_closed(self, handler: windows_foundation.TypedEventHandler[LockScreenCallUI, winrt.system.Object], /) -> windows_foundation.EventRegistrationToken: ...
    def remove_closed(self, token: windows_foundation.EventRegistrationToken, /) -> None: ...
    def add_end_requested(self, handler: windows_foundation.TypedEventHandler[LockScreenCallUI, LockScreenCallEndRequestedEventArgs], /) -> windows_foundation.EventRegistrationToken: ...
    def remove_end_requested(self, token: windows_foundation.EventRegistrationToken, /) -> None: ...
    @_property
    def call_title(self) -> str: ...
    @call_title.setter
    def call_title(self, value: str) -> None: ...

@typing.final
class MuteChangeEventArgs(winrt.system.Object):
    @staticmethod
    def _from(obj: winrt.system.Object, /) -> MuteChangeEventArgs: ...
    @_property
    def muted(self) -> bool: ...

@typing.final
class OutgoingVoipPhoneCallOptions(winrt.system.Object):
    @staticmethod
    def _from(obj: winrt.system.Object, /) -> OutgoingVoipPhoneCallOptions: ...
    @typing.overload
    def __new__(cls: typing.Type[OutgoingVoipPhoneCallOptions], associated_device_ids: typing.Iterable[str]) -> OutgoingVoipPhoneCallOptions: ...
    @typing.overload
    def __new__(cls: typing.Type[OutgoingVoipPhoneCallOptions]) -> OutgoingVoipPhoneCallOptions: ...
    @_property
    def service_name(self) -> str: ...
    @service_name.setter
    def service_name(self, value: str) -> None: ...
    @_property
    def media(self) -> VoipPhoneCallMedia: ...
    @media.setter
    def media(self, value: VoipPhoneCallMedia) -> None: ...
    @_property
    def context(self) -> str: ...
    @context.setter
    def context(self, value: str) -> None: ...
    @_property
    def contact_name(self) -> str: ...
    @contact_name.setter
    def contact_name(self, value: str) -> None: ...
    @_property
    def associated_device_ids(self) -> typing.Optional[windows_foundation_collections.IVector[str]]: ...

@typing.final
class PhoneCall_Static(type):
    def get_from_id(cls, call_id: str, /) -> typing.Optional[PhoneCall]: ...

@typing.final
class PhoneCall(winrt.system.Object, metaclass=PhoneCall_Static):
    @staticmethod
    def _from(obj: winrt.system.Object, /) -> PhoneCall: ...
    def accept_incoming(self) -> PhoneCallOperationStatus: ...
    def accept_incoming_async(self) -> windows_foundation.IAsyncOperation[PhoneCallOperationStatus]: ...
    def change_audio_device(self, endpoint: PhoneCallAudioDevice, /) -> PhoneCallOperationStatus: ...
    def change_audio_device_async(self, endpoint: PhoneCallAudioDevice, /) -> windows_foundation.IAsyncOperation[PhoneCallOperationStatus]: ...
    def end(self) -> PhoneCallOperationStatus: ...
    def end_async(self) -> windows_foundation.IAsyncOperation[PhoneCallOperationStatus]: ...
    def get_phone_call_info(self) -> typing.Optional[PhoneCallInfo]: ...
    def get_phone_call_info_async(self) -> windows_foundation.IAsyncOperation[PhoneCallInfo]: ...
    def hold(self) -> PhoneCallOperationStatus: ...
    def hold_async(self) -> windows_foundation.IAsyncOperation[PhoneCallOperationStatus]: ...
    def mute(self) -> PhoneCallOperationStatus: ...
    def mute_async(self) -> windows_foundation.IAsyncOperation[PhoneCallOperationStatus]: ...
    def reject_incoming(self) -> PhoneCallOperationStatus: ...
    def reject_incoming_async(self) -> windows_foundation.IAsyncOperation[PhoneCallOperationStatus]: ...
    def resume_from_hold(self) -> PhoneCallOperationStatus: ...
    def resume_from_hold_async(self) -> windows_foundation.IAsyncOperation[PhoneCallOperationStatus]: ...
    def send_dtmf_key(self, key: DtmfKey, dtmf_tone_audio_playback: DtmfToneAudioPlayback, /) -> PhoneCallOperationStatus: ...
    def send_dtmf_key_async(self, key: DtmfKey, dtmf_tone_audio_playback: DtmfToneAudioPlayback, /) -> windows_foundation.IAsyncOperation[PhoneCallOperationStatus]: ...
    def unmute(self) -> PhoneCallOperationStatus: ...
    def unmute_async(self) -> windows_foundation.IAsyncOperation[PhoneCallOperationStatus]: ...
    def add_audio_device_changed(self, handler: windows_foundation.TypedEventHandler[PhoneCall, winrt.system.Object], /) -> windows_foundation.EventRegistrationToken: ...
    def remove_audio_device_changed(self, token: windows_foundation.EventRegistrationToken, /) -> None: ...
    def add_is_muted_changed(self, handler: windows_foundation.TypedEventHandler[PhoneCall, winrt.system.Object], /) -> windows_foundation.EventRegistrationToken: ...
    def remove_is_muted_changed(self, token: windows_foundation.EventRegistrationToken, /) -> None: ...
    def add_status_changed(self, handler: windows_foundation.TypedEventHandler[PhoneCall, winrt.system.Object], /) -> windows_foundation.EventRegistrationToken: ...
    def remove_status_changed(self, token: windows_foundation.EventRegistrationToken, /) -> None: ...
    @_property
    def audio_device(self) -> PhoneCallAudioDevice: ...
    @_property
    def call_id(self) -> str: ...
    @_property
    def is_muted(self) -> bool: ...
    @_property
    def status(self) -> PhoneCallStatus: ...

@typing.final
class PhoneCallBlocking_Static(type):
    def set_call_blocking_list_async(cls, phone_number_list: typing.Iterable[str], /) -> windows_foundation.IAsyncOperation[bool]: ...
    @_property
    def block_unknown_numbers(cls) -> bool: ...
    @block_unknown_numbers.setter
    def block_unknown_numbers(cls, value: bool) -> None: ...
    @_property
    def block_private_numbers(cls) -> bool: ...
    @block_private_numbers.setter
    def block_private_numbers(cls, value: bool) -> None: ...

@typing.final
class PhoneCallBlocking(winrt.system.Object, metaclass=PhoneCallBlocking_Static):
    pass

@typing.final
class PhoneCallHistoryEntry(winrt.system.Object):
    @staticmethod
    def _from(obj: winrt.system.Object, /) -> PhoneCallHistoryEntry: ...
    def __new__(cls: typing.Type[PhoneCallHistoryEntry]) -> PhoneCallHistoryEntry: ...
    @_property
    def media(self) -> PhoneCallHistoryEntryMedia: ...
    @media.setter
    def media(self, value: PhoneCallHistoryEntryMedia) -> None: ...
    @_property
    def is_missed(self) -> bool: ...
    @is_missed.setter
    def is_missed(self, value: bool) -> None: ...
    @_property
    def is_incoming(self) -> bool: ...
    @is_incoming.setter
    def is_incoming(self, value: bool) -> None: ...
    @_property
    def is_caller_id_blocked(self) -> bool: ...
    @is_caller_id_blocked.setter
    def is_caller_id_blocked(self, value: bool) -> None: ...
    @_property
    def is_seen(self) -> bool: ...
    @is_seen.setter
    def is_seen(self, value: bool) -> None: ...
    @_property
    def duration(self) -> typing.Optional[typing.Optional[datetime.timedelta]]: ...
    @duration.setter
    def duration(self, value: typing.Optional[typing.Optional[datetime.timedelta]]) -> None: ...
    @_property
    def is_emergency(self) -> bool: ...
    @is_emergency.setter
    def is_emergency(self, value: bool) -> None: ...
    @_property
    def is_suppressed(self) -> bool: ...
    @is_suppressed.setter
    def is_suppressed(self, value: bool) -> None: ...
    @_property
    def start_time(self) -> datetime.datetime: ...
    @start_time.setter
    def start_time(self, value: datetime.datetime) -> None: ...
    @_property
    def source_id_kind(self) -> PhoneCallHistorySourceIdKind: ...
    @source_id_kind.setter
    def source_id_kind(self, value: PhoneCallHistorySourceIdKind) -> None: ...
    @_property
    def address(self) -> typing.Optional[PhoneCallHistoryEntryAddress]: ...
    @address.setter
    def address(self, value: typing.Optional[PhoneCallHistoryEntryAddress]) -> None: ...
    @_property
    def source_id(self) -> str: ...
    @source_id.setter
    def source_id(self, value: str) -> None: ...
    @_property
    def remote_id(self) -> str: ...
    @remote_id.setter
    def remote_id(self, value: str) -> None: ...
    @_property
    def other_app_read_access(self) -> PhoneCallHistoryEntryOtherAppReadAccess: ...
    @other_app_read_access.setter
    def other_app_read_access(self, value: PhoneCallHistoryEntryOtherAppReadAccess) -> None: ...
    @_property
    def is_ringing(self) -> bool: ...
    @is_ringing.setter
    def is_ringing(self, value: bool) -> None: ...
    @_property
    def is_voicemail(self) -> bool: ...
    @is_voicemail.setter
    def is_voicemail(self, value: bool) -> None: ...
    @_property
    def id(self) -> str: ...
    @_property
    def source_display_name(self) -> str: ...

@typing.final
class PhoneCallHistoryEntryAddress(winrt.system.Object):
    @staticmethod
    def _from(obj: winrt.system.Object, /) -> PhoneCallHistoryEntryAddress: ...
    @typing.overload
    def __new__(cls: typing.Type[PhoneCallHistoryEntryAddress], raw_address: str, raw_address_kind: PhoneCallHistoryEntryRawAddressKind) -> PhoneCallHistoryEntryAddress: ...
    @typing.overload
    def __new__(cls: typing.Type[PhoneCallHistoryEntryAddress]) -> PhoneCallHistoryEntryAddress: ...
    @_property
    def raw_address_kind(self) -> PhoneCallHistoryEntryRawAddressKind: ...
    @raw_address_kind.setter
    def raw_address_kind(self, value: PhoneCallHistoryEntryRawAddressKind) -> None: ...
    @_property
    def raw_address(self) -> str: ...
    @raw_address.setter
    def raw_address(self, value: str) -> None: ...
    @_property
    def display_name(self) -> str: ...
    @display_name.setter
    def display_name(self, value: str) -> None: ...
    @_property
    def contact_id(self) -> str: ...
    @contact_id.setter
    def contact_id(self, value: str) -> None: ...

@typing.final
class PhoneCallHistoryEntryQueryOptions(winrt.system.Object):
    @staticmethod
    def _from(obj: winrt.system.Object, /) -> PhoneCallHistoryEntryQueryOptions: ...
    def __new__(cls: typing.Type[PhoneCallHistoryEntryQueryOptions]) -> PhoneCallHistoryEntryQueryOptions: ...
    @_property
    def desired_media(self) -> PhoneCallHistoryEntryQueryDesiredMedia: ...
    @desired_media.setter
    def desired_media(self, value: PhoneCallHistoryEntryQueryDesiredMedia) -> None: ...
    @_property
    def source_ids(self) -> typing.Optional[windows_foundation_collections.IVector[str]]: ...

@typing.final
class PhoneCallHistoryEntryReader(winrt.system.Object):
    @staticmethod
    def _from(obj: winrt.system.Object, /) -> PhoneCallHistoryEntryReader: ...
    def read_batch_async(self) -> windows_foundation.IAsyncOperation[windows_foundation_collections.IVectorView[PhoneCallHistoryEntry]]: ...

@typing.final
class PhoneCallHistoryManager_Static(type):
    def get_for_user(cls, user: typing.Optional[windows_system.User], /) -> typing.Optional[PhoneCallHistoryManagerForUser]: ...
    def request_store_async(cls, access_type: PhoneCallHistoryStoreAccessType, /) -> windows_foundation.IAsyncOperation[PhoneCallHistoryStore]: ...

@typing.final
class PhoneCallHistoryManager(winrt.system.Object, metaclass=PhoneCallHistoryManager_Static):
    pass

@typing.final
class PhoneCallHistoryManagerForUser(winrt.system.Object):
    @staticmethod
    def _from(obj: winrt.system.Object, /) -> PhoneCallHistoryManagerForUser: ...
    def request_store_async(self, access_type: PhoneCallHistoryStoreAccessType, /) -> windows_foundation.IAsyncOperation[PhoneCallHistoryStore]: ...
    @_property
    def user(self) -> typing.Optional[windows_system.User]: ...

@typing.final
class PhoneCallHistoryStore(winrt.system.Object):
    @staticmethod
    def _from(obj: winrt.system.Object, /) -> PhoneCallHistoryStore: ...
    def delete_entries_async(self, call_history_entries: typing.Iterable[PhoneCallHistoryEntry], /) -> windows_foundation.IAsyncAction: ...
    def delete_entry_async(self, call_history_entry: typing.Optional[PhoneCallHistoryEntry], /) -> windows_foundation.IAsyncAction: ...
    def get_entry_async(self, call_history_entry_id: str, /) -> windows_foundation.IAsyncOperation[PhoneCallHistoryEntry]: ...
    @typing.overload
    def get_entry_reader(self) -> typing.Optional[PhoneCallHistoryEntryReader]: ...
    @typing.overload
    def get_entry_reader(self, query_options: typing.Optional[PhoneCallHistoryEntryQueryOptions], /) -> typing.Optional[PhoneCallHistoryEntryReader]: ...
    def get_sources_unseen_count_async(self, source_ids: typing.Iterable[str], /) -> windows_foundation.IAsyncOperation[winrt.system.UInt32]: ...
    def get_unseen_count_async(self) -> windows_foundation.IAsyncOperation[winrt.system.UInt32]: ...
    def mark_all_as_seen_async(self) -> windows_foundation.IAsyncAction: ...
    def mark_entries_as_seen_async(self, call_history_entries: typing.Iterable[PhoneCallHistoryEntry], /) -> windows_foundation.IAsyncAction: ...
    def mark_entry_as_seen_async(self, call_history_entry: typing.Optional[PhoneCallHistoryEntry], /) -> windows_foundation.IAsyncAction: ...
    def mark_sources_as_seen_async(self, source_ids: typing.Iterable[str], /) -> windows_foundation.IAsyncAction: ...
    def save_entry_async(self, call_history_entry: typing.Optional[PhoneCallHistoryEntry], /) -> windows_foundation.IAsyncAction: ...

@typing.final
class PhoneCallInfo(winrt.system.Object):
    @staticmethod
    def _from(obj: winrt.system.Object, /) -> PhoneCallInfo: ...
    @_property
    def call_direction(self) -> PhoneCallDirection: ...
    @_property
    def display_name(self) -> str: ...
    @_property
    def is_hold_supported(self) -> bool: ...
    @_property
    def line_id(self) -> _uuid.UUID: ...
    @_property
    def phone_number(self) -> str: ...
    @_property
    def start_time(self) -> datetime.datetime: ...

@typing.final
class PhoneCallManager_Static(type):
    def request_store_async(cls) -> windows_foundation.IAsyncOperation[PhoneCallStore]: ...
    def show_phone_call_settings_u_i(cls) -> None: ...
    def show_phone_call_u_i(cls, phone_number: str, display_name: str, /) -> None: ...
    def add_call_state_changed(cls, handler: windows_foundation.EventHandler[winrt.system.Object], /) -> windows_foundation.EventRegistrationToken: ...
    def remove_call_state_changed(cls, token: windows_foundation.EventRegistrationToken, /) -> None: ...
    @_property
    def is_call_active(cls) -> bool: ...
    @_property
    def is_call_incoming(cls) -> bool: ...

@typing.final
class PhoneCallManager(winrt.system.Object, metaclass=PhoneCallManager_Static):
    pass

@typing.final
class PhoneCallStore(winrt.system.Object):
    @staticmethod
    def _from(obj: winrt.system.Object, /) -> PhoneCallStore: ...
    def get_default_line_async(self) -> windows_foundation.IAsyncOperation[_uuid.UUID]: ...
    def is_emergency_phone_number_async(self, number: str, /) -> windows_foundation.IAsyncOperation[bool]: ...
    def request_line_watcher(self) -> typing.Optional[PhoneLineWatcher]: ...

@typing.final
class PhoneCallVideoCapabilities(winrt.system.Object):
    @staticmethod
    def _from(obj: winrt.system.Object, /) -> PhoneCallVideoCapabilities: ...
    @_property
    def is_video_calling_capable(self) -> bool: ...

@typing.final
class PhoneCallVideoCapabilitiesManager_Static(type):
    def get_capabilities_async(cls, phone_number: str, /) -> windows_foundation.IAsyncOperation[PhoneCallVideoCapabilities]: ...

@typing.final
class PhoneCallVideoCapabilitiesManager(winrt.system.Object, metaclass=PhoneCallVideoCapabilitiesManager_Static):
    pass

@typing.final
class PhoneCallsResult(winrt.system.Object):
    @staticmethod
    def _from(obj: winrt.system.Object, /) -> PhoneCallsResult: ...
    @_property
    def all_active_phone_calls(self) -> typing.Optional[windows_foundation_collections.IVectorView[PhoneCall]]: ...
    @_property
    def operation_status(self) -> PhoneLineOperationStatus: ...

@typing.final
class PhoneDialOptions(winrt.system.Object):
    @staticmethod
    def _from(obj: winrt.system.Object, /) -> PhoneDialOptions: ...
    def __new__(cls: typing.Type[PhoneDialOptions]) -> PhoneDialOptions: ...
    @_property
    def number(self) -> str: ...
    @number.setter
    def number(self, value: str) -> None: ...
    @_property
    def media(self) -> PhoneCallMedia: ...
    @media.setter
    def media(self, value: PhoneCallMedia) -> None: ...
    @_property
    def display_name(self) -> str: ...
    @display_name.setter
    def display_name(self, value: str) -> None: ...
    @_property
    def contact_phone(self) -> typing.Optional[windows_applicationmodel_contacts.ContactPhone]: ...
    @contact_phone.setter
    def contact_phone(self, value: typing.Optional[windows_applicationmodel_contacts.ContactPhone]) -> None: ...
    @_property
    def contact(self) -> typing.Optional[windows_applicationmodel_contacts.Contact]: ...
    @contact.setter
    def contact(self, value: typing.Optional[windows_applicationmodel_contacts.Contact]) -> None: ...
    @_property
    def audio_endpoint(self) -> PhoneAudioRoutingEndpoint: ...
    @audio_endpoint.setter
    def audio_endpoint(self, value: PhoneAudioRoutingEndpoint) -> None: ...

@typing.final
class PhoneLine_Static(type):
    def from_id_async(cls, line_id: _uuid.UUID, /) -> windows_foundation.IAsyncOperation[PhoneLine]: ...

@typing.final
class PhoneLine(winrt.system.Object, metaclass=PhoneLine_Static):
    @staticmethod
    def _from(obj: winrt.system.Object, /) -> PhoneLine: ...
    def dial(self, number: str, display_name: str, /) -> None: ...
    def dial_with_options(self, options: typing.Optional[PhoneDialOptions], /) -> None: ...
    def dial_with_result(self, number: str, display_name: str, /) -> typing.Optional[PhoneLineDialResult]: ...
    def dial_with_result_async(self, number: str, display_name: str, /) -> windows_foundation.IAsyncOperation[PhoneLineDialResult]: ...
    def enable_text_reply(self, value: bool, /) -> None: ...
    def get_all_active_phone_calls(self) -> typing.Optional[PhoneCallsResult]: ...
    def get_all_active_phone_calls_async(self) -> windows_foundation.IAsyncOperation[PhoneCallsResult]: ...
    def is_immediate_dial_number_async(self, number: str, /) -> windows_foundation.IAsyncOperation[bool]: ...
    def add_line_changed(self, handler: windows_foundation.TypedEventHandler[PhoneLine, winrt.system.Object], /) -> windows_foundation.EventRegistrationToken: ...
    def remove_line_changed(self, token: windows_foundation.EventRegistrationToken, /) -> None: ...
    @_property
    def can_dial(self) -> bool: ...
    @_property
    def cellular_details(self) -> typing.Optional[PhoneLineCellularDetails]: ...
    @_property
    def display_color(self) -> windows_ui.Color: ...
    @_property
    def display_name(self) -> str: ...
    @_property
    def id(self) -> _uuid.UUID: ...
    @_property
    def line_configuration(self) -> typing.Optional[PhoneLineConfiguration]: ...
    @_property
    def network_name(self) -> str: ...
    @_property
    def network_state(self) -> PhoneNetworkState: ...
    @_property
    def supports_tile(self) -> bool: ...
    @_property
    def transport(self) -> PhoneLineTransport: ...
    @_property
    def video_calling_capabilities(self) -> typing.Optional[PhoneCallVideoCapabilities]: ...
    @_property
    def voicemail(self) -> typing.Optional[PhoneVoicemail]: ...
    @_property
    def transport_device_id(self) -> str: ...

@typing.final
class PhoneLineCellularDetails(winrt.system.Object):
    @staticmethod
    def _from(obj: winrt.system.Object, /) -> PhoneLineCellularDetails: ...
    def get_network_operator_display_text(self, location: PhoneLineNetworkOperatorDisplayTextLocation, /) -> str: ...
    @_property
    def is_modem_on(self) -> bool: ...
    @_property
    def registration_reject_code(self) -> winrt.system.Int32: ...
    @_property
    def sim_slot_index(self) -> winrt.system.Int32: ...
    @_property
    def sim_state(self) -> PhoneSimState: ...

@typing.final
class PhoneLineConfiguration(winrt.system.Object):
    @staticmethod
    def _from(obj: winrt.system.Object, /) -> PhoneLineConfiguration: ...
    @_property
    def extended_properties(self) -> typing.Optional[windows_foundation_collections.IMapView[str, winrt.system.Object]]: ...
    @_property
    def is_video_calling_enabled(self) -> bool: ...

@typing.final
class PhoneLineDialResult(winrt.system.Object):
    @staticmethod
    def _from(obj: winrt.system.Object, /) -> PhoneLineDialResult: ...
    @_property
    def dial_call_status(self) -> PhoneCallOperationStatus: ...
    @_property
    def dialed_call(self) -> typing.Optional[PhoneCall]: ...

@typing.final
class PhoneLineTransportDevice_Static(type):
    def from_id(cls, id: str, /) -> typing.Optional[PhoneLineTransportDevice]: ...
    @typing.overload
    def get_device_selector(cls) -> str: ...
    @typing.overload
    def get_device_selector(cls, transport: PhoneLineTransport, /) -> str: ...

@typing.final
class PhoneLineTransportDevice(winrt.system.Object, metaclass=PhoneLineTransportDevice_Static):
    @staticmethod
    def _from(obj: winrt.system.Object, /) -> PhoneLineTransportDevice: ...
    def connect(self) -> bool: ...
    def connect_async(self) -> windows_foundation.IAsyncOperation[bool]: ...
    def is_registered(self) -> bool: ...
    def register_app(self) -> None: ...
    def register_app_for_user(self, user: typing.Optional[windows_system.User], /) -> None: ...
    def request_access_async(self) -> windows_foundation.IAsyncOperation[windows_devices_enumeration.DeviceAccessStatus]: ...
    def unregister_app(self) -> None: ...
    def unregister_app_for_user(self, user: typing.Optional[windows_system.User], /) -> None: ...
    def add_audio_routing_status_changed(self, handler: windows_foundation.TypedEventHandler[PhoneLineTransportDevice, winrt.system.Object], /) -> windows_foundation.EventRegistrationToken: ...
    def remove_audio_routing_status_changed(self, token: windows_foundation.EventRegistrationToken, /) -> None: ...
    def add_in_band_ringing_enabled_changed(self, handler: windows_foundation.TypedEventHandler[PhoneLineTransportDevice, winrt.system.Object], /) -> windows_foundation.EventRegistrationToken: ...
    def remove_in_band_ringing_enabled_changed(self, token: windows_foundation.EventRegistrationToken, /) -> None: ...
    @_property
    def device_id(self) -> str: ...
    @_property
    def transport(self) -> PhoneLineTransport: ...
    @_property
    def audio_routing_status(self) -> TransportDeviceAudioRoutingStatus: ...
    @_property
    def in_band_ringing_enabled(self) -> bool: ...

@typing.final
class PhoneLineWatcher(winrt.system.Object):
    @staticmethod
    def _from(obj: winrt.system.Object, /) -> PhoneLineWatcher: ...
    def start(self) -> None: ...
    def stop(self) -> None: ...
    def add_enumeration_completed(self, handler: windows_foundation.TypedEventHandler[PhoneLineWatcher, winrt.system.Object], /) -> windows_foundation.EventRegistrationToken: ...
    def remove_enumeration_completed(self, token: windows_foundation.EventRegistrationToken, /) -> None: ...
    def add_line_added(self, handler: windows_foundation.TypedEventHandler[PhoneLineWatcher, PhoneLineWatcherEventArgs], /) -> windows_foundation.EventRegistrationToken: ...
    def remove_line_added(self, token: windows_foundation.EventRegistrationToken, /) -> None: ...
    def add_line_removed(self, handler: windows_foundation.TypedEventHandler[PhoneLineWatcher, PhoneLineWatcherEventArgs], /) -> windows_foundation.EventRegistrationToken: ...
    def remove_line_removed(self, token: windows_foundation.EventRegistrationToken, /) -> None: ...
    def add_line_updated(self, handler: windows_foundation.TypedEventHandler[PhoneLineWatcher, PhoneLineWatcherEventArgs], /) -> windows_foundation.EventRegistrationToken: ...
    def remove_line_updated(self, token: windows_foundation.EventRegistrationToken, /) -> None: ...
    def add_stopped(self, handler: windows_foundation.TypedEventHandler[PhoneLineWatcher, winrt.system.Object], /) -> windows_foundation.EventRegistrationToken: ...
    def remove_stopped(self, token: windows_foundation.EventRegistrationToken, /) -> None: ...
    @_property
    def status(self) -> PhoneLineWatcherStatus: ...

@typing.final
class PhoneLineWatcherEventArgs(winrt.system.Object):
    @staticmethod
    def _from(obj: winrt.system.Object, /) -> PhoneLineWatcherEventArgs: ...
    @_property
    def line_id(self) -> _uuid.UUID: ...

@typing.final
class PhoneVoicemail(winrt.system.Object):
    @staticmethod
    def _from(obj: winrt.system.Object, /) -> PhoneVoicemail: ...
    def dial_voicemail_async(self) -> windows_foundation.IAsyncAction: ...
    @_property
    def message_count(self) -> winrt.system.Int32: ...
    @_property
    def number(self) -> str: ...
    @_property
    def type(self) -> PhoneVoicemailType: ...

@typing.final
class VoipCallCoordinator_Static(type):
    def get_default(cls) -> typing.Optional[VoipCallCoordinator]: ...
    def get_device_selector_for_call_control(cls) -> str: ...
    def is_call_control_device_kind_supported_for_association(cls, kind: VoipCallControlDeviceKind, /) -> bool: ...

@typing.final
class VoipCallCoordinator(winrt.system.Object, metaclass=VoipCallCoordinator_Static):
    @staticmethod
    def _from(obj: winrt.system.Object, /) -> VoipCallCoordinator: ...
    def cancel_upgrade(self, call_upgrade_guid: _uuid.UUID, /) -> None: ...
    def notify_muted(self) -> None: ...
    def notify_unmuted(self) -> None: ...
    def request_incoming_upgrade_to_video_call(self, context: str, contact_name: str, contact_number: str, contact_image: typing.Optional[windows_foundation.Uri], service_name: str, branding_image: typing.Optional[windows_foundation.Uri], call_details: str, ringtone: typing.Optional[windows_foundation.Uri], ring_timeout: datetime.timedelta, /) -> typing.Optional[VoipPhoneCall]: ...
    def request_new_app_initiated_call(self, context: str, contact_name: str, contact_number: str, service_name: str, media: VoipPhoneCallMedia, /) -> typing.Optional[VoipPhoneCall]: ...
    def request_new_app_initiated_call_with_options(self, call_options: typing.Optional[AppInitiatedVoipPhoneCallOptions], /) -> typing.Optional[VoipPhoneCall]: ...
    @typing.overload
    def request_new_incoming_call(self, context: str, contact_name: str, contact_number: str, contact_image: typing.Optional[windows_foundation.Uri], service_name: str, branding_image: typing.Optional[windows_foundation.Uri], call_details: str, ringtone: typing.Optional[windows_foundation.Uri], media: VoipPhoneCallMedia, ring_timeout: datetime.timedelta, /) -> typing.Optional[VoipPhoneCall]: ...
    @typing.overload
    def request_new_incoming_call(self, context: str, contact_name: str, contact_number: str, contact_image: typing.Optional[windows_foundation.Uri], service_name: str, branding_image: typing.Optional[windows_foundation.Uri], call_details: str, ringtone: typing.Optional[windows_foundation.Uri], media: VoipPhoneCallMedia, ring_timeout: datetime.timedelta, contact_remote_id: str, /) -> typing.Optional[VoipPhoneCall]: ...
    def request_new_incoming_call_with_options(self, call_options: typing.Optional[IncomingVoipPhoneCallOptions], /) -> typing.Optional[VoipPhoneCall]: ...
    def request_new_outgoing_call(self, context: str, contact_name: str, service_name: str, media: VoipPhoneCallMedia, /) -> typing.Optional[VoipPhoneCall]: ...
    def request_new_outgoing_call_with_options(self, call_options: typing.Optional[OutgoingVoipPhoneCallOptions], /) -> typing.Optional[VoipPhoneCall]: ...
    def request_outgoing_upgrade_to_video_call(self, call_upgrade_guid: _uuid.UUID, context: str, contact_name: str, service_name: str, /) -> typing.Optional[VoipPhoneCall]: ...
    @typing.overload
    def reserve_call_resources_async(self) -> windows_foundation.IAsyncOperation[VoipPhoneCallResourceReservationStatus]: ...
    @typing.overload
    def reserve_call_resources_async(self, task_entry_point: str, /) -> windows_foundation.IAsyncOperation[VoipPhoneCallResourceReservationStatus]: ...
    def setup_new_accepted_call(self, context: str, contact_name: str, contact_number: str, service_name: str, media: VoipPhoneCallMedia, /) -> typing.Optional[VoipPhoneCall]: ...
    def setup_new_accepted_call_with_options(self, call_options: typing.Optional[AcceptedVoipPhoneCallOptions], /) -> typing.Optional[VoipPhoneCall]: ...
    def terminate_cellular_call(self, call_upgrade_guid: _uuid.UUID, /) -> None: ...
    def add_mute_state_changed(self, mute_change_handler: windows_foundation.TypedEventHandler[VoipCallCoordinator, MuteChangeEventArgs], /) -> windows_foundation.EventRegistrationToken: ...
    def remove_mute_state_changed(self, token: windows_foundation.EventRegistrationToken, /) -> None: ...

@typing.final
class VoipPhoneCall(winrt.system.Object):
    @staticmethod
    def _from(obj: winrt.system.Object, /) -> VoipPhoneCall: ...
    def add_associated_call_control_device(self, device_id: str, /) -> None: ...
    def get_associated_call_control_devices(self) -> typing.Optional[windows_foundation_collections.IVectorView[str]]: ...
    def notify_call_accepted(self, media: VoipPhoneCallMedia, /) -> None: ...
    @typing.overload
    def notify_call_active(self) -> None: ...
    @typing.overload
    def notify_call_active(self, associated_device_ids: typing.Iterable[str], /) -> None: ...
    def notify_call_ended(self) -> None: ...
    def notify_call_held(self) -> None: ...
    def notify_call_ready(self) -> None: ...
    def remove_associated_call_control_device(self, device_id: str, /) -> None: ...
    def set_associated_call_control_devices(self, associated_device_ids: typing.Iterable[str], /) -> None: ...
    def try_show_app_u_i(self) -> None: ...
    def add_answer_requested(self, accept_handler: windows_foundation.TypedEventHandler[VoipPhoneCall, CallAnswerEventArgs], /) -> windows_foundation.EventRegistrationToken: ...
    def remove_answer_requested(self, token: windows_foundation.EventRegistrationToken, /) -> None: ...
    def add_end_requested(self, handler: windows_foundation.TypedEventHandler[VoipPhoneCall, CallStateChangeEventArgs], /) -> windows_foundation.EventRegistrationToken: ...
    def remove_end_requested(self, token: windows_foundation.EventRegistrationToken, /) -> None: ...
    def add_hold_requested(self, handler: windows_foundation.TypedEventHandler[VoipPhoneCall, CallStateChangeEventArgs], /) -> windows_foundation.EventRegistrationToken: ...
    def remove_hold_requested(self, token: windows_foundation.EventRegistrationToken, /) -> None: ...
    def add_reject_requested(self, reject_handler: windows_foundation.TypedEventHandler[VoipPhoneCall, CallRejectEventArgs], /) -> windows_foundation.EventRegistrationToken: ...
    def remove_reject_requested(self, token: windows_foundation.EventRegistrationToken, /) -> None: ...
    def add_resume_requested(self, handler: windows_foundation.TypedEventHandler[VoipPhoneCall, CallStateChangeEventArgs], /) -> windows_foundation.EventRegistrationToken: ...
    def remove_resume_requested(self, token: windows_foundation.EventRegistrationToken, /) -> None: ...
    @_property
    def start_time(self) -> datetime.datetime: ...
    @start_time.setter
    def start_time(self, value: datetime.datetime) -> None: ...
    @_property
    def contact_name(self) -> str: ...
    @contact_name.setter
    def contact_name(self, value: str) -> None: ...
    @_property
    def call_media(self) -> VoipPhoneCallMedia: ...
    @call_media.setter
    def call_media(self, value: VoipPhoneCallMedia) -> None: ...
    @_property
    def is_using_associated_devices_list(self) -> bool: ...

