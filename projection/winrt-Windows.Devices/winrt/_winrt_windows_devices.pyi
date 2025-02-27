# WARNING: Please don't edit this file. It was generated by Python/WinRT v0.0.0

import datetime
import sys
import types
import typing
import uuid as _uuid
from builtins import property as _property

import winrt._winrt
import winrt.system
import winrt.windows.devices.adc.provider as windows_devices_adc_provider
import winrt.windows.devices.gpio.provider as windows_devices_gpio_provider
import winrt.windows.devices.i2c.provider as windows_devices_i2c_provider
import winrt.windows.devices.pwm.provider as windows_devices_pwm_provider
import winrt.windows.devices.spi.provider as windows_devices_spi_provider

Self = typing.TypeVar('Self')

@typing.final
class LowLevelDevicesAggregateProvider(winrt.system.Object):
    @staticmethod
    def _from(obj: winrt.system.Object, /) -> LowLevelDevicesAggregateProvider: ...
    def __new__(cls: typing.Type[LowLevelDevicesAggregateProvider], adc: typing.Optional[windows_devices_adc_provider.IAdcControllerProvider], pwm: typing.Optional[windows_devices_pwm_provider.IPwmControllerProvider], gpio: typing.Optional[windows_devices_gpio_provider.IGpioControllerProvider], i2c: typing.Optional[windows_devices_i2c_provider.II2cControllerProvider], spi: typing.Optional[windows_devices_spi_provider.ISpiControllerProvider]) -> LowLevelDevicesAggregateProvider: ...
    @_property
    def adc_controller_provider(self) -> typing.Optional[windows_devices_adc_provider.IAdcControllerProvider]: ...
    @_property
    def gpio_controller_provider(self) -> typing.Optional[windows_devices_gpio_provider.IGpioControllerProvider]: ...
    @_property
    def i2c_controller_provider(self) -> typing.Optional[windows_devices_i2c_provider.II2cControllerProvider]: ...
    @_property
    def pwm_controller_provider(self) -> typing.Optional[windows_devices_pwm_provider.IPwmControllerProvider]: ...
    @_property
    def spi_controller_provider(self) -> typing.Optional[windows_devices_spi_provider.ISpiControllerProvider]: ...

@typing.final
class LowLevelDevicesController_Static(type):
    @_property
    def default_provider(cls) -> typing.Optional[ILowLevelDevicesAggregateProvider]: ...
    @default_provider.setter
    def default_provider(cls, value: typing.Optional[ILowLevelDevicesAggregateProvider]) -> None: ...

@typing.final
class LowLevelDevicesController(winrt.system.Object, metaclass=LowLevelDevicesController_Static):
    @staticmethod
    def _from(obj: winrt.system.Object, /) -> LowLevelDevicesController: ...

@typing.final
class ILowLevelDevicesAggregateProvider(winrt.system.Object):
    @staticmethod
    def _from(obj: winrt.system.Object, /) -> ILowLevelDevicesAggregateProvider: ...
    @_property
    def adc_controller_provider(self) -> typing.Optional[windows_devices_adc_provider.IAdcControllerProvider]: ...
    @_property
    def gpio_controller_provider(self) -> typing.Optional[windows_devices_gpio_provider.IGpioControllerProvider]: ...
    @_property
    def i2c_controller_provider(self) -> typing.Optional[windows_devices_i2c_provider.II2cControllerProvider]: ...
    @_property
    def pwm_controller_provider(self) -> typing.Optional[windows_devices_pwm_provider.IPwmControllerProvider]: ...
    @_property
    def spi_controller_provider(self) -> typing.Optional[windows_devices_spi_provider.ISpiControllerProvider]: ...

