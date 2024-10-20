# WARNING: Please don't edit this file. It was generated by Python/WinRT v0.0.0

import enum
import typing
import uuid as _uuid

import winrt.system
from winrt import _winrt_windows_ui_xaml_input

__all__ = [
    "FocusInputDeviceKind",
    "FocusNavigationDirection",
    "InputScopeNameValue",
    "KeyTipPlacementMode",
    "KeyboardAcceleratorPlacementMode",
    "KeyboardNavigationMode",
    "ManipulationModes",
    "StandardUICommandKind",
    "XYFocusKeyboardNavigationMode",
    "XYFocusNavigationStrategy",
    "XYFocusNavigationStrategyOverride",
    "AccessKeyDisplayDismissedEventArgs",
    "AccessKeyDisplayRequestedEventArgs",
    "AccessKeyInvokedEventArgs",
    "AccessKeyManager",
    "CanExecuteRequestedEventArgs",
    "CharacterReceivedRoutedEventArgs",
    "ContextRequestedEventArgs",
    "DoubleTappedRoutedEventArgs",
    "ExecuteRequestedEventArgs",
    "FindNextElementOptions",
    "FocusManager",
    "FocusManagerGotFocusEventArgs",
    "FocusManagerLostFocusEventArgs",
    "FocusMovementResult",
    "GettingFocusEventArgs",
    "HoldingRoutedEventArgs",
    "InertiaExpansionBehavior",
    "InertiaRotationBehavior",
    "InertiaTranslationBehavior",
    "InputScope",
    "InputScopeName",
    "KeyRoutedEventArgs",
    "KeyboardAccelerator",
    "KeyboardAcceleratorInvokedEventArgs",
    "LosingFocusEventArgs",
    "ManipulationCompletedRoutedEventArgs",
    "ManipulationDeltaRoutedEventArgs",
    "ManipulationInertiaStartingRoutedEventArgs",
    "ManipulationPivot",
    "ManipulationStartedRoutedEventArgs",
    "ManipulationStartingRoutedEventArgs",
    "NoFocusCandidateFoundEventArgs",
    "Pointer",
    "PointerRoutedEventArgs",
    "ProcessKeyboardAcceleratorEventArgs",
    "RightTappedRoutedEventArgs",
    "StandardUICommand",
    "TappedRoutedEventArgs",
    "XamlUICommand",
    "ICommand",
    "DoubleTappedEventHandler",
    "HoldingEventHandler",
    "KeyEventHandler",
    "ManipulationCompletedEventHandler",
    "ManipulationDeltaEventHandler",
    "ManipulationInertiaStartingEventHandler",
    "ManipulationStartedEventHandler",
    "ManipulationStartingEventHandler",
    "PointerEventHandler",
    "RightTappedEventHandler",
    "TappedEventHandler",
]

class FocusInputDeviceKind(enum.IntEnum):
    NONE = 0
    MOUSE = 1
    TOUCH = 2
    PEN = 3
    KEYBOARD = 4
    GAME_CONTROLLER = 5

class FocusNavigationDirection(enum.IntEnum):
    NEXT = 0
    PREVIOUS = 1
    UP = 2
    DOWN = 3
    LEFT = 4
    RIGHT = 5
    NONE = 6

class InputScopeNameValue(enum.IntEnum):
    DEFAULT = 0
    URL = 1
    EMAIL_SMTP_ADDRESS = 5
    PERSONAL_FULL_NAME = 7
    CURRENCY_AMOUNT_AND_SYMBOL = 20
    CURRENCY_AMOUNT = 21
    DATE_MONTH_NUMBER = 23
    DATE_DAY_NUMBER = 24
    DATE_YEAR = 25
    DIGITS = 28
    NUMBER = 29
    PASSWORD = 31
    TELEPHONE_NUMBER = 32
    TELEPHONE_COUNTRY_CODE = 33
    TELEPHONE_AREA_CODE = 34
    TELEPHONE_LOCAL_NUMBER = 35
    TIME_HOUR = 37
    TIME_MINUTES_OR_SECONDS = 38
    NUMBER_FULL_WIDTH = 39
    ALPHANUMERIC_HALF_WIDTH = 40
    ALPHANUMERIC_FULL_WIDTH = 41
    HIRAGANA = 44
    KATAKANA_HALF_WIDTH = 45
    KATAKANA_FULL_WIDTH = 46
    HANJA = 47
    HANGUL_HALF_WIDTH = 48
    HANGUL_FULL_WIDTH = 49
    SEARCH = 50
    FORMULA = 51
    SEARCH_INCREMENTAL = 52
    CHINESE_HALF_WIDTH = 53
    CHINESE_FULL_WIDTH = 54
    NATIVE_SCRIPT = 55
    TEXT = 57
    CHAT = 58
    NAME_OR_PHONE_NUMBER = 59
    EMAIL_NAME_OR_ADDRESS = 60
    PRIVATE = 61
    MAPS = 62
    NUMERIC_PASSWORD = 63
    NUMERIC_PIN = 64
    ALPHANUMERIC_PIN = 65
    FORMULA_NUMBER = 67
    CHAT_WITHOUT_EMOJI = 68

class KeyTipPlacementMode(enum.IntEnum):
    AUTO = 0
    BOTTOM = 1
    TOP = 2
    LEFT = 3
    RIGHT = 4
    CENTER = 5
    HIDDEN = 6

class KeyboardAcceleratorPlacementMode(enum.IntEnum):
    AUTO = 0
    HIDDEN = 1

class KeyboardNavigationMode(enum.IntEnum):
    LOCAL = 0
    CYCLE = 1
    ONCE = 2

class ManipulationModes(enum.IntFlag):
    NONE = 0
    TRANSLATE_X = 0x1
    TRANSLATE_Y = 0x2
    TRANSLATE_RAILS_X = 0x4
    TRANSLATE_RAILS_Y = 0x8
    ROTATE = 0x10
    SCALE = 0x20
    TRANSLATE_INERTIA = 0x40
    ROTATE_INERTIA = 0x80
    SCALE_INERTIA = 0x100
    ALL = 0xffff
    SYSTEM = 0x10000

class StandardUICommandKind(enum.IntEnum):
    NONE = 0
    CUT = 1
    COPY = 2
    PASTE = 3
    SELECT_ALL = 4
    DELETE = 5
    SHARE = 6
    SAVE = 7
    OPEN = 8
    CLOSE = 9
    PAUSE = 10
    PLAY = 11
    STOP = 12
    FORWARD = 13
    BACKWARD = 14
    UNDO = 15
    REDO = 16

class XYFocusKeyboardNavigationMode(enum.IntEnum):
    AUTO = 0
    ENABLED = 1
    DISABLED = 2

class XYFocusNavigationStrategy(enum.IntEnum):
    AUTO = 0
    PROJECTION = 1
    NAVIGATION_DIRECTION_DISTANCE = 2
    RECTILINEAR_DISTANCE = 3

class XYFocusNavigationStrategyOverride(enum.IntEnum):
    NONE = 0
    AUTO = 1
    PROJECTION = 2
    NAVIGATION_DIRECTION_DISTANCE = 3
    RECTILINEAR_DISTANCE = 4

AccessKeyDisplayDismissedEventArgs = _winrt_windows_ui_xaml_input.AccessKeyDisplayDismissedEventArgs
AccessKeyDisplayRequestedEventArgs = _winrt_windows_ui_xaml_input.AccessKeyDisplayRequestedEventArgs
AccessKeyInvokedEventArgs = _winrt_windows_ui_xaml_input.AccessKeyInvokedEventArgs
AccessKeyManager = _winrt_windows_ui_xaml_input.AccessKeyManager
CanExecuteRequestedEventArgs = _winrt_windows_ui_xaml_input.CanExecuteRequestedEventArgs
CharacterReceivedRoutedEventArgs = _winrt_windows_ui_xaml_input.CharacterReceivedRoutedEventArgs
ContextRequestedEventArgs = _winrt_windows_ui_xaml_input.ContextRequestedEventArgs
DoubleTappedRoutedEventArgs = _winrt_windows_ui_xaml_input.DoubleTappedRoutedEventArgs
ExecuteRequestedEventArgs = _winrt_windows_ui_xaml_input.ExecuteRequestedEventArgs
FindNextElementOptions = _winrt_windows_ui_xaml_input.FindNextElementOptions
FocusManager = _winrt_windows_ui_xaml_input.FocusManager
FocusManagerGotFocusEventArgs = _winrt_windows_ui_xaml_input.FocusManagerGotFocusEventArgs
FocusManagerLostFocusEventArgs = _winrt_windows_ui_xaml_input.FocusManagerLostFocusEventArgs
FocusMovementResult = _winrt_windows_ui_xaml_input.FocusMovementResult
GettingFocusEventArgs = _winrt_windows_ui_xaml_input.GettingFocusEventArgs
HoldingRoutedEventArgs = _winrt_windows_ui_xaml_input.HoldingRoutedEventArgs
InertiaExpansionBehavior = _winrt_windows_ui_xaml_input.InertiaExpansionBehavior
InertiaRotationBehavior = _winrt_windows_ui_xaml_input.InertiaRotationBehavior
InertiaTranslationBehavior = _winrt_windows_ui_xaml_input.InertiaTranslationBehavior
InputScope = _winrt_windows_ui_xaml_input.InputScope
InputScopeName = _winrt_windows_ui_xaml_input.InputScopeName
KeyRoutedEventArgs = _winrt_windows_ui_xaml_input.KeyRoutedEventArgs
KeyboardAccelerator = _winrt_windows_ui_xaml_input.KeyboardAccelerator
KeyboardAcceleratorInvokedEventArgs = _winrt_windows_ui_xaml_input.KeyboardAcceleratorInvokedEventArgs
LosingFocusEventArgs = _winrt_windows_ui_xaml_input.LosingFocusEventArgs
ManipulationCompletedRoutedEventArgs = _winrt_windows_ui_xaml_input.ManipulationCompletedRoutedEventArgs
ManipulationDeltaRoutedEventArgs = _winrt_windows_ui_xaml_input.ManipulationDeltaRoutedEventArgs
ManipulationInertiaStartingRoutedEventArgs = _winrt_windows_ui_xaml_input.ManipulationInertiaStartingRoutedEventArgs
ManipulationPivot = _winrt_windows_ui_xaml_input.ManipulationPivot
ManipulationStartedRoutedEventArgs = _winrt_windows_ui_xaml_input.ManipulationStartedRoutedEventArgs
ManipulationStartingRoutedEventArgs = _winrt_windows_ui_xaml_input.ManipulationStartingRoutedEventArgs
NoFocusCandidateFoundEventArgs = _winrt_windows_ui_xaml_input.NoFocusCandidateFoundEventArgs
Pointer = _winrt_windows_ui_xaml_input.Pointer
PointerRoutedEventArgs = _winrt_windows_ui_xaml_input.PointerRoutedEventArgs
ProcessKeyboardAcceleratorEventArgs = _winrt_windows_ui_xaml_input.ProcessKeyboardAcceleratorEventArgs
RightTappedRoutedEventArgs = _winrt_windows_ui_xaml_input.RightTappedRoutedEventArgs
StandardUICommand = _winrt_windows_ui_xaml_input.StandardUICommand
TappedRoutedEventArgs = _winrt_windows_ui_xaml_input.TappedRoutedEventArgs
XamlUICommand = _winrt_windows_ui_xaml_input.XamlUICommand
ICommand = _winrt_windows_ui_xaml_input.ICommand
DoubleTappedEventHandler = typing.Callable[[typing.Optional[winrt.system.Object], typing.Optional[DoubleTappedRoutedEventArgs]], None]
HoldingEventHandler = typing.Callable[[typing.Optional[winrt.system.Object], typing.Optional[HoldingRoutedEventArgs]], None]
KeyEventHandler = typing.Callable[[typing.Optional[winrt.system.Object], typing.Optional[KeyRoutedEventArgs]], None]
ManipulationCompletedEventHandler = typing.Callable[[typing.Optional[winrt.system.Object], typing.Optional[ManipulationCompletedRoutedEventArgs]], None]
ManipulationDeltaEventHandler = typing.Callable[[typing.Optional[winrt.system.Object], typing.Optional[ManipulationDeltaRoutedEventArgs]], None]
ManipulationInertiaStartingEventHandler = typing.Callable[[typing.Optional[winrt.system.Object], typing.Optional[ManipulationInertiaStartingRoutedEventArgs]], None]
ManipulationStartedEventHandler = typing.Callable[[typing.Optional[winrt.system.Object], typing.Optional[ManipulationStartedRoutedEventArgs]], None]
ManipulationStartingEventHandler = typing.Callable[[typing.Optional[winrt.system.Object], typing.Optional[ManipulationStartingRoutedEventArgs]], None]
PointerEventHandler = typing.Callable[[typing.Optional[winrt.system.Object], typing.Optional[PointerRoutedEventArgs]], None]
RightTappedEventHandler = typing.Callable[[typing.Optional[winrt.system.Object], typing.Optional[RightTappedRoutedEventArgs]], None]
TappedEventHandler = typing.Callable[[typing.Optional[winrt.system.Object], typing.Optional[TappedRoutedEventArgs]], None]
