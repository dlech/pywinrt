# WARNING: Please don't edit this file. It was generated by Python/WinRT v0.0.0

import enum

import winrt.system
from winrt import _winrt_windows_networking

__all__ = [
    "DomainNameType",
    "HostNameSortOptions",
    "HostNameType",
    "EndpointPair",
    "HostName",
]

class DomainNameType(enum.IntEnum):
    SUFFIX = 0
    FULLY_QUALIFIED = 1

class HostNameSortOptions(enum.IntFlag):
    NONE = 0x0
    OPTIMIZE_FOR_LONG_CONNECTIONS = 0x2

class HostNameType(enum.IntEnum):
    DOMAIN_NAME = 0
    IPV4 = 1
    IPV6 = 2
    BLUETOOTH = 3

EndpointPair = _winrt_windows_networking.EndpointPair
HostName = _winrt_windows_networking.HostName
