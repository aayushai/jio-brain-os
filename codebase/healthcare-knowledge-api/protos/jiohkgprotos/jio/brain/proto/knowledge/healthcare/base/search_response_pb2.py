# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: jio/brain/proto/knowledge/healthcare/base/search_response.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='jio/brain/proto/knowledge/healthcare/base/search_response.proto',
  package='jio.brain.proto.knowledge.healthcare.base',
  syntax='proto3',
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n?jio/brain/proto/knowledge/healthcare/base/search_response.proto\x12)jio.brain.proto.knowledge.healthcare.base\"2\n\x0eSearchResponse\x12\n\n\x02id\x18\x01 \x01(\r\x12\x14\n\x0c\x64isplay_name\x18\x02 \x01(\tb\x06proto3'
)




_SEARCHRESPONSE = _descriptor.Descriptor(
  name='SearchResponse',
  full_name='jio.brain.proto.knowledge.healthcare.base.SearchResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='jio.brain.proto.knowledge.healthcare.base.SearchResponse.id', index=0,
      number=1, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='display_name', full_name='jio.brain.proto.knowledge.healthcare.base.SearchResponse.display_name', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=110,
  serialized_end=160,
)

DESCRIPTOR.message_types_by_name['SearchResponse'] = _SEARCHRESPONSE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

SearchResponse = _reflection.GeneratedProtocolMessageType('SearchResponse', (_message.Message,), {
  'DESCRIPTOR' : _SEARCHRESPONSE,
  '__module__' : 'jio.brain.proto.knowledge.healthcare.base.search_response_pb2'
  # @@protoc_insertion_point(class_scope:jio.brain.proto.knowledge.healthcare.base.SearchResponse)
  })
_sym_db.RegisterMessage(SearchResponse)


# @@protoc_insertion_point(module_scope)
