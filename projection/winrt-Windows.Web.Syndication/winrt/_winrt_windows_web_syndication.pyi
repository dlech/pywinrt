# WARNING: Please don't edit this file. It was generated by Python/WinRT v0.0.0

import datetime
import sys
import types
import typing
import uuid as _uuid
from builtins import property as _property

import winrt._winrt
import winrt.system
import winrt.windows.data.xml.dom as windows_data_xml_dom
import winrt.windows.foundation as windows_foundation
import winrt.windows.foundation.collections as windows_foundation_collections
import winrt.windows.security.credentials as windows_security_credentials

from winrt.windows.web.syndication import SyndicationErrorStatus, SyndicationFormat, SyndicationTextType

Self = typing.TypeVar('Self')

@typing.final
class RetrievalProgress:
    bytes_retrieved: winrt.system.UInt32
    total_bytes_to_retrieve: winrt.system.UInt32
    def __init__(self, bytes_retrieved: winrt.system.UInt32, total_bytes_to_retrieve: winrt.system.UInt32) -> None: ...

@typing.final
class TransferProgress:
    bytes_sent: winrt.system.UInt32
    total_bytes_to_send: winrt.system.UInt32
    bytes_retrieved: winrt.system.UInt32
    total_bytes_to_retrieve: winrt.system.UInt32
    def __init__(self, bytes_sent: winrt.system.UInt32, total_bytes_to_send: winrt.system.UInt32, bytes_retrieved: winrt.system.UInt32, total_bytes_to_retrieve: winrt.system.UInt32) -> None: ...

@typing.final
class SyndicationAttribute(winrt.system.Object):
    @staticmethod
    def _from(obj: winrt.system.Object, /) -> SyndicationAttribute: ...
    @typing.overload
    def __new__(cls: typing.Type[SyndicationAttribute], attribute_name: str, attribute_namespace: str, attribute_value: str) -> SyndicationAttribute: ...
    @typing.overload
    def __new__(cls: typing.Type[SyndicationAttribute]) -> SyndicationAttribute: ...
    @_property
    def value(self) -> str: ...
    @value.setter
    def value(self, value: str) -> None: ...
    @_property
    def namespace(self) -> str: ...
    @namespace.setter
    def namespace(self, value: str) -> None: ...
    @_property
    def name(self) -> str: ...
    @name.setter
    def name(self, value: str) -> None: ...

@typing.final
class SyndicationCategory(winrt.system.Object):
    @staticmethod
    def _from(obj: winrt.system.Object, /) -> SyndicationCategory: ...
    @typing.overload
    def __new__(cls: typing.Type[SyndicationCategory], term: str) -> SyndicationCategory: ...
    @typing.overload
    def __new__(cls: typing.Type[SyndicationCategory], term: str, scheme: str, label: str) -> SyndicationCategory: ...
    @typing.overload
    def __new__(cls: typing.Type[SyndicationCategory]) -> SyndicationCategory: ...
    def get_xml_document(self, format: SyndicationFormat, /) -> typing.Optional[windows_data_xml_dom.XmlDocument]: ...
    @_property
    def term(self) -> str: ...
    @term.setter
    def term(self, value: str) -> None: ...
    @_property
    def scheme(self) -> str: ...
    @scheme.setter
    def scheme(self, value: str) -> None: ...
    @_property
    def label(self) -> str: ...
    @label.setter
    def label(self, value: str) -> None: ...
    @_property
    def node_value(self) -> str: ...
    @node_value.setter
    def node_value(self, value: str) -> None: ...
    @_property
    def node_namespace(self) -> str: ...
    @node_namespace.setter
    def node_namespace(self, value: str) -> None: ...
    @_property
    def node_name(self) -> str: ...
    @node_name.setter
    def node_name(self, value: str) -> None: ...
    @_property
    def language(self) -> str: ...
    @language.setter
    def language(self, value: str) -> None: ...
    @_property
    def base_uri(self) -> typing.Optional[windows_foundation.Uri]: ...
    @base_uri.setter
    def base_uri(self, value: typing.Optional[windows_foundation.Uri]) -> None: ...
    @_property
    def attribute_extensions(self) -> typing.Optional[windows_foundation_collections.IVector[SyndicationAttribute]]: ...
    @_property
    def element_extensions(self) -> typing.Optional[windows_foundation_collections.IVector[ISyndicationNode]]: ...

@typing.final
class SyndicationClient(winrt.system.Object):
    @staticmethod
    def _from(obj: winrt.system.Object, /) -> SyndicationClient: ...
    @typing.overload
    def __new__(cls: typing.Type[SyndicationClient], server_credential: typing.Optional[windows_security_credentials.PasswordCredential]) -> SyndicationClient: ...
    @typing.overload
    def __new__(cls: typing.Type[SyndicationClient]) -> SyndicationClient: ...
    def retrieve_feed_async(self, uri: typing.Optional[windows_foundation.Uri], /) -> windows_foundation.IAsyncOperationWithProgress[SyndicationFeed, RetrievalProgress]: ...
    def set_request_header(self, name: str, value: str, /) -> None: ...
    @_property
    def timeout(self) -> winrt.system.UInt32: ...
    @timeout.setter
    def timeout(self, value: winrt.system.UInt32) -> None: ...
    @_property
    def server_credential(self) -> typing.Optional[windows_security_credentials.PasswordCredential]: ...
    @server_credential.setter
    def server_credential(self, value: typing.Optional[windows_security_credentials.PasswordCredential]) -> None: ...
    @_property
    def proxy_credential(self) -> typing.Optional[windows_security_credentials.PasswordCredential]: ...
    @proxy_credential.setter
    def proxy_credential(self, value: typing.Optional[windows_security_credentials.PasswordCredential]) -> None: ...
    @_property
    def max_response_buffer_size(self) -> winrt.system.UInt32: ...
    @max_response_buffer_size.setter
    def max_response_buffer_size(self, value: winrt.system.UInt32) -> None: ...
    @_property
    def bypass_cache_on_retrieve(self) -> bool: ...
    @bypass_cache_on_retrieve.setter
    def bypass_cache_on_retrieve(self, value: bool) -> None: ...

@typing.final
class SyndicationContent(winrt.system.Object):
    @staticmethod
    def _from(obj: winrt.system.Object, /) -> SyndicationContent: ...
    @typing.overload
    def __new__(cls: typing.Type[SyndicationContent], text: str, type: SyndicationTextType) -> SyndicationContent: ...
    @typing.overload
    def __new__(cls: typing.Type[SyndicationContent], source_uri: typing.Optional[windows_foundation.Uri]) -> SyndicationContent: ...
    @typing.overload
    def __new__(cls: typing.Type[SyndicationContent]) -> SyndicationContent: ...
    def get_xml_document(self, format: SyndicationFormat, /) -> typing.Optional[windows_data_xml_dom.XmlDocument]: ...
    @_property
    def source_uri(self) -> typing.Optional[windows_foundation.Uri]: ...
    @source_uri.setter
    def source_uri(self, value: typing.Optional[windows_foundation.Uri]) -> None: ...
    @_property
    def node_value(self) -> str: ...
    @node_value.setter
    def node_value(self, value: str) -> None: ...
    @_property
    def base_uri(self) -> typing.Optional[windows_foundation.Uri]: ...
    @base_uri.setter
    def base_uri(self, value: typing.Optional[windows_foundation.Uri]) -> None: ...
    @_property
    def language(self) -> str: ...
    @language.setter
    def language(self, value: str) -> None: ...
    @_property
    def node_name(self) -> str: ...
    @node_name.setter
    def node_name(self, value: str) -> None: ...
    @_property
    def node_namespace(self) -> str: ...
    @node_namespace.setter
    def node_namespace(self, value: str) -> None: ...
    @_property
    def attribute_extensions(self) -> typing.Optional[windows_foundation_collections.IVector[SyndicationAttribute]]: ...
    @_property
    def element_extensions(self) -> typing.Optional[windows_foundation_collections.IVector[ISyndicationNode]]: ...
    @_property
    def text(self) -> str: ...
    @text.setter
    def text(self, value: str) -> None: ...
    @_property
    def type(self) -> str: ...
    @type.setter
    def type(self, value: str) -> None: ...
    @_property
    def xml(self) -> typing.Optional[windows_data_xml_dom.XmlDocument]: ...
    @xml.setter
    def xml(self, value: typing.Optional[windows_data_xml_dom.XmlDocument]) -> None: ...

@typing.final
class SyndicationError_Static(type):
    def get_status(cls, hresult: winrt.system.Int32, /) -> SyndicationErrorStatus: ...

@typing.final
class SyndicationError(winrt.system.Object, metaclass=SyndicationError_Static):
    pass

@typing.final
class SyndicationFeed(winrt.system.Object):
    @staticmethod
    def _from(obj: winrt.system.Object, /) -> SyndicationFeed: ...
    @typing.overload
    def __new__(cls: typing.Type[SyndicationFeed], title: str, subtitle: str, uri: typing.Optional[windows_foundation.Uri]) -> SyndicationFeed: ...
    @typing.overload
    def __new__(cls: typing.Type[SyndicationFeed]) -> SyndicationFeed: ...
    def get_xml_document(self, format: SyndicationFormat, /) -> typing.Optional[windows_data_xml_dom.XmlDocument]: ...
    def load(self, feed: str, /) -> None: ...
    def load_from_xml(self, feed_document: typing.Optional[windows_data_xml_dom.XmlDocument], /) -> None: ...
    @_property
    def title(self) -> typing.Optional[ISyndicationText]: ...
    @title.setter
    def title(self, value: typing.Optional[ISyndicationText]) -> None: ...
    @_property
    def subtitle(self) -> typing.Optional[ISyndicationText]: ...
    @subtitle.setter
    def subtitle(self, value: typing.Optional[ISyndicationText]) -> None: ...
    @_property
    def rights(self) -> typing.Optional[ISyndicationText]: ...
    @rights.setter
    def rights(self, value: typing.Optional[ISyndicationText]) -> None: ...
    @_property
    def generator(self) -> typing.Optional[SyndicationGenerator]: ...
    @generator.setter
    def generator(self, value: typing.Optional[SyndicationGenerator]) -> None: ...
    @_property
    def last_updated_time(self) -> datetime.datetime: ...
    @last_updated_time.setter
    def last_updated_time(self, value: datetime.datetime) -> None: ...
    @_property
    def image_uri(self) -> typing.Optional[windows_foundation.Uri]: ...
    @image_uri.setter
    def image_uri(self, value: typing.Optional[windows_foundation.Uri]) -> None: ...
    @_property
    def icon_uri(self) -> typing.Optional[windows_foundation.Uri]: ...
    @icon_uri.setter
    def icon_uri(self, value: typing.Optional[windows_foundation.Uri]) -> None: ...
    @_property
    def id(self) -> str: ...
    @id.setter
    def id(self, value: str) -> None: ...
    @_property
    def first_uri(self) -> typing.Optional[windows_foundation.Uri]: ...
    @_property
    def items(self) -> typing.Optional[windows_foundation_collections.IVector[SyndicationItem]]: ...
    @_property
    def last_uri(self) -> typing.Optional[windows_foundation.Uri]: ...
    @_property
    def links(self) -> typing.Optional[windows_foundation_collections.IVector[SyndicationLink]]: ...
    @_property
    def next_uri(self) -> typing.Optional[windows_foundation.Uri]: ...
    @_property
    def previous_uri(self) -> typing.Optional[windows_foundation.Uri]: ...
    @_property
    def categories(self) -> typing.Optional[windows_foundation_collections.IVector[SyndicationCategory]]: ...
    @_property
    def source_format(self) -> SyndicationFormat: ...
    @_property
    def contributors(self) -> typing.Optional[windows_foundation_collections.IVector[SyndicationPerson]]: ...
    @_property
    def authors(self) -> typing.Optional[windows_foundation_collections.IVector[SyndicationPerson]]: ...
    @_property
    def node_value(self) -> str: ...
    @node_value.setter
    def node_value(self, value: str) -> None: ...
    @_property
    def node_namespace(self) -> str: ...
    @node_namespace.setter
    def node_namespace(self, value: str) -> None: ...
    @_property
    def node_name(self) -> str: ...
    @node_name.setter
    def node_name(self, value: str) -> None: ...
    @_property
    def language(self) -> str: ...
    @language.setter
    def language(self, value: str) -> None: ...
    @_property
    def base_uri(self) -> typing.Optional[windows_foundation.Uri]: ...
    @base_uri.setter
    def base_uri(self, value: typing.Optional[windows_foundation.Uri]) -> None: ...
    @_property
    def attribute_extensions(self) -> typing.Optional[windows_foundation_collections.IVector[SyndicationAttribute]]: ...
    @_property
    def element_extensions(self) -> typing.Optional[windows_foundation_collections.IVector[ISyndicationNode]]: ...

@typing.final
class SyndicationGenerator(winrt.system.Object):
    @staticmethod
    def _from(obj: winrt.system.Object, /) -> SyndicationGenerator: ...
    @typing.overload
    def __new__(cls: typing.Type[SyndicationGenerator], text: str) -> SyndicationGenerator: ...
    @typing.overload
    def __new__(cls: typing.Type[SyndicationGenerator]) -> SyndicationGenerator: ...
    def get_xml_document(self, format: SyndicationFormat, /) -> typing.Optional[windows_data_xml_dom.XmlDocument]: ...
    @_property
    def version(self) -> str: ...
    @version.setter
    def version(self, value: str) -> None: ...
    @_property
    def uri(self) -> typing.Optional[windows_foundation.Uri]: ...
    @uri.setter
    def uri(self, value: typing.Optional[windows_foundation.Uri]) -> None: ...
    @_property
    def text(self) -> str: ...
    @text.setter
    def text(self, value: str) -> None: ...
    @_property
    def node_value(self) -> str: ...
    @node_value.setter
    def node_value(self, value: str) -> None: ...
    @_property
    def node_namespace(self) -> str: ...
    @node_namespace.setter
    def node_namespace(self, value: str) -> None: ...
    @_property
    def node_name(self) -> str: ...
    @node_name.setter
    def node_name(self, value: str) -> None: ...
    @_property
    def language(self) -> str: ...
    @language.setter
    def language(self, value: str) -> None: ...
    @_property
    def base_uri(self) -> typing.Optional[windows_foundation.Uri]: ...
    @base_uri.setter
    def base_uri(self, value: typing.Optional[windows_foundation.Uri]) -> None: ...
    @_property
    def attribute_extensions(self) -> typing.Optional[windows_foundation_collections.IVector[SyndicationAttribute]]: ...
    @_property
    def element_extensions(self) -> typing.Optional[windows_foundation_collections.IVector[ISyndicationNode]]: ...

@typing.final
class SyndicationItem(winrt.system.Object):
    @staticmethod
    def _from(obj: winrt.system.Object, /) -> SyndicationItem: ...
    @typing.overload
    def __new__(cls: typing.Type[SyndicationItem], title: str, content: typing.Optional[SyndicationContent], uri: typing.Optional[windows_foundation.Uri]) -> SyndicationItem: ...
    @typing.overload
    def __new__(cls: typing.Type[SyndicationItem]) -> SyndicationItem: ...
    def get_xml_document(self, format: SyndicationFormat, /) -> typing.Optional[windows_data_xml_dom.XmlDocument]: ...
    def load(self, item: str, /) -> None: ...
    def load_from_xml(self, item_document: typing.Optional[windows_data_xml_dom.XmlDocument], /) -> None: ...
    @_property
    def title(self) -> typing.Optional[ISyndicationText]: ...
    @title.setter
    def title(self, value: typing.Optional[ISyndicationText]) -> None: ...
    @_property
    def source(self) -> typing.Optional[SyndicationFeed]: ...
    @source.setter
    def source(self, value: typing.Optional[SyndicationFeed]) -> None: ...
    @_property
    def rights(self) -> typing.Optional[ISyndicationText]: ...
    @rights.setter
    def rights(self, value: typing.Optional[ISyndicationText]) -> None: ...
    @_property
    def summary(self) -> typing.Optional[ISyndicationText]: ...
    @summary.setter
    def summary(self, value: typing.Optional[ISyndicationText]) -> None: ...
    @_property
    def published_date(self) -> datetime.datetime: ...
    @published_date.setter
    def published_date(self, value: datetime.datetime) -> None: ...
    @_property
    def comments_uri(self) -> typing.Optional[windows_foundation.Uri]: ...
    @comments_uri.setter
    def comments_uri(self, value: typing.Optional[windows_foundation.Uri]) -> None: ...
    @_property
    def id(self) -> str: ...
    @id.setter
    def id(self, value: str) -> None: ...
    @_property
    def last_updated_time(self) -> datetime.datetime: ...
    @last_updated_time.setter
    def last_updated_time(self, value: datetime.datetime) -> None: ...
    @_property
    def content(self) -> typing.Optional[SyndicationContent]: ...
    @content.setter
    def content(self, value: typing.Optional[SyndicationContent]) -> None: ...
    @_property
    def edit_uri(self) -> typing.Optional[windows_foundation.Uri]: ...
    @_property
    def links(self) -> typing.Optional[windows_foundation_collections.IVector[SyndicationLink]]: ...
    @_property
    def authors(self) -> typing.Optional[windows_foundation_collections.IVector[SyndicationPerson]]: ...
    @_property
    def categories(self) -> typing.Optional[windows_foundation_collections.IVector[SyndicationCategory]]: ...
    @_property
    def contributors(self) -> typing.Optional[windows_foundation_collections.IVector[SyndicationPerson]]: ...
    @_property
    def item_uri(self) -> typing.Optional[windows_foundation.Uri]: ...
    @_property
    def e_tag(self) -> str: ...
    @_property
    def edit_media_uri(self) -> typing.Optional[windows_foundation.Uri]: ...
    @_property
    def node_value(self) -> str: ...
    @node_value.setter
    def node_value(self, value: str) -> None: ...
    @_property
    def node_namespace(self) -> str: ...
    @node_namespace.setter
    def node_namespace(self, value: str) -> None: ...
    @_property
    def node_name(self) -> str: ...
    @node_name.setter
    def node_name(self, value: str) -> None: ...
    @_property
    def language(self) -> str: ...
    @language.setter
    def language(self, value: str) -> None: ...
    @_property
    def base_uri(self) -> typing.Optional[windows_foundation.Uri]: ...
    @base_uri.setter
    def base_uri(self, value: typing.Optional[windows_foundation.Uri]) -> None: ...
    @_property
    def attribute_extensions(self) -> typing.Optional[windows_foundation_collections.IVector[SyndicationAttribute]]: ...
    @_property
    def element_extensions(self) -> typing.Optional[windows_foundation_collections.IVector[ISyndicationNode]]: ...

@typing.final
class SyndicationLink(winrt.system.Object):
    @staticmethod
    def _from(obj: winrt.system.Object, /) -> SyndicationLink: ...
    @typing.overload
    def __new__(cls: typing.Type[SyndicationLink], uri: typing.Optional[windows_foundation.Uri]) -> SyndicationLink: ...
    @typing.overload
    def __new__(cls: typing.Type[SyndicationLink], uri: typing.Optional[windows_foundation.Uri], relationship: str, title: str, media_type: str, length: winrt.system.UInt32) -> SyndicationLink: ...
    @typing.overload
    def __new__(cls: typing.Type[SyndicationLink]) -> SyndicationLink: ...
    def get_xml_document(self, format: SyndicationFormat, /) -> typing.Optional[windows_data_xml_dom.XmlDocument]: ...
    @_property
    def uri(self) -> typing.Optional[windows_foundation.Uri]: ...
    @uri.setter
    def uri(self, value: typing.Optional[windows_foundation.Uri]) -> None: ...
    @_property
    def title(self) -> str: ...
    @title.setter
    def title(self, value: str) -> None: ...
    @_property
    def resource_language(self) -> str: ...
    @resource_language.setter
    def resource_language(self, value: str) -> None: ...
    @_property
    def relationship(self) -> str: ...
    @relationship.setter
    def relationship(self, value: str) -> None: ...
    @_property
    def media_type(self) -> str: ...
    @media_type.setter
    def media_type(self, value: str) -> None: ...
    @_property
    def length(self) -> winrt.system.UInt32: ...
    @length.setter
    def length(self, value: winrt.system.UInt32) -> None: ...
    @_property
    def node_value(self) -> str: ...
    @node_value.setter
    def node_value(self, value: str) -> None: ...
    @_property
    def node_namespace(self) -> str: ...
    @node_namespace.setter
    def node_namespace(self, value: str) -> None: ...
    @_property
    def node_name(self) -> str: ...
    @node_name.setter
    def node_name(self, value: str) -> None: ...
    @_property
    def language(self) -> str: ...
    @language.setter
    def language(self, value: str) -> None: ...
    @_property
    def base_uri(self) -> typing.Optional[windows_foundation.Uri]: ...
    @base_uri.setter
    def base_uri(self, value: typing.Optional[windows_foundation.Uri]) -> None: ...
    @_property
    def attribute_extensions(self) -> typing.Optional[windows_foundation_collections.IVector[SyndicationAttribute]]: ...
    @_property
    def element_extensions(self) -> typing.Optional[windows_foundation_collections.IVector[ISyndicationNode]]: ...

@typing.final
class SyndicationNode(winrt.system.Object):
    @staticmethod
    def _from(obj: winrt.system.Object, /) -> SyndicationNode: ...
    @typing.overload
    def __new__(cls: typing.Type[SyndicationNode], node_name: str, node_namespace: str, node_value: str) -> SyndicationNode: ...
    @typing.overload
    def __new__(cls: typing.Type[SyndicationNode]) -> SyndicationNode: ...
    def get_xml_document(self, format: SyndicationFormat, /) -> typing.Optional[windows_data_xml_dom.XmlDocument]: ...
    @_property
    def node_value(self) -> str: ...
    @node_value.setter
    def node_value(self, value: str) -> None: ...
    @_property
    def node_namespace(self) -> str: ...
    @node_namespace.setter
    def node_namespace(self, value: str) -> None: ...
    @_property
    def node_name(self) -> str: ...
    @node_name.setter
    def node_name(self, value: str) -> None: ...
    @_property
    def language(self) -> str: ...
    @language.setter
    def language(self, value: str) -> None: ...
    @_property
    def base_uri(self) -> typing.Optional[windows_foundation.Uri]: ...
    @base_uri.setter
    def base_uri(self, value: typing.Optional[windows_foundation.Uri]) -> None: ...
    @_property
    def attribute_extensions(self) -> typing.Optional[windows_foundation_collections.IVector[SyndicationAttribute]]: ...
    @_property
    def element_extensions(self) -> typing.Optional[windows_foundation_collections.IVector[ISyndicationNode]]: ...

@typing.final
class SyndicationPerson(winrt.system.Object):
    @staticmethod
    def _from(obj: winrt.system.Object, /) -> SyndicationPerson: ...
    @typing.overload
    def __new__(cls: typing.Type[SyndicationPerson], name: str) -> SyndicationPerson: ...
    @typing.overload
    def __new__(cls: typing.Type[SyndicationPerson], name: str, email: str, uri: typing.Optional[windows_foundation.Uri]) -> SyndicationPerson: ...
    @typing.overload
    def __new__(cls: typing.Type[SyndicationPerson]) -> SyndicationPerson: ...
    def get_xml_document(self, format: SyndicationFormat, /) -> typing.Optional[windows_data_xml_dom.XmlDocument]: ...
    @_property
    def node_value(self) -> str: ...
    @node_value.setter
    def node_value(self, value: str) -> None: ...
    @_property
    def node_namespace(self) -> str: ...
    @node_namespace.setter
    def node_namespace(self, value: str) -> None: ...
    @_property
    def node_name(self) -> str: ...
    @node_name.setter
    def node_name(self, value: str) -> None: ...
    @_property
    def language(self) -> str: ...
    @language.setter
    def language(self, value: str) -> None: ...
    @_property
    def base_uri(self) -> typing.Optional[windows_foundation.Uri]: ...
    @base_uri.setter
    def base_uri(self, value: typing.Optional[windows_foundation.Uri]) -> None: ...
    @_property
    def attribute_extensions(self) -> typing.Optional[windows_foundation_collections.IVector[SyndicationAttribute]]: ...
    @_property
    def element_extensions(self) -> typing.Optional[windows_foundation_collections.IVector[ISyndicationNode]]: ...
    @_property
    def uri(self) -> typing.Optional[windows_foundation.Uri]: ...
    @uri.setter
    def uri(self, value: typing.Optional[windows_foundation.Uri]) -> None: ...
    @_property
    def name(self) -> str: ...
    @name.setter
    def name(self, value: str) -> None: ...
    @_property
    def email(self) -> str: ...
    @email.setter
    def email(self, value: str) -> None: ...

@typing.final
class SyndicationText(winrt.system.Object):
    @staticmethod
    def _from(obj: winrt.system.Object, /) -> SyndicationText: ...
    @typing.overload
    def __new__(cls: typing.Type[SyndicationText], text: str) -> SyndicationText: ...
    @typing.overload
    def __new__(cls: typing.Type[SyndicationText], text: str, type: SyndicationTextType) -> SyndicationText: ...
    @typing.overload
    def __new__(cls: typing.Type[SyndicationText]) -> SyndicationText: ...
    def get_xml_document(self, format: SyndicationFormat, /) -> typing.Optional[windows_data_xml_dom.XmlDocument]: ...
    @_property
    def node_value(self) -> str: ...
    @node_value.setter
    def node_value(self, value: str) -> None: ...
    @_property
    def node_namespace(self) -> str: ...
    @node_namespace.setter
    def node_namespace(self, value: str) -> None: ...
    @_property
    def node_name(self) -> str: ...
    @node_name.setter
    def node_name(self, value: str) -> None: ...
    @_property
    def language(self) -> str: ...
    @language.setter
    def language(self, value: str) -> None: ...
    @_property
    def base_uri(self) -> typing.Optional[windows_foundation.Uri]: ...
    @base_uri.setter
    def base_uri(self, value: typing.Optional[windows_foundation.Uri]) -> None: ...
    @_property
    def attribute_extensions(self) -> typing.Optional[windows_foundation_collections.IVector[SyndicationAttribute]]: ...
    @_property
    def element_extensions(self) -> typing.Optional[windows_foundation_collections.IVector[ISyndicationNode]]: ...
    @_property
    def xml(self) -> typing.Optional[windows_data_xml_dom.XmlDocument]: ...
    @xml.setter
    def xml(self, value: typing.Optional[windows_data_xml_dom.XmlDocument]) -> None: ...
    @_property
    def type(self) -> str: ...
    @type.setter
    def type(self, value: str) -> None: ...
    @_property
    def text(self) -> str: ...
    @text.setter
    def text(self, value: str) -> None: ...

@typing.final
class ISyndicationClient(winrt.system.Object):
    @staticmethod
    def _from(obj: winrt.system.Object, /) -> ISyndicationClient: ...
    def retrieve_feed_async(self, uri: typing.Optional[windows_foundation.Uri], /) -> windows_foundation.IAsyncOperationWithProgress[SyndicationFeed, RetrievalProgress]: ...
    def set_request_header(self, name: str, value: str, /) -> None: ...
    @_property
    def bypass_cache_on_retrieve(self) -> bool: ...
    @bypass_cache_on_retrieve.setter
    def bypass_cache_on_retrieve(self, value: bool) -> None: ...
    @_property
    def max_response_buffer_size(self) -> winrt.system.UInt32: ...
    @max_response_buffer_size.setter
    def max_response_buffer_size(self, value: winrt.system.UInt32) -> None: ...
    @_property
    def proxy_credential(self) -> typing.Optional[windows_security_credentials.PasswordCredential]: ...
    @proxy_credential.setter
    def proxy_credential(self, value: typing.Optional[windows_security_credentials.PasswordCredential]) -> None: ...
    @_property
    def server_credential(self) -> typing.Optional[windows_security_credentials.PasswordCredential]: ...
    @server_credential.setter
    def server_credential(self, value: typing.Optional[windows_security_credentials.PasswordCredential]) -> None: ...
    @_property
    def timeout(self) -> winrt.system.UInt32: ...
    @timeout.setter
    def timeout(self, value: winrt.system.UInt32) -> None: ...

@typing.final
class ISyndicationNode(winrt.system.Object):
    @staticmethod
    def _from(obj: winrt.system.Object, /) -> ISyndicationNode: ...
    def get_xml_document(self, format: SyndicationFormat, /) -> typing.Optional[windows_data_xml_dom.XmlDocument]: ...
    @_property
    def attribute_extensions(self) -> typing.Optional[windows_foundation_collections.IVector[SyndicationAttribute]]: ...
    @_property
    def base_uri(self) -> typing.Optional[windows_foundation.Uri]: ...
    @base_uri.setter
    def base_uri(self, value: typing.Optional[windows_foundation.Uri]) -> None: ...
    @_property
    def element_extensions(self) -> typing.Optional[windows_foundation_collections.IVector[ISyndicationNode]]: ...
    @_property
    def language(self) -> str: ...
    @language.setter
    def language(self, value: str) -> None: ...
    @_property
    def node_name(self) -> str: ...
    @node_name.setter
    def node_name(self, value: str) -> None: ...
    @_property
    def node_namespace(self) -> str: ...
    @node_namespace.setter
    def node_namespace(self, value: str) -> None: ...
    @_property
    def node_value(self) -> str: ...
    @node_value.setter
    def node_value(self, value: str) -> None: ...

@typing.final
class ISyndicationText(winrt.system.Object):
    @staticmethod
    def _from(obj: winrt.system.Object, /) -> ISyndicationText: ...
    def get_xml_document(self, format: SyndicationFormat, /) -> typing.Optional[windows_data_xml_dom.XmlDocument]: ...
    @_property
    def text(self) -> str: ...
    @text.setter
    def text(self, value: str) -> None: ...
    @_property
    def type(self) -> str: ...
    @type.setter
    def type(self, value: str) -> None: ...
    @_property
    def xml(self) -> typing.Optional[windows_data_xml_dom.XmlDocument]: ...
    @xml.setter
    def xml(self, value: typing.Optional[windows_data_xml_dom.XmlDocument]) -> None: ...
    @_property
    def attribute_extensions(self) -> typing.Optional[windows_foundation_collections.IVector[SyndicationAttribute]]: ...
    @_property
    def base_uri(self) -> typing.Optional[windows_foundation.Uri]: ...
    @base_uri.setter
    def base_uri(self, value: typing.Optional[windows_foundation.Uri]) -> None: ...
    @_property
    def element_extensions(self) -> typing.Optional[windows_foundation_collections.IVector[ISyndicationNode]]: ...
    @_property
    def language(self) -> str: ...
    @language.setter
    def language(self, value: str) -> None: ...
    @_property
    def node_name(self) -> str: ...
    @node_name.setter
    def node_name(self, value: str) -> None: ...
    @_property
    def node_namespace(self) -> str: ...
    @node_namespace.setter
    def node_namespace(self, value: str) -> None: ...
    @_property
    def node_value(self) -> str: ...
    @node_value.setter
    def node_value(self, value: str) -> None: ...

