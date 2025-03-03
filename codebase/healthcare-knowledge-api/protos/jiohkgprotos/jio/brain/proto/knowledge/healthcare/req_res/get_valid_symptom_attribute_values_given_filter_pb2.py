# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: jio/brain/proto/knowledge/healthcare/req_res/get_valid_symptom_attribute_values_given_filter.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from jio.brain.proto.knowledge.healthcare.base import status_pb2 as jio_dot_brain_dot_proto_dot_knowledge_dot_healthcare_dot_base_dot_status__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='jio/brain/proto/knowledge/healthcare/req_res/get_valid_symptom_attribute_values_given_filter.proto',
  package='jio.brain.proto.knowledge.healthcare',
  syntax='proto3',
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\nbjio/brain/proto/knowledge/healthcare/req_res/get_valid_symptom_attribute_values_given_filter.proto\x12$jio.brain.proto.knowledge.healthcare\x1a\x36jio/brain/proto/knowledge/healthcare/base/status.proto\"y\n0GetValidSymptomAttributeValuesGivenFilterRequest\x12\x12\n\nsymptom_id\x18\x01 \x01(\r\x12\x14\n\x0c\x61ttribute_id\x18\x02 \x01(\r\x12\x0e\n\x06gender\x18\x03 \x01(\r\x12\x0b\n\x03\x61ge\x18\x04 \x01(\r\"\x88\x01\n1GetValidSymptomAttributeValuesGivenFilterResponse\x12\x10\n\x08value_id\x18\x01 \x03(\r\x12\x41\n\x06status\x18\x02 \x01(\x0b\x32\x31.jio.brain.proto.knowledge.healthcare.base.Statusb\x06proto3'
  ,
  dependencies=[jio_dot_brain_dot_proto_dot_knowledge_dot_healthcare_dot_base_dot_status__pb2.DESCRIPTOR,])




_GETVALIDSYMPTOMATTRIBUTEVALUESGIVENFILTERREQUEST = _descriptor.Descriptor(
  name='GetValidSymptomAttributeValuesGivenFilterRequest',
  full_name='jio.brain.proto.knowledge.healthcare.GetValidSymptomAttributeValuesGivenFilterRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='symptom_id', full_name='jio.brain.proto.knowledge.healthcare.GetValidSymptomAttributeValuesGivenFilterRequest.symptom_id', index=0,
      number=1, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='attribute_id', full_name='jio.brain.proto.knowledge.healthcare.GetValidSymptomAttributeValuesGivenFilterRequest.attribute_id', index=1,
      number=2, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='gender', full_name='jio.brain.proto.knowledge.healthcare.GetValidSymptomAttributeValuesGivenFilterRequest.gender', index=2,
      number=3, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='age', full_name='jio.brain.proto.knowledge.healthcare.GetValidSymptomAttributeValuesGivenFilterRequest.age', index=3,
      number=4, type=13, cpp_type=3, label=1,
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
  serialized_start=196,
  serialized_end=317,
)


_GETVALIDSYMPTOMATTRIBUTEVALUESGIVENFILTERRESPONSE = _descriptor.Descriptor(
  name='GetValidSymptomAttributeValuesGivenFilterResponse',
  full_name='jio.brain.proto.knowledge.healthcare.GetValidSymptomAttributeValuesGivenFilterResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='value_id', full_name='jio.brain.proto.knowledge.healthcare.GetValidSymptomAttributeValuesGivenFilterResponse.value_id', index=0,
      number=1, type=13, cpp_type=3, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='status', full_name='jio.brain.proto.knowledge.healthcare.GetValidSymptomAttributeValuesGivenFilterResponse.status', index=1,
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
  serialized_start=320,
  serialized_end=456,
)

_GETVALIDSYMPTOMATTRIBUTEVALUESGIVENFILTERRESPONSE.fields_by_name['status'].message_type = jio_dot_brain_dot_proto_dot_knowledge_dot_healthcare_dot_base_dot_status__pb2._STATUS
DESCRIPTOR.message_types_by_name['GetValidSymptomAttributeValuesGivenFilterRequest'] = _GETVALIDSYMPTOMATTRIBUTEVALUESGIVENFILTERREQUEST
DESCRIPTOR.message_types_by_name['GetValidSymptomAttributeValuesGivenFilterResponse'] = _GETVALIDSYMPTOMATTRIBUTEVALUESGIVENFILTERRESPONSE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

GetValidSymptomAttributeValuesGivenFilterRequest = _reflection.GeneratedProtocolMessageType('GetValidSymptomAttributeValuesGivenFilterRequest', (_message.Message,), {
  'DESCRIPTOR' : _GETVALIDSYMPTOMATTRIBUTEVALUESGIVENFILTERREQUEST,
  '__module__' : 'jio.brain.proto.knowledge.healthcare.req_res.get_valid_symptom_attribute_values_given_filter_pb2'
  # @@protoc_insertion_point(class_scope:jio.brain.proto.knowledge.healthcare.GetValidSymptomAttributeValuesGivenFilterRequest)
  })
_sym_db.RegisterMessage(GetValidSymptomAttributeValuesGivenFilterRequest)

GetValidSymptomAttributeValuesGivenFilterResponse = _reflection.GeneratedProtocolMessageType('GetValidSymptomAttributeValuesGivenFilterResponse', (_message.Message,), {
  'DESCRIPTOR' : _GETVALIDSYMPTOMATTRIBUTEVALUESGIVENFILTERRESPONSE,
  '__module__' : 'jio.brain.proto.knowledge.healthcare.req_res.get_valid_symptom_attribute_values_given_filter_pb2'
  # @@protoc_insertion_point(class_scope:jio.brain.proto.knowledge.healthcare.GetValidSymptomAttributeValuesGivenFilterResponse)
  })
_sym_db.RegisterMessage(GetValidSymptomAttributeValuesGivenFilterResponse)


# @@protoc_insertion_point(module_scope)
