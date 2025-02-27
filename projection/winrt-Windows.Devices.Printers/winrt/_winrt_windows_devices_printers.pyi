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
import winrt.windows.graphics.printing as windows_graphics_printing
import winrt.windows.graphics.printing.printticket as windows_graphics_printing_printticket
import winrt.windows.storage.streams as windows_storage_streams

from winrt.windows.devices.printers import IppAttributeErrorReason, IppAttributeValueKind, IppPrintDeviceKind, IppResolutionUnit, PageConfigurationSource

Self = typing.TypeVar('Self')

@typing.final
class IppAttributeError(winrt.system.Object):
    @staticmethod
    def _from(obj: winrt.system.Object, /) -> IppAttributeError: ...
    def get_unsupported_values(self) -> typing.Optional[windows_foundation_collections.IVectorView[IppAttributeValue]]: ...
    @_property
    def extended_error(self) -> windows_foundation.HResult: ...
    @_property
    def reason(self) -> IppAttributeErrorReason: ...

@typing.final
class IppAttributeValue_Static(type):
    def create_boolean(cls, value: bool, /) -> typing.Optional[IppAttributeValue]: ...
    def create_boolean_array(cls, values: typing.Iterable[bool], /) -> typing.Optional[IppAttributeValue]: ...
    def create_charset(cls, value: str, /) -> typing.Optional[IppAttributeValue]: ...
    def create_charset_array(cls, values: typing.Iterable[str], /) -> typing.Optional[IppAttributeValue]: ...
    def create_collection(cls, member_attributes: typing.Iterable[windows_foundation_collections.IKeyValuePair[str, IppAttributeValue]], /) -> typing.Optional[IppAttributeValue]: ...
    def create_collection_array(cls, member_attributes_array: typing.Iterable[windows_foundation_collections.IIterable[windows_foundation_collections.IKeyValuePair[str, IppAttributeValue]]], /) -> typing.Optional[IppAttributeValue]: ...
    def create_date_time(cls, value: datetime.datetime, /) -> typing.Optional[IppAttributeValue]: ...
    def create_date_time_array(cls, values: typing.Iterable[datetime.datetime], /) -> typing.Optional[IppAttributeValue]: ...
    def create_enum(cls, value: winrt.system.Int32, /) -> typing.Optional[IppAttributeValue]: ...
    def create_enum_array(cls, values: typing.Iterable[winrt.system.Int32], /) -> typing.Optional[IppAttributeValue]: ...
    def create_integer(cls, value: winrt.system.Int32, /) -> typing.Optional[IppAttributeValue]: ...
    def create_integer_array(cls, values: typing.Iterable[winrt.system.Int32], /) -> typing.Optional[IppAttributeValue]: ...
    def create_keyword(cls, value: str, /) -> typing.Optional[IppAttributeValue]: ...
    def create_keyword_array(cls, values: typing.Iterable[str], /) -> typing.Optional[IppAttributeValue]: ...
    def create_mime_media(cls, value: str, /) -> typing.Optional[IppAttributeValue]: ...
    def create_mime_media_array(cls, values: typing.Iterable[str], /) -> typing.Optional[IppAttributeValue]: ...
    def create_name_with_language(cls, value: typing.Optional[IppTextWithLanguage], /) -> typing.Optional[IppAttributeValue]: ...
    def create_name_with_language_array(cls, values: typing.Iterable[IppTextWithLanguage], /) -> typing.Optional[IppAttributeValue]: ...
    def create_name_without_language(cls, value: str, /) -> typing.Optional[IppAttributeValue]: ...
    def create_name_without_language_array(cls, values: typing.Iterable[str], /) -> typing.Optional[IppAttributeValue]: ...
    def create_natural_language(cls, value: str, /) -> typing.Optional[IppAttributeValue]: ...
    def create_natural_language_array(cls, values: typing.Iterable[str], /) -> typing.Optional[IppAttributeValue]: ...
    def create_no_value(cls) -> typing.Optional[IppAttributeValue]: ...
    def create_octet_string(cls, value: typing.Optional[windows_storage_streams.IBuffer], /) -> typing.Optional[IppAttributeValue]: ...
    def create_octet_string_array(cls, values: typing.Iterable[windows_storage_streams.IBuffer], /) -> typing.Optional[IppAttributeValue]: ...
    def create_range_of_integer(cls, value: typing.Optional[IppIntegerRange], /) -> typing.Optional[IppAttributeValue]: ...
    def create_range_of_integer_array(cls, values: typing.Iterable[IppIntegerRange], /) -> typing.Optional[IppAttributeValue]: ...
    def create_resolution(cls, value: typing.Optional[IppResolution], /) -> typing.Optional[IppAttributeValue]: ...
    def create_resolution_array(cls, values: typing.Iterable[IppResolution], /) -> typing.Optional[IppAttributeValue]: ...
    def create_text_with_language(cls, value: typing.Optional[IppTextWithLanguage], /) -> typing.Optional[IppAttributeValue]: ...
    def create_text_with_language_array(cls, values: typing.Iterable[IppTextWithLanguage], /) -> typing.Optional[IppAttributeValue]: ...
    def create_text_without_language(cls, value: str, /) -> typing.Optional[IppAttributeValue]: ...
    def create_text_without_language_array(cls, values: typing.Iterable[str], /) -> typing.Optional[IppAttributeValue]: ...
    def create_unknown(cls) -> typing.Optional[IppAttributeValue]: ...
    def create_unsupported(cls) -> typing.Optional[IppAttributeValue]: ...
    def create_uri(cls, value: typing.Optional[windows_foundation.Uri], /) -> typing.Optional[IppAttributeValue]: ...
    def create_uri_array(cls, values: typing.Iterable[windows_foundation.Uri], /) -> typing.Optional[IppAttributeValue]: ...
    def create_uri_schema(cls, value: str, /) -> typing.Optional[IppAttributeValue]: ...
    def create_uri_schema_array(cls, values: typing.Iterable[str], /) -> typing.Optional[IppAttributeValue]: ...

@typing.final
class IppAttributeValue(winrt.system.Object, metaclass=IppAttributeValue_Static):
    @staticmethod
    def _from(obj: winrt.system.Object, /) -> IppAttributeValue: ...
    def get_boolean_array(self) -> typing.Optional[windows_foundation_collections.IVector[bool]]: ...
    def get_charset_array(self) -> typing.Optional[windows_foundation_collections.IVector[str]]: ...
    def get_collection_array(self) -> typing.Optional[windows_foundation_collections.IVector[windows_foundation_collections.IMapView[str, IppAttributeValue]]]: ...
    def get_date_time_array(self) -> typing.Optional[windows_foundation_collections.IVector[datetime.datetime]]: ...
    def get_enum_array(self) -> typing.Optional[windows_foundation_collections.IVector[winrt.system.Int32]]: ...
    def get_integer_array(self) -> typing.Optional[windows_foundation_collections.IVector[winrt.system.Int32]]: ...
    def get_keyword_array(self) -> typing.Optional[windows_foundation_collections.IVector[str]]: ...
    def get_mime_media_type_array(self) -> typing.Optional[windows_foundation_collections.IVector[str]]: ...
    def get_name_with_language_array(self) -> typing.Optional[windows_foundation_collections.IVector[IppTextWithLanguage]]: ...
    def get_name_without_language_array(self) -> typing.Optional[windows_foundation_collections.IVector[str]]: ...
    def get_natural_language_array(self) -> typing.Optional[windows_foundation_collections.IVector[str]]: ...
    def get_octet_string_array(self) -> typing.Optional[windows_foundation_collections.IVector[windows_storage_streams.IBuffer]]: ...
    def get_range_of_integer_array(self) -> typing.Optional[windows_foundation_collections.IVector[IppIntegerRange]]: ...
    def get_resolution_array(self) -> typing.Optional[windows_foundation_collections.IVector[IppResolution]]: ...
    def get_text_with_language_array(self) -> typing.Optional[windows_foundation_collections.IVector[IppTextWithLanguage]]: ...
    def get_text_without_language_array(self) -> typing.Optional[windows_foundation_collections.IVector[str]]: ...
    def get_uri_array(self) -> typing.Optional[windows_foundation_collections.IVector[windows_foundation.Uri]]: ...
    def get_uri_schema_array(self) -> typing.Optional[windows_foundation_collections.IVector[str]]: ...
    @_property
    def kind(self) -> IppAttributeValueKind: ...

@typing.final
class IppIntegerRange(winrt.system.Object):
    @staticmethod
    def _from(obj: winrt.system.Object, /) -> IppIntegerRange: ...
    def __new__(cls: typing.Type[IppIntegerRange], start: winrt.system.Int32, end: winrt.system.Int32) -> IppIntegerRange: ...
    @_property
    def end(self) -> winrt.system.Int32: ...
    @_property
    def start(self) -> winrt.system.Int32: ...

@typing.final
class IppPrintDevice_Static(type):
    def from_id(cls, device_id: str, /) -> typing.Optional[IppPrintDevice]: ...
    def from_printer_name(cls, printer_name: str, /) -> typing.Optional[IppPrintDevice]: ...
    def get_device_selector(cls) -> str: ...
    def is_ipp_printer(cls, printer_name: str, /) -> bool: ...

@typing.final
class IppPrintDevice(winrt.system.Object, metaclass=IppPrintDevice_Static):
    @staticmethod
    def _from(obj: winrt.system.Object, /) -> IppPrintDevice: ...
    def get_max_supported_pdf_size(self) -> winrt.system.UInt64: ...
    def get_max_supported_pdf_version(self) -> str: ...
    def get_max_supported_pdl_version(self, pdl_content_type: str, /) -> str: ...
    def get_pdl_passthrough_provider(self) -> typing.Optional[PdlPassthroughProvider]: ...
    def get_printer_attributes(self, attribute_names: typing.Iterable[str], /) -> typing.Optional[windows_foundation_collections.IMap[str, IppAttributeValue]]: ...
    def get_printer_attributes_as_buffer(self, attribute_names: typing.Iterable[str], /) -> typing.Optional[windows_storage_streams.IBuffer]: ...
    def is_pdl_passthrough_supported(self, pdl_content_type: str, /) -> bool: ...
    def refresh_print_device_capabilities(self) -> None: ...
    def set_printer_attributes(self, printer_attributes: typing.Iterable[windows_foundation_collections.IKeyValuePair[str, IppAttributeValue]], /) -> typing.Optional[IppSetAttributesResult]: ...
    def set_printer_attributes_from_buffer(self, printer_attributes_buffer: typing.Optional[windows_storage_streams.IBuffer], /) -> typing.Optional[IppSetAttributesResult]: ...
    @_property
    def printer_name(self) -> str: ...
    @_property
    def printer_uri(self) -> typing.Optional[windows_foundation.Uri]: ...
    @_property
    def is_ipp_fax_out_printer(self) -> bool: ...
    @_property
    def user_default_print_ticket(self) -> typing.Optional[windows_graphics_printing_printticket.WorkflowPrintTicket]: ...
    @user_default_print_ticket.setter
    def user_default_print_ticket(self, value: typing.Optional[windows_graphics_printing_printticket.WorkflowPrintTicket]) -> None: ...
    @_property
    def can_modify_user_default_print_ticket(self) -> bool: ...
    @_property
    def device_kind(self) -> IppPrintDeviceKind: ...

@typing.final
class IppResolution(winrt.system.Object):
    @staticmethod
    def _from(obj: winrt.system.Object, /) -> IppResolution: ...
    def __new__(cls: typing.Type[IppResolution], width: winrt.system.Int32, height: winrt.system.Int32, unit: IppResolutionUnit) -> IppResolution: ...
    @_property
    def height(self) -> winrt.system.Int32: ...
    @_property
    def unit(self) -> IppResolutionUnit: ...
    @_property
    def width(self) -> winrt.system.Int32: ...

@typing.final
class IppSetAttributesResult(winrt.system.Object):
    @staticmethod
    def _from(obj: winrt.system.Object, /) -> IppSetAttributesResult: ...
    @_property
    def attribute_errors(self) -> typing.Optional[windows_foundation_collections.IMapView[str, IppAttributeError]]: ...
    @_property
    def succeeded(self) -> bool: ...

@typing.final
class IppTextWithLanguage(winrt.system.Object):
    @staticmethod
    def _from(obj: winrt.system.Object, /) -> IppTextWithLanguage: ...
    def __new__(cls: typing.Type[IppTextWithLanguage], language: str, text: str) -> IppTextWithLanguage: ...
    @_property
    def language(self) -> str: ...
    @_property
    def value(self) -> str: ...

@typing.final
class PageConfigurationSettings(winrt.system.Object):
    @staticmethod
    def _from(obj: winrt.system.Object, /) -> PageConfigurationSettings: ...
    def __new__(cls: typing.Type[PageConfigurationSettings]) -> PageConfigurationSettings: ...
    @_property
    def size_source(self) -> PageConfigurationSource: ...
    @size_source.setter
    def size_source(self, value: PageConfigurationSource) -> None: ...
    @_property
    def orientation_source(self) -> PageConfigurationSource: ...
    @orientation_source.setter
    def orientation_source(self, value: PageConfigurationSource) -> None: ...

@typing.final
class PdlPassthroughProvider(winrt.system.Object):
    @staticmethod
    def _from(obj: winrt.system.Object, /) -> PdlPassthroughProvider: ...
    def start_print_job_with_print_ticket(self, job_name: str, pdl_content_type: str, print_ticket: typing.Optional[windows_storage_streams.IInputStream], page_configuration_settings: typing.Optional[PageConfigurationSettings], /) -> typing.Optional[PdlPassthroughTarget]: ...
    def start_print_job_with_task_options(self, job_name: str, pdl_content_type: str, task_options: typing.Optional[windows_graphics_printing.PrintTaskOptions], page_configuration_settings: typing.Optional[PageConfigurationSettings], /) -> typing.Optional[PdlPassthroughTarget]: ...
    @_property
    def supported_pdl_content_types(self) -> typing.Optional[windows_foundation_collections.IVectorView[str]]: ...

@typing.final
class PdlPassthroughTarget(winrt.system.Object):
    def __enter__(self: Self) -> Self: ...
    def __exit__(self, *args) -> None: ...
    @staticmethod
    def _from(obj: winrt.system.Object, /) -> PdlPassthroughTarget: ...
    def close(self) -> None: ...
    def get_output_stream(self) -> typing.Optional[windows_storage_streams.IOutputStream]: ...
    def submit(self) -> None: ...
    @_property
    def print_job_id(self) -> winrt.system.Int32: ...

@typing.final
class Print3DDevice_Static(type):
    def from_id_async(cls, device_id: str, /) -> windows_foundation.IAsyncOperation[Print3DDevice]: ...
    def get_device_selector(cls) -> str: ...

@typing.final
class Print3DDevice(winrt.system.Object, metaclass=Print3DDevice_Static):
    @staticmethod
    def _from(obj: winrt.system.Object, /) -> Print3DDevice: ...
    @_property
    def print_schema(self) -> typing.Optional[PrintSchema]: ...

@typing.final
class PrintSchema(winrt.system.Object):
    @staticmethod
    def _from(obj: winrt.system.Object, /) -> PrintSchema: ...
    def get_capabilities_async(self, constrain_ticket: typing.Optional[windows_storage_streams.IRandomAccessStreamWithContentType], /) -> windows_foundation.IAsyncOperation[windows_storage_streams.IRandomAccessStreamWithContentType]: ...
    def get_default_print_ticket_async(self) -> windows_foundation.IAsyncOperation[windows_storage_streams.IRandomAccessStreamWithContentType]: ...
    def merge_and_validate_with_default_print_ticket_async(self, delta_ticket: typing.Optional[windows_storage_streams.IRandomAccessStreamWithContentType], /) -> windows_foundation.IAsyncOperation[windows_storage_streams.IRandomAccessStreamWithContentType]: ...

