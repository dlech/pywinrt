# WARNING: Please don't edit this file. It was generated by Python/WinRT v0.0.0

import datetime
import sys
import types
import typing
import uuid as _uuid
from builtins import property as _property

import winrt._winrt
import winrt.system

Self = typing.TypeVar('Self')

@typing.final
class CustomXamlResourceLoader_Static(type):
    @_property
    def current(cls) -> typing.Optional[CustomXamlResourceLoader]: ...
    @current.setter
    def current(cls, value: typing.Optional[CustomXamlResourceLoader]) -> None: ...

@typing.final
class CustomXamlResourceLoader(winrt.system.Object, metaclass=CustomXamlResourceLoader_Static):
    @staticmethod
    def _from(obj: winrt.system.Object, /) -> CustomXamlResourceLoader: ...
    def __new__(cls: typing.Type[CustomXamlResourceLoader]) -> CustomXamlResourceLoader:...

