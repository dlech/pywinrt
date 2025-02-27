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

from winrt.microsoft.windows.system.power import BatteryStatus, DisplayStatus, EffectivePowerMode, EnergySaverStatus, PowerSourceKind, PowerSupplyStatus, SystemSuspendStatus, UserPresenceStatus

Self = typing.TypeVar('Self')

@typing.final
class PowerManager_Static(type):
    def add_battery_status_changed(cls, handler: windows_foundation.EventHandler[winrt.system.Object], /) -> windows_foundation.EventRegistrationToken: ...
    def remove_battery_status_changed(cls, token: windows_foundation.EventRegistrationToken, /) -> None: ...
    def add_display_status_changed(cls, handler: windows_foundation.EventHandler[winrt.system.Object], /) -> windows_foundation.EventRegistrationToken: ...
    def remove_display_status_changed(cls, token: windows_foundation.EventRegistrationToken, /) -> None: ...
    def add_effective_power_mode_changed(cls, handler: windows_foundation.EventHandler[winrt.system.Object], /) -> windows_foundation.EventRegistrationToken: ...
    def remove_effective_power_mode_changed(cls, token: windows_foundation.EventRegistrationToken, /) -> None: ...
    def add_energy_saver_status_changed(cls, handler: windows_foundation.EventHandler[winrt.system.Object], /) -> windows_foundation.EventRegistrationToken: ...
    def remove_energy_saver_status_changed(cls, token: windows_foundation.EventRegistrationToken, /) -> None: ...
    def add_power_source_kind_changed(cls, handler: windows_foundation.EventHandler[winrt.system.Object], /) -> windows_foundation.EventRegistrationToken: ...
    def remove_power_source_kind_changed(cls, token: windows_foundation.EventRegistrationToken, /) -> None: ...
    def add_power_supply_status_changed(cls, handler: windows_foundation.EventHandler[winrt.system.Object], /) -> windows_foundation.EventRegistrationToken: ...
    def remove_power_supply_status_changed(cls, token: windows_foundation.EventRegistrationToken, /) -> None: ...
    def add_remaining_charge_percent_changed(cls, handler: windows_foundation.EventHandler[winrt.system.Object], /) -> windows_foundation.EventRegistrationToken: ...
    def remove_remaining_charge_percent_changed(cls, token: windows_foundation.EventRegistrationToken, /) -> None: ...
    def add_remaining_discharge_time_changed(cls, handler: windows_foundation.EventHandler[winrt.system.Object], /) -> windows_foundation.EventRegistrationToken: ...
    def remove_remaining_discharge_time_changed(cls, token: windows_foundation.EventRegistrationToken, /) -> None: ...
    def add_system_idle_status_changed(cls, handler: windows_foundation.EventHandler[winrt.system.Object], /) -> windows_foundation.EventRegistrationToken: ...
    def remove_system_idle_status_changed(cls, token: windows_foundation.EventRegistrationToken, /) -> None: ...
    def add_system_suspend_status_changed(cls, handler: windows_foundation.EventHandler[winrt.system.Object], /) -> windows_foundation.EventRegistrationToken: ...
    def remove_system_suspend_status_changed(cls, token: windows_foundation.EventRegistrationToken, /) -> None: ...
    def add_user_presence_status_changed(cls, handler: windows_foundation.EventHandler[winrt.system.Object], /) -> windows_foundation.EventRegistrationToken: ...
    def remove_user_presence_status_changed(cls, token: windows_foundation.EventRegistrationToken, /) -> None: ...
    @_property
    def battery_status(cls) -> BatteryStatus: ...
    @_property
    def display_status(cls) -> DisplayStatus: ...
    @_property
    def effective_power_mode(cls) -> windows_foundation.IAsyncOperation[EffectivePowerMode]: ...
    @_property
    def energy_saver_status(cls) -> EnergySaverStatus: ...
    @_property
    def power_source_kind(cls) -> PowerSourceKind: ...
    @_property
    def power_supply_status(cls) -> PowerSupplyStatus: ...
    @_property
    def remaining_charge_percent(cls) -> winrt.system.Int32: ...
    @_property
    def remaining_discharge_time(cls) -> datetime.timedelta: ...
    @_property
    def system_suspend_status(cls) -> SystemSuspendStatus: ...
    @_property
    def user_presence_status(cls) -> UserPresenceStatus: ...
    @_property
    def effective_power_mode2(cls) -> EffectivePowerMode: ...

@typing.final
class PowerManager(winrt.system.Object, metaclass=PowerManager_Static):
    pass

