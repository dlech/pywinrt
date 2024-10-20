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
import winrt.windows.foundation.numerics as windows_foundation_numerics
import winrt.windows.storage.streams as windows_storage_streams
import winrt.windows.ui as windows_ui

from winrt.windows.graphics.printing3d import Print3DTaskCompletion, Print3DTaskDetail, Printing3DBufferFormat, Printing3DMeshVerificationMode, Printing3DModelUnit, Printing3DObjectType, Printing3DPackageCompression, Printing3DTextureEdgeBehavior
from winrt.windows.graphics.printing3d import Print3DTaskSourceRequestedHandler

Self = typing.TypeVar('Self')

@typing.final
class Printing3DBufferDescription:
    format: Printing3DBufferFormat
    stride: winrt.system.UInt32
    def __init__(self, format: Printing3DBufferFormat, stride: winrt.system.UInt32) -> None: ...

@typing.final
class Print3DManager_Static(type):
    def get_for_current_view(cls) -> typing.Optional[Print3DManager]: ...
    def show_print_u_i_async(cls) -> windows_foundation.IAsyncOperation[bool]: ...

@typing.final
class Print3DManager(winrt.system.Object, metaclass=Print3DManager_Static):
    @staticmethod
    def _from(obj: winrt.system.Object, /) -> Print3DManager: ...
    def add_task_requested(self, event_handler: windows_foundation.TypedEventHandler[Print3DManager, Print3DTaskRequestedEventArgs], /) -> windows_foundation.EventRegistrationToken: ...
    def remove_task_requested(self, token: windows_foundation.EventRegistrationToken, /) -> None: ...

@typing.final
class Print3DTask(winrt.system.Object):
    @staticmethod
    def _from(obj: winrt.system.Object, /) -> Print3DTask: ...
    def add_completed(self, event_handler: windows_foundation.TypedEventHandler[Print3DTask, Print3DTaskCompletedEventArgs], /) -> windows_foundation.EventRegistrationToken: ...
    def remove_completed(self, event_cookie: windows_foundation.EventRegistrationToken, /) -> None: ...
    def add_source_changed(self, event_handler: windows_foundation.TypedEventHandler[Print3DTask, Print3DTaskSourceChangedEventArgs], /) -> windows_foundation.EventRegistrationToken: ...
    def remove_source_changed(self, event_cookie: windows_foundation.EventRegistrationToken, /) -> None: ...
    def add_submitting(self, event_handler: windows_foundation.TypedEventHandler[Print3DTask, winrt.system.Object], /) -> windows_foundation.EventRegistrationToken: ...
    def remove_submitting(self, event_cookie: windows_foundation.EventRegistrationToken, /) -> None: ...
    @_property
    def source(self) -> typing.Optional[Printing3D3MFPackage]: ...

@typing.final
class Print3DTaskCompletedEventArgs(winrt.system.Object):
    @staticmethod
    def _from(obj: winrt.system.Object, /) -> Print3DTaskCompletedEventArgs: ...
    @_property
    def completion(self) -> Print3DTaskCompletion: ...
    @_property
    def extended_status(self) -> Print3DTaskDetail: ...

@typing.final
class Print3DTaskRequest(winrt.system.Object):
    @staticmethod
    def _from(obj: winrt.system.Object, /) -> Print3DTaskRequest: ...
    def create_task(self, title: str, printer_id: str, handler: typing.Optional[Print3DTaskSourceRequestedHandler], /) -> typing.Optional[Print3DTask]: ...

@typing.final
class Print3DTaskRequestedEventArgs(winrt.system.Object):
    @staticmethod
    def _from(obj: winrt.system.Object, /) -> Print3DTaskRequestedEventArgs: ...
    @_property
    def request(self) -> typing.Optional[Print3DTaskRequest]: ...

@typing.final
class Print3DTaskSourceChangedEventArgs(winrt.system.Object):
    @staticmethod
    def _from(obj: winrt.system.Object, /) -> Print3DTaskSourceChangedEventArgs: ...
    @_property
    def source(self) -> typing.Optional[Printing3D3MFPackage]: ...

@typing.final
class Print3DTaskSourceRequestedArgs(winrt.system.Object):
    @staticmethod
    def _from(obj: winrt.system.Object, /) -> Print3DTaskSourceRequestedArgs: ...
    def set_source(self, source: typing.Optional[Printing3D3MFPackage], /) -> None: ...

@typing.final
class Printing3D3MFPackage_Static(type):
    def load_async(cls, value: typing.Optional[windows_storage_streams.IRandomAccessStream], /) -> windows_foundation.IAsyncOperation[Printing3D3MFPackage]: ...

@typing.final
class Printing3D3MFPackage(winrt.system.Object, metaclass=Printing3D3MFPackage_Static):
    @staticmethod
    def _from(obj: winrt.system.Object, /) -> Printing3D3MFPackage: ...
    def __new__(cls: typing.Type[Printing3D3MFPackage]) -> Printing3D3MFPackage:...
    def load_model_from_package_async(self, value: typing.Optional[windows_storage_streams.IRandomAccessStream], /) -> windows_foundation.IAsyncOperation[Printing3DModel]: ...
    def save_async(self) -> windows_foundation.IAsyncOperation[windows_storage_streams.IRandomAccessStream]: ...
    def save_model_to_package_async(self, value: typing.Optional[Printing3DModel], /) -> windows_foundation.IAsyncAction: ...
    @_property
    def thumbnail(self) -> typing.Optional[Printing3DTextureResource]: ...
    @thumbnail.setter
    def thumbnail(self, value: typing.Optional[Printing3DTextureResource]) -> None: ...
    @_property
    def print_ticket(self) -> typing.Optional[windows_storage_streams.IRandomAccessStream]: ...
    @print_ticket.setter
    def print_ticket(self, value: typing.Optional[windows_storage_streams.IRandomAccessStream]) -> None: ...
    @_property
    def model_part(self) -> typing.Optional[windows_storage_streams.IRandomAccessStream]: ...
    @model_part.setter
    def model_part(self, value: typing.Optional[windows_storage_streams.IRandomAccessStream]) -> None: ...
    @_property
    def textures(self) -> typing.Optional[windows_foundation_collections.IVector[Printing3DTextureResource]]: ...
    @_property
    def compression(self) -> Printing3DPackageCompression: ...
    @compression.setter
    def compression(self, value: Printing3DPackageCompression) -> None: ...

@typing.final
class Printing3DBaseMaterial_Static(type):
    @_property
    def abs(cls) -> str: ...
    @_property
    def pla(cls) -> str: ...

@typing.final
class Printing3DBaseMaterial(winrt.system.Object, metaclass=Printing3DBaseMaterial_Static):
    @staticmethod
    def _from(obj: winrt.system.Object, /) -> Printing3DBaseMaterial: ...
    def __new__(cls: typing.Type[Printing3DBaseMaterial]) -> Printing3DBaseMaterial:...
    @_property
    def name(self) -> str: ...
    @name.setter
    def name(self, value: str) -> None: ...
    @_property
    def color(self) -> typing.Optional[Printing3DColorMaterial]: ...
    @color.setter
    def color(self, value: typing.Optional[Printing3DColorMaterial]) -> None: ...

@typing.final
class Printing3DBaseMaterialGroup(winrt.system.Object):
    @staticmethod
    def _from(obj: winrt.system.Object, /) -> Printing3DBaseMaterialGroup: ...
    def __new__(cls: typing.Type[Printing3DBaseMaterialGroup], material_group_id: winrt.system.UInt32) -> Printing3DBaseMaterialGroup:...
    @_property
    def bases(self) -> typing.Optional[windows_foundation_collections.IVector[Printing3DBaseMaterial]]: ...
    @_property
    def material_group_id(self) -> winrt.system.UInt32: ...

@typing.final
class Printing3DColorMaterial(winrt.system.Object):
    @staticmethod
    def _from(obj: winrt.system.Object, /) -> Printing3DColorMaterial: ...
    def __new__(cls: typing.Type[Printing3DColorMaterial]) -> Printing3DColorMaterial:...
    @_property
    def value(self) -> winrt.system.UInt32: ...
    @value.setter
    def value(self, value: winrt.system.UInt32) -> None: ...
    @_property
    def color(self) -> windows_ui.Color: ...
    @color.setter
    def color(self, value: windows_ui.Color) -> None: ...

@typing.final
class Printing3DColorMaterialGroup(winrt.system.Object):
    @staticmethod
    def _from(obj: winrt.system.Object, /) -> Printing3DColorMaterialGroup: ...
    def __new__(cls: typing.Type[Printing3DColorMaterialGroup], material_group_id: winrt.system.UInt32) -> Printing3DColorMaterialGroup:...
    @_property
    def colors(self) -> typing.Optional[windows_foundation_collections.IVector[Printing3DColorMaterial]]: ...
    @_property
    def material_group_id(self) -> winrt.system.UInt32: ...

@typing.final
class Printing3DComponent(winrt.system.Object):
    @staticmethod
    def _from(obj: winrt.system.Object, /) -> Printing3DComponent: ...
    def __new__(cls: typing.Type[Printing3DComponent]) -> Printing3DComponent:...
    @_property
    def type(self) -> Printing3DObjectType: ...
    @type.setter
    def type(self, value: Printing3DObjectType) -> None: ...
    @_property
    def thumbnail(self) -> typing.Optional[Printing3DTextureResource]: ...
    @thumbnail.setter
    def thumbnail(self, value: typing.Optional[Printing3DTextureResource]) -> None: ...
    @_property
    def part_number(self) -> str: ...
    @part_number.setter
    def part_number(self, value: str) -> None: ...
    @_property
    def name(self) -> str: ...
    @name.setter
    def name(self, value: str) -> None: ...
    @_property
    def mesh(self) -> typing.Optional[Printing3DMesh]: ...
    @mesh.setter
    def mesh(self, value: typing.Optional[Printing3DMesh]) -> None: ...
    @_property
    def components(self) -> typing.Optional[windows_foundation_collections.IVector[Printing3DComponentWithMatrix]]: ...

@typing.final
class Printing3DComponentWithMatrix(winrt.system.Object):
    @staticmethod
    def _from(obj: winrt.system.Object, /) -> Printing3DComponentWithMatrix: ...
    def __new__(cls: typing.Type[Printing3DComponentWithMatrix]) -> Printing3DComponentWithMatrix:...
    @_property
    def matrix(self) -> windows_foundation_numerics.Matrix4x4: ...
    @matrix.setter
    def matrix(self, value: windows_foundation_numerics.Matrix4x4) -> None: ...
    @_property
    def component(self) -> typing.Optional[Printing3DComponent]: ...
    @component.setter
    def component(self, value: typing.Optional[Printing3DComponent]) -> None: ...

@typing.final
class Printing3DCompositeMaterial(winrt.system.Object):
    @staticmethod
    def _from(obj: winrt.system.Object, /) -> Printing3DCompositeMaterial: ...
    def __new__(cls: typing.Type[Printing3DCompositeMaterial]) -> Printing3DCompositeMaterial:...
    @_property
    def values(self) -> typing.Optional[windows_foundation_collections.IVector[winrt.system.Double]]: ...

@typing.final
class Printing3DCompositeMaterialGroup(winrt.system.Object):
    @staticmethod
    def _from(obj: winrt.system.Object, /) -> Printing3DCompositeMaterialGroup: ...
    def __new__(cls: typing.Type[Printing3DCompositeMaterialGroup], material_group_id: winrt.system.UInt32) -> Printing3DCompositeMaterialGroup:...
    @_property
    def composites(self) -> typing.Optional[windows_foundation_collections.IVector[Printing3DCompositeMaterial]]: ...
    @_property
    def material_group_id(self) -> winrt.system.UInt32: ...
    @_property
    def material_indices(self) -> typing.Optional[windows_foundation_collections.IVector[winrt.system.UInt32]]: ...
    @_property
    def base_material_group(self) -> typing.Optional[Printing3DBaseMaterialGroup]: ...
    @base_material_group.setter
    def base_material_group(self, value: typing.Optional[Printing3DBaseMaterialGroup]) -> None: ...

@typing.final
class Printing3DFaceReductionOptions(winrt.system.Object):
    @staticmethod
    def _from(obj: winrt.system.Object, /) -> Printing3DFaceReductionOptions: ...
    def __new__(cls: typing.Type[Printing3DFaceReductionOptions]) -> Printing3DFaceReductionOptions:...
    @_property
    def target_triangle_count(self) -> winrt.system.UInt32: ...
    @target_triangle_count.setter
    def target_triangle_count(self, value: winrt.system.UInt32) -> None: ...
    @_property
    def max_reduction_area(self) -> winrt.system.Double: ...
    @max_reduction_area.setter
    def max_reduction_area(self, value: winrt.system.Double) -> None: ...
    @_property
    def max_edge_length(self) -> winrt.system.Double: ...
    @max_edge_length.setter
    def max_edge_length(self, value: winrt.system.Double) -> None: ...

@typing.final
class Printing3DMaterial(winrt.system.Object):
    @staticmethod
    def _from(obj: winrt.system.Object, /) -> Printing3DMaterial: ...
    def __new__(cls: typing.Type[Printing3DMaterial]) -> Printing3DMaterial:...
    @_property
    def base_groups(self) -> typing.Optional[windows_foundation_collections.IVector[Printing3DBaseMaterialGroup]]: ...
    @_property
    def color_groups(self) -> typing.Optional[windows_foundation_collections.IVector[Printing3DColorMaterialGroup]]: ...
    @_property
    def composite_groups(self) -> typing.Optional[windows_foundation_collections.IVector[Printing3DCompositeMaterialGroup]]: ...
    @_property
    def multiple_property_groups(self) -> typing.Optional[windows_foundation_collections.IVector[Printing3DMultiplePropertyMaterialGroup]]: ...
    @_property
    def texture2_coord_groups(self) -> typing.Optional[windows_foundation_collections.IVector[Printing3DTexture2CoordMaterialGroup]]: ...

@typing.final
class Printing3DMesh(winrt.system.Object):
    @staticmethod
    def _from(obj: winrt.system.Object, /) -> Printing3DMesh: ...
    def __new__(cls: typing.Type[Printing3DMesh]) -> Printing3DMesh:...
    def create_triangle_indices(self, value: winrt.system.UInt32, /) -> None: ...
    def create_triangle_material_indices(self, value: winrt.system.UInt32, /) -> None: ...
    def create_vertex_normals(self, value: winrt.system.UInt32, /) -> None: ...
    def create_vertex_positions(self, value: winrt.system.UInt32, /) -> None: ...
    def get_triangle_indices(self) -> typing.Optional[windows_storage_streams.IBuffer]: ...
    def get_triangle_material_indices(self) -> typing.Optional[windows_storage_streams.IBuffer]: ...
    def get_vertex_normals(self) -> typing.Optional[windows_storage_streams.IBuffer]: ...
    def get_vertex_positions(self) -> typing.Optional[windows_storage_streams.IBuffer]: ...
    def verify_async(self, value: Printing3DMeshVerificationMode, /) -> windows_foundation.IAsyncOperation[Printing3DMeshVerificationResult]: ...
    @_property
    def vertex_positions_description(self) -> Printing3DBufferDescription: ...
    @vertex_positions_description.setter
    def vertex_positions_description(self, value: Printing3DBufferDescription) -> None: ...
    @_property
    def vertex_normals_description(self) -> Printing3DBufferDescription: ...
    @vertex_normals_description.setter
    def vertex_normals_description(self, value: Printing3DBufferDescription) -> None: ...
    @_property
    def vertex_count(self) -> winrt.system.UInt32: ...
    @vertex_count.setter
    def vertex_count(self, value: winrt.system.UInt32) -> None: ...
    @_property
    def triangle_material_indices_description(self) -> Printing3DBufferDescription: ...
    @triangle_material_indices_description.setter
    def triangle_material_indices_description(self, value: Printing3DBufferDescription) -> None: ...
    @_property
    def triangle_indices_description(self) -> Printing3DBufferDescription: ...
    @triangle_indices_description.setter
    def triangle_indices_description(self, value: Printing3DBufferDescription) -> None: ...
    @_property
    def index_count(self) -> winrt.system.UInt32: ...
    @index_count.setter
    def index_count(self, value: winrt.system.UInt32) -> None: ...
    @_property
    def buffer_description_set(self) -> typing.Optional[windows_foundation_collections.IPropertySet]: ...
    @_property
    def buffer_set(self) -> typing.Optional[windows_foundation_collections.IPropertySet]: ...

@typing.final
class Printing3DMeshVerificationResult(winrt.system.Object):
    @staticmethod
    def _from(obj: winrt.system.Object, /) -> Printing3DMeshVerificationResult: ...
    @_property
    def is_valid(self) -> bool: ...
    @_property
    def nonmanifold_triangles(self) -> typing.Optional[windows_foundation_collections.IVectorView[winrt.system.UInt32]]: ...
    @_property
    def reversed_normal_triangles(self) -> typing.Optional[windows_foundation_collections.IVectorView[winrt.system.UInt32]]: ...

@typing.final
class Printing3DModel(winrt.system.Object):
    @staticmethod
    def _from(obj: winrt.system.Object, /) -> Printing3DModel: ...
    def __new__(cls: typing.Type[Printing3DModel]) -> Printing3DModel:...
    def clone(self) -> typing.Optional[Printing3DModel]: ...
    def repair_async(self) -> windows_foundation.IAsyncAction: ...
    def repair_with_progress_async(self) -> windows_foundation.IAsyncOperationWithProgress[bool, winrt.system.Double]: ...
    @typing.overload
    def try_partial_repair_async(self) -> windows_foundation.IAsyncOperation[bool]: ...
    @typing.overload
    def try_partial_repair_async(self, max_wait_time: datetime.timedelta, /) -> windows_foundation.IAsyncOperation[bool]: ...
    @typing.overload
    def try_reduce_faces_async(self) -> windows_foundation.IAsyncOperationWithProgress[bool, winrt.system.Double]: ...
    @typing.overload
    def try_reduce_faces_async(self, printing3_d_face_reduction_options: typing.Optional[Printing3DFaceReductionOptions], /) -> windows_foundation.IAsyncOperationWithProgress[bool, winrt.system.Double]: ...
    @typing.overload
    def try_reduce_faces_async(self, printing3_d_face_reduction_options: typing.Optional[Printing3DFaceReductionOptions], max_wait: datetime.timedelta, /) -> windows_foundation.IAsyncOperationWithProgress[bool, winrt.system.Double]: ...
    @_property
    def version(self) -> str: ...
    @version.setter
    def version(self, value: str) -> None: ...
    @_property
    def unit(self) -> Printing3DModelUnit: ...
    @unit.setter
    def unit(self, value: Printing3DModelUnit) -> None: ...
    @_property
    def material(self) -> typing.Optional[Printing3DMaterial]: ...
    @material.setter
    def material(self, value: typing.Optional[Printing3DMaterial]) -> None: ...
    @_property
    def build(self) -> typing.Optional[Printing3DComponent]: ...
    @build.setter
    def build(self, value: typing.Optional[Printing3DComponent]) -> None: ...
    @_property
    def components(self) -> typing.Optional[windows_foundation_collections.IVector[Printing3DComponent]]: ...
    @_property
    def meshes(self) -> typing.Optional[windows_foundation_collections.IVector[Printing3DMesh]]: ...
    @_property
    def metadata(self) -> typing.Optional[windows_foundation_collections.IMap[str, str]]: ...
    @_property
    def required_extensions(self) -> typing.Optional[windows_foundation_collections.IVector[str]]: ...
    @_property
    def textures(self) -> typing.Optional[windows_foundation_collections.IVector[Printing3DModelTexture]]: ...

@typing.final
class Printing3DModelTexture(winrt.system.Object):
    @staticmethod
    def _from(obj: winrt.system.Object, /) -> Printing3DModelTexture: ...
    def __new__(cls: typing.Type[Printing3DModelTexture]) -> Printing3DModelTexture:...
    @_property
    def tile_style_v(self) -> Printing3DTextureEdgeBehavior: ...
    @tile_style_v.setter
    def tile_style_v(self, value: Printing3DTextureEdgeBehavior) -> None: ...
    @_property
    def tile_style_u(self) -> Printing3DTextureEdgeBehavior: ...
    @tile_style_u.setter
    def tile_style_u(self, value: Printing3DTextureEdgeBehavior) -> None: ...
    @_property
    def texture_resource(self) -> typing.Optional[Printing3DTextureResource]: ...
    @texture_resource.setter
    def texture_resource(self, value: typing.Optional[Printing3DTextureResource]) -> None: ...

@typing.final
class Printing3DMultiplePropertyMaterial(winrt.system.Object):
    @staticmethod
    def _from(obj: winrt.system.Object, /) -> Printing3DMultiplePropertyMaterial: ...
    def __new__(cls: typing.Type[Printing3DMultiplePropertyMaterial]) -> Printing3DMultiplePropertyMaterial:...
    @_property
    def material_indices(self) -> typing.Optional[windows_foundation_collections.IVector[winrt.system.UInt32]]: ...

@typing.final
class Printing3DMultiplePropertyMaterialGroup(winrt.system.Object):
    @staticmethod
    def _from(obj: winrt.system.Object, /) -> Printing3DMultiplePropertyMaterialGroup: ...
    def __new__(cls: typing.Type[Printing3DMultiplePropertyMaterialGroup], material_group_id: winrt.system.UInt32) -> Printing3DMultiplePropertyMaterialGroup:...
    @_property
    def material_group_id(self) -> winrt.system.UInt32: ...
    @_property
    def material_group_indices(self) -> typing.Optional[windows_foundation_collections.IVector[winrt.system.UInt32]]: ...
    @_property
    def multiple_properties(self) -> typing.Optional[windows_foundation_collections.IVector[Printing3DMultiplePropertyMaterial]]: ...

@typing.final
class Printing3DTexture2CoordMaterial(winrt.system.Object):
    @staticmethod
    def _from(obj: winrt.system.Object, /) -> Printing3DTexture2CoordMaterial: ...
    def __new__(cls: typing.Type[Printing3DTexture2CoordMaterial]) -> Printing3DTexture2CoordMaterial:...
    @_property
    def v(self) -> winrt.system.Double: ...
    @v.setter
    def v(self, value: winrt.system.Double) -> None: ...
    @_property
    def u(self) -> winrt.system.Double: ...
    @u.setter
    def u(self, value: winrt.system.Double) -> None: ...
    @_property
    def texture(self) -> typing.Optional[Printing3DModelTexture]: ...
    @texture.setter
    def texture(self, value: typing.Optional[Printing3DModelTexture]) -> None: ...

@typing.final
class Printing3DTexture2CoordMaterialGroup(winrt.system.Object):
    @staticmethod
    def _from(obj: winrt.system.Object, /) -> Printing3DTexture2CoordMaterialGroup: ...
    def __new__(cls: typing.Type[Printing3DTexture2CoordMaterialGroup], material_group_id: winrt.system.UInt32) -> Printing3DTexture2CoordMaterialGroup:...
    @_property
    def material_group_id(self) -> winrt.system.UInt32: ...
    @_property
    def texture2_coords(self) -> typing.Optional[windows_foundation_collections.IVector[Printing3DTexture2CoordMaterial]]: ...
    @_property
    def texture(self) -> typing.Optional[Printing3DModelTexture]: ...
    @texture.setter
    def texture(self, value: typing.Optional[Printing3DModelTexture]) -> None: ...

@typing.final
class Printing3DTextureResource(winrt.system.Object):
    @staticmethod
    def _from(obj: winrt.system.Object, /) -> Printing3DTextureResource: ...
    def __new__(cls: typing.Type[Printing3DTextureResource]) -> Printing3DTextureResource:...
    @_property
    def texture_data(self) -> typing.Optional[windows_storage_streams.IRandomAccessStreamWithContentType]: ...
    @texture_data.setter
    def texture_data(self, value: typing.Optional[windows_storage_streams.IRandomAccessStreamWithContentType]) -> None: ...
    @_property
    def name(self) -> str: ...
    @name.setter
    def name(self, value: str) -> None: ...

