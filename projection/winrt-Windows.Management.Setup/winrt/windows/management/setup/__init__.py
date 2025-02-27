# WARNING: Please don't edit this file. It was generated by Python/WinRT v0.0.0

import enum
import typing
import uuid as _uuid

import winrt.system
from winrt import _winrt_windows_management_setup

__all__ = [
    "DeploymentAgentProgressState",
    "DeploymentSessionConnectionChange",
    "DeploymentSessionStateChange",
    "DeploymentWorkloadState",
    "AgentProvisioningProgressReport",
    "DeploymentSessionConnectionChangedEventArgs",
    "DeploymentSessionHeartbeatRequestedEventArgs",
    "DeploymentSessionStateChangedEventArgs",
    "DeploymentWorkload",
    "DeploymentWorkloadBatch",
    "DevicePreparationExecutionContext",
    "MachineProvisioningProgressReporter",
    "DeploymentSessionHeartbeatRequested",
]

class DeploymentAgentProgressState(enum.IntEnum):
    NOT_STARTED = 0
    INITIALIZING = 1
    IN_PROGRESS = 2
    COMPLETED = 3
    ERROR_OCCURRED = 4
    REBOOT_REQUIRED = 5
    CANCELED = 6

class DeploymentSessionConnectionChange(enum.IntEnum):
    NO_CHANGE = 0
    HOST_CONNECTION_LOST = 1
    HOST_CONNECTION_RESTORED = 2
    AGENT_CONNECTION_LOST = 3
    AGENT_CONNECTION_RESTORED = 4
    INTERNET_CONNECTION_LOST = 5
    INTERNET_CONNECTION_RESTORED = 6

class DeploymentSessionStateChange(enum.IntEnum):
    NO_CHANGE = 0
    CANCEL_REQUESTED_BY_USER = 1
    RETRY_REQUESTED_BY_USER = 2

class DeploymentWorkloadState(enum.IntEnum):
    NOT_STARTED = 0
    IN_PROGRESS = 1
    COMPLETED = 2
    FAILED = 3
    CANCELED = 4
    SKIPPED = 5
    UNINSTALLED = 6
    REBOOT_REQUIRED = 7

AgentProvisioningProgressReport = _winrt_windows_management_setup.AgentProvisioningProgressReport
DeploymentSessionConnectionChangedEventArgs = _winrt_windows_management_setup.DeploymentSessionConnectionChangedEventArgs
DeploymentSessionHeartbeatRequestedEventArgs = _winrt_windows_management_setup.DeploymentSessionHeartbeatRequestedEventArgs
DeploymentSessionStateChangedEventArgs = _winrt_windows_management_setup.DeploymentSessionStateChangedEventArgs
DeploymentWorkload = _winrt_windows_management_setup.DeploymentWorkload
DeploymentWorkloadBatch = _winrt_windows_management_setup.DeploymentWorkloadBatch
DevicePreparationExecutionContext = _winrt_windows_management_setup.DevicePreparationExecutionContext
MachineProvisioningProgressReporter = _winrt_windows_management_setup.MachineProvisioningProgressReporter
DeploymentSessionHeartbeatRequested = typing.Callable[[typing.Optional[DeploymentSessionHeartbeatRequestedEventArgs]], None]
