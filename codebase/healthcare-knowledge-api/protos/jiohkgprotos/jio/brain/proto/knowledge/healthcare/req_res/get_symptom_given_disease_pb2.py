# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: jio/brain/proto/knowledge/healthcare/req_res/get_symptom_given_disease.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from jio.brain.proto.knowledge.healthcare.base import status_pb2 as jio_dot_brain_dot_proto_dot_knowledge_dot_healthcare_dot_base_dot_status__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='jio/brain/proto/knowledge/healthcare/req_res/get_symptom_given_disease.proto',
  package='jio.brain.proto.knowledge.healthcare',
  syntax='proto3',
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\nLjio/brain/proto/knowledge/healthcare/req_res/get_symptom_given_disease.proto\x12$jio.brain.proto.knowledge.healthcare\x1a\x36jio/brain/proto/knowledge/healthcare/base/status.proto\"3\n\x1dGetSymptomGivenDiseaseRequest\x12\x12\n\ndisease_id\x18\x01 \x03(\r\"w\n\x1eGetSymptomGivenDiseaseResponse\x12\x12\n\nsymptom_id\x18\x01 \x03(\r\x12\x41\n\x06status\x18\x02 \x01(\x0b\x32\x31.jio.brain.proto.knowledge.healthcare.base.Statusb\x06proto3'
  ,
  dependencies=[jio_dot_brain_dot_proto_dot_knowledge_dot_healthcare_dot_base_dot_status__pb2.DESCRIPTOR,])




_GETSYMPTOMGIVENDISEASEREQUEST = _descriptor.Descriptor(
  name='GetSymptomGivenDiseaseRequest',
  full_name='jio.brain.proto.knowledge.healthcare.GetSymptomGivenDiseaseRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='disease_id', full_name='jio.brain.proto.knowledge.healthcare.GetSymptomGivenDiseaseRequest.disease_id', index=0,
      number=1, type=13, cpp_type=3, label=3,
      has_default_value=False, default_value=[],
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
  serialized_start=174,
  serialized_end=225,
)


_GETSYMPTOMGIVENDISEASERESPONSE = _descriptor.Descriptor(
  name='GetSymptomGivenDiseaseResponse',
  full_name='jio.brain.proto.knowledge.healthcare.GetSymptomGivenDiseaseResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='symptom_id', full_name='jio.brain.proto.knowledge.healthcare.GetSymptomGivenDiseaseResponse.symptom_id', index=0,
      number=1, type=13, cpp_type=3, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='status', full_name='jio.brain.proto.knowledge.healthcare.GetSymptomGivenDiseaseResponse.status', index=1,
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
  serialized_start=227,
  serialized_end=346,
)

_GETSYMPTOMGIVENDISEASERESPONSE.fields_by_name['status'].message_type = jio_dot_brain_dot_proto_dot_knowledge_dot_healthcare_dot_base_dot_status__pb2._STATUS
DESCRIPTOR.message_types_by_name['GetSymptomGivenDiseaseRequest'] = _GETSYMPTOMGIVENDISEASEREQUEST
DESCRIPTOR.message_types_by_name['GetSymptomGivenDiseaseResponse'] = _GETSYMPTOMGIVENDISEASERESPONSE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

GetSymptomGivenDiseaseRequest = _reflection.GeneratedProtocolMessageType('GetSymptomGivenDiseaseRequest', (_message.Message,), {
  'DESCRIPTOR' : _GETSYMPTOMGIVENDISEASEREQUEST,
  '__module__' : 'jio.brain.proto.knowledge.healthcare.req_res.get_symptom_given_disease_pb2'
  # @@protoc_insertion_point(class_scope:jio.brain.proto.knowledge.healthcare.GetSymptomGivenDiseaseRequest)
  })
_sym_db.RegisterMessage(GetSymptomGivenDiseaseRequest)

GetSymptomGivenDiseaseResponse = _reflection.GeneratedProtocolMessageType('GetSymptomGivenDiseaseResponse', (_message.Message,), {
  'DESCRIPTOR' : _GETSYMPTOMGIVENDISEASERESPONSE,
  '__module__' : 'jio.brain.proto.knowledge.healthcare.req_res.get_symptom_given_disease_pb2'
  # @@protoc_insertion_point(class_scope:jio.brain.proto.knowledge.healthcare.GetSymptomGivenDiseaseResponse)
  })
_sym_db.RegisterMessage(GetSymptomGivenDiseaseResponse)


# @@protoc_insertion_point(module_scope)
