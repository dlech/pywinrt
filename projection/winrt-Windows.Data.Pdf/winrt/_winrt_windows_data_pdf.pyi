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
import winrt.windows.storage.streams as windows_storage_streams
import winrt.windows.ui as windows_ui

from winrt.windows.data.pdf import PdfPageRotation

Self = typing.TypeVar('Self')

@typing.final
class PdfDocument_Static(type):
    @typing.overload
    def load_from_file_async(cls, file: typing.Optional[windows_storage.IStorageFile], /) -> windows_foundation.IAsyncOperation[PdfDocument]: ...
    @typing.overload
    def load_from_file_async(cls, file: typing.Optional[windows_storage.IStorageFile], password: str, /) -> windows_foundation.IAsyncOperation[PdfDocument]: ...
    @typing.overload
    def load_from_stream_async(cls, input_stream: typing.Optional[windows_storage_streams.IRandomAccessStream], /) -> windows_foundation.IAsyncOperation[PdfDocument]: ...
    @typing.overload
    def load_from_stream_async(cls, input_stream: typing.Optional[windows_storage_streams.IRandomAccessStream], password: str, /) -> windows_foundation.IAsyncOperation[PdfDocument]: ...

@typing.final
class PdfDocument(winrt.system.Object, metaclass=PdfDocument_Static):
    @staticmethod
    def _from(obj: winrt.system.Object, /) -> PdfDocument: ...
    def get_page(self, page_index: winrt.system.UInt32, /) -> typing.Optional[PdfPage]: ...
    @_property
    def is_password_protected(self) -> bool: ...
    @_property
    def page_count(self) -> winrt.system.UInt32: ...

@typing.final
class PdfPage(winrt.system.Object):
    def __enter__(self: Self) -> Self: ...
    def __exit__(self, *args) -> None: ...
    @staticmethod
    def _from(obj: winrt.system.Object, /) -> PdfPage: ...
    def close(self) -> None: ...
    def prepare_page_async(self) -> windows_foundation.IAsyncAction: ...
    @typing.overload
    def render_to_stream_async(self, output_stream: typing.Optional[windows_storage_streams.IRandomAccessStream], /) -> windows_foundation.IAsyncAction: ...
    @typing.overload
    def render_to_stream_async(self, output_stream: typing.Optional[windows_storage_streams.IRandomAccessStream], options: typing.Optional[PdfPageRenderOptions], /) -> windows_foundation.IAsyncAction: ...
    @_property
    def dimensions(self) -> typing.Optional[PdfPageDimensions]: ...
    @_property
    def index(self) -> winrt.system.UInt32: ...
    @_property
    def preferred_zoom(self) -> winrt.system.Single: ...
    @_property
    def rotation(self) -> PdfPageRotation: ...
    @_property
    def size(self) -> windows_foundation.Size: ...

@typing.final
class PdfPageDimensions(winrt.system.Object):
    @staticmethod
    def _from(obj: winrt.system.Object, /) -> PdfPageDimensions: ...
    @_property
    def art_box(self) -> windows_foundation.Rect: ...
    @_property
    def bleed_box(self) -> windows_foundation.Rect: ...
    @_property
    def crop_box(self) -> windows_foundation.Rect: ...
    @_property
    def media_box(self) -> windows_foundation.Rect: ...
    @_property
    def trim_box(self) -> windows_foundation.Rect: ...

@typing.final
class PdfPageRenderOptions(winrt.system.Object):
    @staticmethod
    def _from(obj: winrt.system.Object, /) -> PdfPageRenderOptions: ...
    def __new__(cls: typing.Type[PdfPageRenderOptions]) -> PdfPageRenderOptions: ...
    @_property
    def source_rect(self) -> windows_foundation.Rect: ...
    @source_rect.setter
    def source_rect(self, value: windows_foundation.Rect) -> None: ...
    @_property
    def is_ignoring_high_contrast(self) -> bool: ...
    @is_ignoring_high_contrast.setter
    def is_ignoring_high_contrast(self, value: bool) -> None: ...
    @_property
    def destination_width(self) -> winrt.system.UInt32: ...
    @destination_width.setter
    def destination_width(self, value: winrt.system.UInt32) -> None: ...
    @_property
    def destination_height(self) -> winrt.system.UInt32: ...
    @destination_height.setter
    def destination_height(self, value: winrt.system.UInt32) -> None: ...
    @_property
    def bitmap_encoder_id(self) -> _uuid.UUID: ...
    @bitmap_encoder_id.setter
    def bitmap_encoder_id(self, value: _uuid.UUID) -> None: ...
    @_property
    def background_color(self) -> windows_ui.Color: ...
    @background_color.setter
    def background_color(self, value: windows_ui.Color) -> None: ...

