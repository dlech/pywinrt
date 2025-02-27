# WARNING: Please don't edit this file. It was generated by Python/WinRT v0.0.0

import datetime
import sys
import types
import typing
import uuid as _uuid
from builtins import property as _property

import winrt._winrt
import winrt.system
import winrt.windows.graphics.effects as windows_graphics_effects

from winrt.microsoft.ui.composition.effects import SceneLightingEffectReflectanceModel

Self = typing.TypeVar('Self')

@typing.final
class SceneLightingEffect(winrt.system.Object):
    @staticmethod
    def _from(obj: winrt.system.Object, /) -> SceneLightingEffect: ...
    def __new__(cls: typing.Type[SceneLightingEffect]) -> SceneLightingEffect: ...
    @_property
    def specular_shine(self) -> winrt.system.Single: ...
    @specular_shine.setter
    def specular_shine(self, value: winrt.system.Single) -> None: ...
    @_property
    def specular_amount(self) -> winrt.system.Single: ...
    @specular_amount.setter
    def specular_amount(self, value: winrt.system.Single) -> None: ...
    @_property
    def normal_map_source(self) -> typing.Optional[windows_graphics_effects.IGraphicsEffectSource]: ...
    @normal_map_source.setter
    def normal_map_source(self, value: typing.Optional[windows_graphics_effects.IGraphicsEffectSource]) -> None: ...
    @_property
    def diffuse_amount(self) -> winrt.system.Single: ...
    @diffuse_amount.setter
    def diffuse_amount(self, value: winrt.system.Single) -> None: ...
    @_property
    def ambient_amount(self) -> winrt.system.Single: ...
    @ambient_amount.setter
    def ambient_amount(self, value: winrt.system.Single) -> None: ...
    @_property
    def reflectance_model(self) -> SceneLightingEffectReflectanceModel: ...
    @reflectance_model.setter
    def reflectance_model(self, value: SceneLightingEffectReflectanceModel) -> None: ...
    @_property
    def name(self) -> str: ...
    @name.setter
    def name(self, value: str) -> None: ...

