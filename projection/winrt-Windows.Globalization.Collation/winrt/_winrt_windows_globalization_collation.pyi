# WARNING: Please don't edit this file. It was generated by Python/WinRT v0.0.0

import datetime
import sys
import types
import typing
import uuid as _uuid
from builtins import property as _property

import winrt._winrt
import winrt.system
import winrt.windows.foundation.collections as windows_foundation_collections

Self = typing.TypeVar('Self')

@typing.final
class CharacterGrouping(winrt.system.Object):
    @staticmethod
    def _from(obj: winrt.system.Object, /) -> CharacterGrouping: ...
    @_property
    def first(self) -> str: ...
    @_property
    def label(self) -> str: ...

@typing.final
class CharacterGroupings(winrt.system.Object, winrt._winrt.Sequence[CharacterGrouping]):
    def __len__(self) -> int: ...
    def __iter__(self) -> windows_foundation_collections.IIterator[CharacterGrouping]: ...
    @typing.overload
    def __getitem__(self, index: typing.SupportsIndex) -> CharacterGrouping: ...
    @typing.overload
    def __getitem__(self, index: slice) -> winrt.system.Array[CharacterGrouping]: ...
    @staticmethod
    def _from(obj: winrt.system.Object, /) -> CharacterGroupings: ...
    @typing.overload
    def __new__(cls: typing.Type[CharacterGroupings], language: str) -> CharacterGroupings: ...
    @typing.overload
    def __new__(cls: typing.Type[CharacterGroupings]) -> CharacterGroupings: ...
    def first(self) -> typing.Optional[windows_foundation_collections.IIterator[CharacterGrouping]]: ...
    def get_at(self, index: winrt.system.UInt32, /) -> typing.Optional[CharacterGrouping]: ...
    def get_many(self, start_index: winrt.system.UInt32, items: typing.Union[winrt.system.Array[CharacterGrouping], winrt.system.WriteableBuffer], /) -> winrt.system.UInt32: ...
    def index_of(self, value: typing.Optional[CharacterGrouping], /) -> typing.Tuple[bool, winrt.system.UInt32]: ...
    def lookup(self, text: str, /) -> str: ...
    @_property
    def size(self) -> winrt.system.UInt32: ...

