# WARNING: Please don't edit this file. It was generated by Python/WinRT v0.0.0

import datetime
import sys
import types
import typing
import uuid as _uuid
from builtins import property as _property

import winrt._winrt
import winrt.system
import winrt.windows.ui.text as windows_ui_text

Self = typing.TypeVar('Self')

@typing.final
class LanguageFont(winrt.system.Object):
    @staticmethod
    def _from(obj: winrt.system.Object, /) -> LanguageFont: ...
    @_property
    def font_family(self) -> str: ...
    @_property
    def font_stretch(self) -> windows_ui_text.FontStretch: ...
    @_property
    def font_style(self) -> windows_ui_text.FontStyle: ...
    @_property
    def font_weight(self) -> windows_ui_text.FontWeight: ...
    @_property
    def scale_factor(self) -> winrt.system.Double: ...

@typing.final
class LanguageFontGroup(winrt.system.Object):
    @staticmethod
    def _from(obj: winrt.system.Object, /) -> LanguageFontGroup: ...
    def __new__(cls: typing.Type[LanguageFontGroup], language_tag: str) -> LanguageFontGroup: ...
    @_property
    def document_alternate1_font(self) -> typing.Optional[LanguageFont]: ...
    @_property
    def document_alternate2_font(self) -> typing.Optional[LanguageFont]: ...
    @_property
    def document_heading_font(self) -> typing.Optional[LanguageFont]: ...
    @_property
    def fixed_width_text_font(self) -> typing.Optional[LanguageFont]: ...
    @_property
    def modern_document_font(self) -> typing.Optional[LanguageFont]: ...
    @_property
    def traditional_document_font(self) -> typing.Optional[LanguageFont]: ...
    @_property
    def u_i_caption_font(self) -> typing.Optional[LanguageFont]: ...
    @_property
    def u_i_heading_font(self) -> typing.Optional[LanguageFont]: ...
    @_property
    def u_i_notification_heading_font(self) -> typing.Optional[LanguageFont]: ...
    @_property
    def u_i_text_font(self) -> typing.Optional[LanguageFont]: ...
    @_property
    def u_i_title_font(self) -> typing.Optional[LanguageFont]: ...

