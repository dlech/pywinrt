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
import winrt.windows.media as windows_media
import winrt.windows.storage.streams as windows_storage_streams

from winrt.windows.media.control import GlobalSystemMediaTransportControlsSessionPlaybackStatus

Self = typing.TypeVar('Self')

@typing.final
class CurrentSessionChangedEventArgs(winrt.system.Object):
    @staticmethod
    def _from(obj: winrt.system.Object, /) -> CurrentSessionChangedEventArgs: ...

@typing.final
class GlobalSystemMediaTransportControlsSession(winrt.system.Object):
    @staticmethod
    def _from(obj: winrt.system.Object, /) -> GlobalSystemMediaTransportControlsSession: ...
    def get_playback_info(self) -> typing.Optional[GlobalSystemMediaTransportControlsSessionPlaybackInfo]: ...
    def get_timeline_properties(self) -> typing.Optional[GlobalSystemMediaTransportControlsSessionTimelineProperties]: ...
    def try_change_auto_repeat_mode_async(self, requested_auto_repeat_mode: windows_media.MediaPlaybackAutoRepeatMode, /) -> windows_foundation.IAsyncOperation[bool]: ...
    def try_change_channel_down_async(self) -> windows_foundation.IAsyncOperation[bool]: ...
    def try_change_channel_up_async(self) -> windows_foundation.IAsyncOperation[bool]: ...
    def try_change_playback_position_async(self, requested_playback_position: winrt.system.Int64, /) -> windows_foundation.IAsyncOperation[bool]: ...
    def try_change_playback_rate_async(self, requested_playback_rate: winrt.system.Double, /) -> windows_foundation.IAsyncOperation[bool]: ...
    def try_change_shuffle_active_async(self, requested_shuffle_state: bool, /) -> windows_foundation.IAsyncOperation[bool]: ...
    def try_fast_forward_async(self) -> windows_foundation.IAsyncOperation[bool]: ...
    def try_get_media_properties_async(self) -> windows_foundation.IAsyncOperation[GlobalSystemMediaTransportControlsSessionMediaProperties]: ...
    def try_pause_async(self) -> windows_foundation.IAsyncOperation[bool]: ...
    def try_play_async(self) -> windows_foundation.IAsyncOperation[bool]: ...
    def try_record_async(self) -> windows_foundation.IAsyncOperation[bool]: ...
    def try_rewind_async(self) -> windows_foundation.IAsyncOperation[bool]: ...
    def try_skip_next_async(self) -> windows_foundation.IAsyncOperation[bool]: ...
    def try_skip_previous_async(self) -> windows_foundation.IAsyncOperation[bool]: ...
    def try_stop_async(self) -> windows_foundation.IAsyncOperation[bool]: ...
    def try_toggle_play_pause_async(self) -> windows_foundation.IAsyncOperation[bool]: ...
    def add_media_properties_changed(self, handler: windows_foundation.TypedEventHandler[GlobalSystemMediaTransportControlsSession, MediaPropertiesChangedEventArgs], /) -> windows_foundation.EventRegistrationToken: ...
    def remove_media_properties_changed(self, token: windows_foundation.EventRegistrationToken, /) -> None: ...
    def add_playback_info_changed(self, handler: windows_foundation.TypedEventHandler[GlobalSystemMediaTransportControlsSession, PlaybackInfoChangedEventArgs], /) -> windows_foundation.EventRegistrationToken: ...
    def remove_playback_info_changed(self, token: windows_foundation.EventRegistrationToken, /) -> None: ...
    def add_timeline_properties_changed(self, handler: windows_foundation.TypedEventHandler[GlobalSystemMediaTransportControlsSession, TimelinePropertiesChangedEventArgs], /) -> windows_foundation.EventRegistrationToken: ...
    def remove_timeline_properties_changed(self, token: windows_foundation.EventRegistrationToken, /) -> None: ...
    @_property
    def source_app_user_model_id(self) -> str: ...

@typing.final
class GlobalSystemMediaTransportControlsSessionManager_Static(type):
    def request_async(cls) -> windows_foundation.IAsyncOperation[GlobalSystemMediaTransportControlsSessionManager]: ...

@typing.final
class GlobalSystemMediaTransportControlsSessionManager(winrt.system.Object, metaclass=GlobalSystemMediaTransportControlsSessionManager_Static):
    @staticmethod
    def _from(obj: winrt.system.Object, /) -> GlobalSystemMediaTransportControlsSessionManager: ...
    def get_current_session(self) -> typing.Optional[GlobalSystemMediaTransportControlsSession]: ...
    def get_sessions(self) -> typing.Optional[windows_foundation_collections.IVectorView[GlobalSystemMediaTransportControlsSession]]: ...
    def add_current_session_changed(self, handler: windows_foundation.TypedEventHandler[GlobalSystemMediaTransportControlsSessionManager, CurrentSessionChangedEventArgs], /) -> windows_foundation.EventRegistrationToken: ...
    def remove_current_session_changed(self, token: windows_foundation.EventRegistrationToken, /) -> None: ...
    def add_sessions_changed(self, handler: windows_foundation.TypedEventHandler[GlobalSystemMediaTransportControlsSessionManager, SessionsChangedEventArgs], /) -> windows_foundation.EventRegistrationToken: ...
    def remove_sessions_changed(self, token: windows_foundation.EventRegistrationToken, /) -> None: ...

@typing.final
class GlobalSystemMediaTransportControlsSessionMediaProperties(winrt.system.Object):
    @staticmethod
    def _from(obj: winrt.system.Object, /) -> GlobalSystemMediaTransportControlsSessionMediaProperties: ...
    @_property
    def album_artist(self) -> str: ...
    @_property
    def album_title(self) -> str: ...
    @_property
    def album_track_count(self) -> winrt.system.Int32: ...
    @_property
    def artist(self) -> str: ...
    @_property
    def genres(self) -> typing.Optional[windows_foundation_collections.IVectorView[str]]: ...
    @_property
    def playback_type(self) -> typing.Optional[typing.Optional[windows_media.MediaPlaybackType]]: ...
    @_property
    def subtitle(self) -> str: ...
    @_property
    def thumbnail(self) -> typing.Optional[windows_storage_streams.IRandomAccessStreamReference]: ...
    @_property
    def title(self) -> str: ...
    @_property
    def track_number(self) -> winrt.system.Int32: ...

@typing.final
class GlobalSystemMediaTransportControlsSessionPlaybackControls(winrt.system.Object):
    @staticmethod
    def _from(obj: winrt.system.Object, /) -> GlobalSystemMediaTransportControlsSessionPlaybackControls: ...
    @_property
    def is_channel_down_enabled(self) -> bool: ...
    @_property
    def is_channel_up_enabled(self) -> bool: ...
    @_property
    def is_fast_forward_enabled(self) -> bool: ...
    @_property
    def is_next_enabled(self) -> bool: ...
    @_property
    def is_pause_enabled(self) -> bool: ...
    @_property
    def is_play_enabled(self) -> bool: ...
    @_property
    def is_play_pause_toggle_enabled(self) -> bool: ...
    @_property
    def is_playback_position_enabled(self) -> bool: ...
    @_property
    def is_playback_rate_enabled(self) -> bool: ...
    @_property
    def is_previous_enabled(self) -> bool: ...
    @_property
    def is_record_enabled(self) -> bool: ...
    @_property
    def is_repeat_enabled(self) -> bool: ...
    @_property
    def is_rewind_enabled(self) -> bool: ...
    @_property
    def is_shuffle_enabled(self) -> bool: ...
    @_property
    def is_stop_enabled(self) -> bool: ...

@typing.final
class GlobalSystemMediaTransportControlsSessionPlaybackInfo(winrt.system.Object):
    @staticmethod
    def _from(obj: winrt.system.Object, /) -> GlobalSystemMediaTransportControlsSessionPlaybackInfo: ...
    @_property
    def auto_repeat_mode(self) -> typing.Optional[typing.Optional[windows_media.MediaPlaybackAutoRepeatMode]]: ...
    @_property
    def controls(self) -> typing.Optional[GlobalSystemMediaTransportControlsSessionPlaybackControls]: ...
    @_property
    def is_shuffle_active(self) -> typing.Optional[typing.Optional[bool]]: ...
    @_property
    def playback_rate(self) -> typing.Optional[typing.Optional[winrt.system.Double]]: ...
    @_property
    def playback_status(self) -> GlobalSystemMediaTransportControlsSessionPlaybackStatus: ...
    @_property
    def playback_type(self) -> typing.Optional[typing.Optional[windows_media.MediaPlaybackType]]: ...

@typing.final
class GlobalSystemMediaTransportControlsSessionTimelineProperties(winrt.system.Object):
    @staticmethod
    def _from(obj: winrt.system.Object, /) -> GlobalSystemMediaTransportControlsSessionTimelineProperties: ...
    @_property
    def end_time(self) -> datetime.timedelta: ...
    @_property
    def last_updated_time(self) -> datetime.datetime: ...
    @_property
    def max_seek_time(self) -> datetime.timedelta: ...
    @_property
    def min_seek_time(self) -> datetime.timedelta: ...
    @_property
    def position(self) -> datetime.timedelta: ...
    @_property
    def start_time(self) -> datetime.timedelta: ...

@typing.final
class MediaPropertiesChangedEventArgs(winrt.system.Object):
    @staticmethod
    def _from(obj: winrt.system.Object, /) -> MediaPropertiesChangedEventArgs: ...

@typing.final
class PlaybackInfoChangedEventArgs(winrt.system.Object):
    @staticmethod
    def _from(obj: winrt.system.Object, /) -> PlaybackInfoChangedEventArgs: ...

@typing.final
class SessionsChangedEventArgs(winrt.system.Object):
    @staticmethod
    def _from(obj: winrt.system.Object, /) -> SessionsChangedEventArgs: ...

@typing.final
class TimelinePropertiesChangedEventArgs(winrt.system.Object):
    @staticmethod
    def _from(obj: winrt.system.Object, /) -> TimelinePropertiesChangedEventArgs: ...

