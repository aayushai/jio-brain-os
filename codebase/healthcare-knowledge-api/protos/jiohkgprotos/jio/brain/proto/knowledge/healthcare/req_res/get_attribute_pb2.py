# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: jio/brain/proto/knowledge/healthcare/req_res/get_attribute.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from jio.brain.proto.knowledge.healthcare.base import attribute_pb2 as jio_dot_brain_dot_proto_dot_knowledge_dot_healthcare_dot_base_dot_attribute__pb2
from jio.brain.proto.knowledge.healthcare.base import status_pb2 as jio_dot_brain_dot_proto_dot_knowledge_dot_healthcare_dot_base_dot_status__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='jio/brain/proto/knowledge/healthcare/req_res/get_attribute.proto',
  package='jio.brain.proto.knowledge.healthcare',
  syntax='proto3',
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n@jio/brain/proto/knowledge/healthcare/req_res/get_attribute.proto\x12$jio.brain.proto.knowledge.healthcare\x1a\x39jio/brain/proto/knowledge/healthcare/base/attribute.proto\x1a\x36jio/brain/proto/knowledge/healthcare/base/status.proto\"I\n\x13GetAttributeRequest\x12\x17\n\x0fsymptom_type_id\x18\x01 \x01(\r\x12\x19\n\x11\x61ttribute_type_id\x18\x02 \x01(\r\"\xa2\x01\n\x14GetAttributeResponse\x12G\n\tattribute\x18\x01 \x01(\x0b\x32\x34.jio.brain.proto.knowledge.healthcare.base.Attribute\x12\x41\n\x06status\x18\x02 \x01(\x0b\x32\x31.jio.brain.proto.knowledge.healthcare.base.Statusb\x06proto3'
  ,
  dependencies=[jio_dot_brain_dot_proto_dot_knowledge_dot_healthcare_dot_base_dot_attribute__pb2.DESCRIPTOR,jio_dot_brain_dot_proto_dot_knowledge_dot_healthcare_dot_base_dot_status__pb2.DESCRIPTOR,])




_GETATTRIBUTEREQUEST = _descriptor.Descriptor(
  name='GetAttributeRequest',
  full_name='jio.brain.proto.knowledge.healthcare.GetAttributeRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='symptom_type_id', full_name='jio.brain.proto.knowledge.healthcare.GetAttributeRequest.symptom_type_id', index=0,
      number=1, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='attribute_type_id', full_name='jio.brain.proto.knowledge.healthcare.GetAttributeRequest.attribute_type_id', index=1,
      number=2, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
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
  serialized_start=221,
  serialized_end=294,
)


_GETATTRIBUTERESPONSE = _descriptor.Descriptor(
  name='GetAttributeResponse',
  full_name='jio.brain.proto.knowledge.healthcare.GetAttributeResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='attribute', full_name='jio.brain.proto.knowledge.healthcare.GetAttributeResponse.attribute', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='status', full_name='jio.brain.proto.knowledge.healthcare.GetAttributeResponse.status', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
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
  serialized_start=297,
  serialized_end=459,
)

_GETATTRIBUTERESPONSE.fields_by_name['attribute'].message_type = jio_dot_brain_dot_proto_dot_knowledge_dot_healthcare_dot_base_dot_attribute__pb2._ATTRIBUTE
_GETATTRIBUTERESPONSE.fields_by_name['status'].message_type = jio_dot_brain_dot_proto_dot_knowledge_dot_healthcare_dot_base_dot_status__pb2._STATUS
DESCRIPTOR.message_types_by_name['GetAttributeRequest'] = _GETATTRIBUTEREQUEST
DESCRIPTOR.message_types_by_name['GetAttributeResponse'] = _GETATTRIBUTERESPONSE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

GetAttributeRequest = _reflection.GeneratedProtocolMessageType('GetAttributeRequest', (_message.Message,), {
  'DESCRIPTOR' : _GETATTRIBUTEREQUEST,
  '__module__' : 'jio.brain.proto.knowledge.healthcare.req_res.get_attribute_pb2'
  # @@protoc_insertion_point(class_scope:jio.brain.proto.knowledge.healthcare.GetAttributeRequest)
  })
_sym_db.RegisterMessage(GetAttributeRequest)

GetAttributeResponse = _reflection.GeneratedProtocolMessageType('GetAttributeResponse', (_message.Message,), {
  'DESCRIPTOR' : _GETATTRIBUTERESPONSE,
  '__module__' : 'jio.brain.proto.knowledge.healthcare.req_res.get_attribute_pb2'
  # @@protoc_insertion_point(class_scope:jio.brain.proto.knowledge.healthcare.GetAttributeResponse)
  })
_sym_db.RegisterMessage(GetAttributeResponse)


# @@protoc_insertion_point(module_scope)
