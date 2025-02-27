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
import winrt.windows.foundation.collections as windows_foundation_collections
import winrt.windows.graphics.imaging as windows_graphics_imaging
import winrt.windows.storage as windows_storage
import winrt.windows.storage.streams as windows_storage_streams

from winrt.windows.ai.machinelearning.preview import FeatureElementKindPreview, LearningModelDeviceKindPreview, LearningModelFeatureKindPreview

Self = typing.TypeVar('Self')

@typing.final
class ImageVariableDescriptorPreview(winrt.system.Object):
    @staticmethod
    def _from(obj: winrt.system.Object, /) -> ImageVariableDescriptorPreview: ...
    @_property
    def bitmap_pixel_format(self) -> windows_graphics_imaging.BitmapPixelFormat: ...
    @_property
    def height(self) -> winrt.system.UInt32: ...
    @_property
    def width(self) -> winrt.system.UInt32: ...
    @_property
    def description(self) -> str: ...
    @_property
    def is_required(self) -> bool: ...
    @_property
    def model_feature_kind(self) -> LearningModelFeatureKindPreview: ...
    @_property
    def name(self) -> str: ...

@typing.final
class InferencingOptionsPreview(winrt.system.Object):
    @staticmethod
    def _from(obj: winrt.system.Object, /) -> InferencingOptionsPreview: ...
    @_property
    def reclaim_memory_after_evaluation(self) -> bool: ...
    @reclaim_memory_after_evaluation.setter
    def reclaim_memory_after_evaluation(self, value: bool) -> None: ...
    @_property
    def preferred_device_kind(self) -> LearningModelDeviceKindPreview: ...
    @preferred_device_kind.setter
    def preferred_device_kind(self, value: LearningModelDeviceKindPreview) -> None: ...
    @_property
    def minimize_memory_allocation(self) -> bool: ...
    @minimize_memory_allocation.setter
    def minimize_memory_allocation(self, value: bool) -> None: ...
    @_property
    def max_batch_size(self) -> winrt.system.Int32: ...
    @max_batch_size.setter
    def max_batch_size(self, value: winrt.system.Int32) -> None: ...
    @_property
    def is_tracing_enabled(self) -> bool: ...
    @is_tracing_enabled.setter
    def is_tracing_enabled(self, value: bool) -> None: ...

@typing.final
class LearningModelBindingPreview(winrt.system.Object, winrt._winrt.Mapping[str, winrt.system.Object]):
    def __len__(self) -> int: ...
    def __iter__(self) -> typing.Iterator[str]: ...
    def __contains__(self, key: object) -> bool: ...
    def __getitem__(self, key: str) -> winrt.system.Object: ...
    @staticmethod
    def _from(obj: winrt.system.Object, /) -> LearningModelBindingPreview: ...
    def __new__(cls: typing.Type[LearningModelBindingPreview], model: typing.Optional[LearningModelPreview]) -> LearningModelBindingPreview: ...
    @typing.overload
    def bind(self, name: str, value: typing.Optional[winrt.system.Object], /) -> None: ...
    @typing.overload
    def bind(self, name: str, value: typing.Optional[winrt.system.Object], metadata: typing.Optional[windows_foundation_collections.IPropertySet], /) -> None: ...
    def clear(self) -> None: ...
    def first(self) -> typing.Optional[windows_foundation_collections.IIterator[windows_foundation_collections.IKeyValuePair[str, winrt.system.Object]]]: ...
    def has_key(self, key: str, /) -> bool: ...
    def lookup(self, key: str, /) -> typing.Optional[winrt.system.Object]: ...
    def split(self) -> typing.Tuple[typing.Optional[windows_foundation_collections.IMapView[str, winrt.system.Object]], typing.Optional[windows_foundation_collections.IMapView[str, winrt.system.Object]]]: ...
    @_property
    def size(self) -> winrt.system.UInt32: ...

@typing.final
class LearningModelDescriptionPreview(winrt.system.Object):
    @staticmethod
    def _from(obj: winrt.system.Object, /) -> LearningModelDescriptionPreview: ...
    @_property
    def author(self) -> str: ...
    @_property
    def description(self) -> str: ...
    @_property
    def domain(self) -> str: ...
    @_property
    def input_features(self) -> typing.Optional[windows_foundation_collections.IIterable[ILearningModelVariableDescriptorPreview]]: ...
    @_property
    def metadata(self) -> typing.Optional[windows_foundation_collections.IMapView[str, str]]: ...
    @_property
    def name(self) -> str: ...
    @_property
    def output_features(self) -> typing.Optional[windows_foundation_collections.IIterable[ILearningModelVariableDescriptorPreview]]: ...
    @_property
    def version(self) -> winrt.system.Int64: ...

@typing.final
class LearningModelEvaluationResultPreview(winrt.system.Object):
    @staticmethod
    def _from(obj: winrt.system.Object, /) -> LearningModelEvaluationResultPreview: ...
    @_property
    def correlation_id(self) -> str: ...
    @_property
    def outputs(self) -> typing.Optional[windows_foundation_collections.IMapView[str, winrt.system.Object]]: ...

@typing.final
class LearningModelPreview_Static(type):
    def load_model_from_storage_file_async(cls, model_file: typing.Optional[windows_storage.IStorageFile], /) -> windows_foundation.IAsyncOperation[LearningModelPreview]: ...
    def load_model_from_stream_async(cls, model_stream: typing.Optional[windows_storage_streams.IRandomAccessStreamReference], /) -> windows_foundation.IAsyncOperation[LearningModelPreview]: ...

@typing.final
class LearningModelPreview(winrt.system.Object, metaclass=LearningModelPreview_Static):
    @staticmethod
    def _from(obj: winrt.system.Object, /) -> LearningModelPreview: ...
    def evaluate_async(self, binding: typing.Optional[LearningModelBindingPreview], correlation_id: str, /) -> windows_foundation.IAsyncOperation[LearningModelEvaluationResultPreview]: ...
    def evaluate_features_async(self, features: windows_foundation_collections.IMap[str, winrt.system.Object], correlation_id: str, /) -> windows_foundation.IAsyncOperation[LearningModelEvaluationResultPreview]: ...
    @_property
    def inferencing_options(self) -> typing.Optional[InferencingOptionsPreview]: ...
    @inferencing_options.setter
    def inferencing_options(self, value: typing.Optional[InferencingOptionsPreview]) -> None: ...
    @_property
    def description(self) -> typing.Optional[LearningModelDescriptionPreview]: ...

@typing.final
class LearningModelVariableDescriptorPreview(winrt.system.Object):
    @staticmethod
    def _from(obj: winrt.system.Object, /) -> LearningModelVariableDescriptorPreview: ...
    @_property
    def description(self) -> str: ...
    @_property
    def is_required(self) -> bool: ...
    @_property
    def model_feature_kind(self) -> LearningModelFeatureKindPreview: ...
    @_property
    def name(self) -> str: ...

@typing.final
class MapVariableDescriptorPreview(winrt.system.Object):
    @staticmethod
    def _from(obj: winrt.system.Object, /) -> MapVariableDescriptorPreview: ...
    @_property
    def description(self) -> str: ...
    @_property
    def is_required(self) -> bool: ...
    @_property
    def model_feature_kind(self) -> LearningModelFeatureKindPreview: ...
    @_property
    def name(self) -> str: ...
    @_property
    def fields(self) -> typing.Optional[ILearningModelVariableDescriptorPreview]: ...
    @_property
    def key_kind(self) -> FeatureElementKindPreview: ...
    @_property
    def valid_integer_keys(self) -> typing.Optional[windows_foundation_collections.IIterable[winrt.system.Int64]]: ...
    @_property
    def valid_string_keys(self) -> typing.Optional[windows_foundation_collections.IIterable[str]]: ...

@typing.final
class SequenceVariableDescriptorPreview(winrt.system.Object):
    @staticmethod
    def _from(obj: winrt.system.Object, /) -> SequenceVariableDescriptorPreview: ...
    @_property
    def description(self) -> str: ...
    @_property
    def is_required(self) -> bool: ...
    @_property
    def model_feature_kind(self) -> LearningModelFeatureKindPreview: ...
    @_property
    def name(self) -> str: ...
    @_property
    def element_type(self) -> typing.Optional[ILearningModelVariableDescriptorPreview]: ...

@typing.final
class TensorVariableDescriptorPreview(winrt.system.Object):
    @staticmethod
    def _from(obj: winrt.system.Object, /) -> TensorVariableDescriptorPreview: ...
    @_property
    def description(self) -> str: ...
    @_property
    def is_required(self) -> bool: ...
    @_property
    def model_feature_kind(self) -> LearningModelFeatureKindPreview: ...
    @_property
    def name(self) -> str: ...
    @_property
    def data_type(self) -> FeatureElementKindPreview: ...
    @_property
    def shape(self) -> typing.Optional[windows_foundation_collections.IIterable[winrt.system.Int64]]: ...

@typing.final
class ILearningModelVariableDescriptorPreview(winrt.system.Object):
    @staticmethod
    def _from(obj: winrt.system.Object, /) -> ILearningModelVariableDescriptorPreview: ...
    @_property
    def description(self) -> str: ...
    @_property
    def is_required(self) -> bool: ...
    @_property
    def model_feature_kind(self) -> LearningModelFeatureKindPreview: ...
    @_property
    def name(self) -> str: ...

