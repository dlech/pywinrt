# WARNING: Please don't edit this file. It was generated by Python/WinRT v0.0.0

import datetime
import sys
import types
import typing
import uuid as _uuid
from builtins import property as _property

import winrt._winrt
import winrt.system

from winrt.windows.foundation.metadata import AttributeTargets, CompositionType, DeprecationType, FeatureStage, GCPressureAmount, MarshalingType, Platform, ThreadingModel

Self = typing.TypeVar('Self')

@typing.final
class ApiInformation_Static(type):
    @typing.overload
    def is_api_contract_present(cls, contract_name: str, major_version: winrt.system.UInt16, /) -> bool: ...
    @typing.overload
    def is_api_contract_present(cls, contract_name: str, major_version: winrt.system.UInt16, minor_version: winrt.system.UInt16, /) -> bool: ...
    def is_enum_named_value_present(cls, enum_type_name: str, value_name: str, /) -> bool: ...
    def is_event_present(cls, type_name: str, event_name: str, /) -> bool: ...
    @typing.overload
    def is_method_present(cls, type_name: str, method_name: str, /) -> bool: ...
    @typing.overload
    def is_method_present(cls, type_name: str, method_name: str, input_parameter_count: winrt.system.UInt32, /) -> bool: ...
    def is_property_present(cls, type_name: str, property_name: str, /) -> bool: ...
    def is_read_only_property_present(cls, type_name: str, property_name: str, /) -> bool: ...
    def is_type_present(cls, type_name: str, /) -> bool: ...
    def is_writeable_property_present(cls, type_name: str, property_name: str, /) -> bool: ...

@typing.final
class ApiInformation(winrt.system.Object, metaclass=ApiInformation_Static):
    pass

