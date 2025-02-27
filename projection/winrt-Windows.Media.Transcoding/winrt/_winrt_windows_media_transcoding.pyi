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
import winrt.windows.media.core as windows_media_core
import winrt.windows.media.mediaproperties as windows_media_mediaproperties
import winrt.windows.storage as windows_storage
import winrt.windows.storage.streams as windows_storage_streams

from winrt.windows.media.transcoding import MediaVideoProcessingAlgorithm, TranscodeFailureReason

Self = typing.TypeVar('Self')

@typing.final
class MediaTranscoder(winrt.system.Object):
    @staticmethod
    def _from(obj: winrt.system.Object, /) -> MediaTranscoder: ...
    def __new__(cls: typing.Type[MediaTranscoder]) -> MediaTranscoder: ...
    @typing.overload
    def add_audio_effect(self, activatable_class_id: str, /) -> None: ...
    @typing.overload
    def add_audio_effect(self, activatable_class_id: str, effect_required: bool, configuration: typing.Optional[windows_foundation_collections.IPropertySet], /) -> None: ...
    @typing.overload
    def add_video_effect(self, activatable_class_id: str, /) -> None: ...
    @typing.overload
    def add_video_effect(self, activatable_class_id: str, effect_required: bool, configuration: typing.Optional[windows_foundation_collections.IPropertySet], /) -> None: ...
    def clear_effects(self) -> None: ...
    def prepare_file_transcode_async(self, source: typing.Optional[windows_storage.IStorageFile], destination: typing.Optional[windows_storage.IStorageFile], profile: typing.Optional[windows_media_mediaproperties.MediaEncodingProfile], /) -> windows_foundation.IAsyncOperation[PrepareTranscodeResult]: ...
    def prepare_media_stream_source_transcode_async(self, source: typing.Optional[windows_media_core.IMediaSource], destination: typing.Optional[windows_storage_streams.IRandomAccessStream], profile: typing.Optional[windows_media_mediaproperties.MediaEncodingProfile], /) -> windows_foundation.IAsyncOperation[PrepareTranscodeResult]: ...
    def prepare_stream_transcode_async(self, source: typing.Optional[windows_storage_streams.IRandomAccessStream], destination: typing.Optional[windows_storage_streams.IRandomAccessStream], profile: typing.Optional[windows_media_mediaproperties.MediaEncodingProfile], /) -> windows_foundation.IAsyncOperation[PrepareTranscodeResult]: ...
    @_property
    def trim_stop_time(self) -> datetime.timedelta: ...
    @trim_stop_time.setter
    def trim_stop_time(self, value: datetime.timedelta) -> None: ...
    @_property
    def trim_start_time(self) -> datetime.timedelta: ...
    @trim_start_time.setter
    def trim_start_time(self, value: datetime.timedelta) -> None: ...
    @_property
    def hardware_acceleration_enabled(self) -> bool: ...
    @hardware_acceleration_enabled.setter
    def hardware_acceleration_enabled(self, value: bool) -> None: ...
    @_property
    def always_reencode(self) -> bool: ...
    @always_reencode.setter
    def always_reencode(self, value: bool) -> None: ...
    @_property
    def video_processing_algorithm(self) -> MediaVideoProcessingAlgorithm: ...
    @video_processing_algorithm.setter
    def video_processing_algorithm(self, value: MediaVideoProcessingAlgorithm) -> None: ...

@typing.final
class PrepareTranscodeResult(winrt.system.Object):
    @staticmethod
    def _from(obj: winrt.system.Object, /) -> PrepareTranscodeResult: ...
    def transcode_async(self) -> windows_foundation.IAsyncActionWithProgress[winrt.system.Double]: ...
    @_property
    def can_transcode(self) -> bool: ...
    @_property
    def failure_reason(self) -> TranscodeFailureReason: ...

