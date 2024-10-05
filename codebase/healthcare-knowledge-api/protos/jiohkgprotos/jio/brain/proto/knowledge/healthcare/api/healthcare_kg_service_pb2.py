# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: jio/brain/proto/knowledge/healthcare/api/healthcare_kg_service.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from jio.brain.proto.knowledge.healthcare.req_res import get_all_disease_pb2 as jio_dot_brain_dot_proto_dot_knowledge_dot_healthcare_dot_req__res_dot_get__all__disease__pb2
from jio.brain.proto.knowledge.healthcare.req_res import get_disease_pb2 as jio_dot_brain_dot_proto_dot_knowledge_dot_healthcare_dot_req__res_dot_get__disease__pb2
from jio.brain.proto.knowledge.healthcare.req_res import get_disease_given_symptom_pb2 as jio_dot_brain_dot_proto_dot_knowledge_dot_healthcare_dot_req__res_dot_get__disease__given__symptom__pb2
from jio.brain.proto.knowledge.healthcare.req_res import get_symptom_given_disease_pb2 as jio_dot_brain_dot_proto_dot_knowledge_dot_healthcare_dot_req__res_dot_get__symptom__given__disease__pb2
from jio.brain.proto.knowledge.healthcare.req_res import get_all_symptom_pb2 as jio_dot_brain_dot_proto_dot_knowledge_dot_healthcare_dot_req__res_dot_get__all__symptom__pb2
from jio.brain.proto.knowledge.healthcare.req_res import get_symptom_pb2 as jio_dot_brain_dot_proto_dot_knowledge_dot_healthcare_dot_req__res_dot_get__symptom__pb2
from jio.brain.proto.knowledge.healthcare.req_res import get_attribute_pb2 as jio_dot_brain_dot_proto_dot_knowledge_dot_healthcare_dot_req__res_dot_get__attribute__pb2
from jio.brain.proto.knowledge.healthcare.req_res import get_attribute_value_pb2 as jio_dot_brain_dot_proto_dot_knowledge_dot_healthcare_dot_req__res_dot_get__attribute__value__pb2
from jio.brain.proto.knowledge.healthcare.req_res import get_attribute_order_pb2 as jio_dot_brain_dot_proto_dot_knowledge_dot_healthcare_dot_req__res_dot_get__attribute__order__pb2
from jio.brain.proto.knowledge.healthcare.req_res import get_attribute_name_pb2 as jio_dot_brain_dot_proto_dot_knowledge_dot_healthcare_dot_req__res_dot_get__attribute__name__pb2
from jio.brain.proto.knowledge.healthcare.req_res import get_attribute_id_pb2 as jio_dot_brain_dot_proto_dot_knowledge_dot_healthcare_dot_req__res_dot_get__attribute__id__pb2
from jio.brain.proto.knowledge.healthcare.req_res import get_symptom_bucket_in_disease_pb2 as jio_dot_brain_dot_proto_dot_knowledge_dot_healthcare_dot_req__res_dot_get__symptom__bucket__in__disease__pb2
from jio.brain.proto.knowledge.healthcare.req_res import get_highest_attribute_bucket_pb2 as jio_dot_brain_dot_proto_dot_knowledge_dot_healthcare_dot_req__res_dot_get__highest__attribute__bucket__pb2
from jio.brain.proto.knowledge.healthcare.req_res import get_attribute_bucket_in_disease_pb2 as jio_dot_brain_dot_proto_dot_knowledge_dot_healthcare_dot_req__res_dot_get__attribute__bucket__in__disease__pb2
from jio.brain.proto.knowledge.healthcare.req_res import get_attribute_value_id_pb2 as jio_dot_brain_dot_proto_dot_knowledge_dot_healthcare_dot_req__res_dot_get__attribute__value__id__pb2
from jio.brain.proto.knowledge.healthcare.req_res import get_attributes_of_symptom_and_disease_pb2 as jio_dot_brain_dot_proto_dot_knowledge_dot_healthcare_dot_req__res_dot_get__attributes__of__symptom__and__disease__pb2
from jio.brain.proto.knowledge.healthcare.req_res import get_disease_id_pb2 as jio_dot_brain_dot_proto_dot_knowledge_dot_healthcare_dot_req__res_dot_get__disease__id__pb2
from jio.brain.proto.knowledge.healthcare.req_res import get_symptom_id_pb2 as jio_dot_brain_dot_proto_dot_knowledge_dot_healthcare_dot_req__res_dot_get__symptom__id__pb2
from jio.brain.proto.knowledge.healthcare.req_res import get_context_pb2 as jio_dot_brain_dot_proto_dot_knowledge_dot_healthcare_dot_req__res_dot_get__context__pb2
from jio.brain.proto.knowledge.healthcare.req_res import get_context_id_pb2 as jio_dot_brain_dot_proto_dot_knowledge_dot_healthcare_dot_req__res_dot_get__context__id__pb2
from jio.brain.proto.knowledge.healthcare.req_res import get_context_value_id_pb2 as jio_dot_brain_dot_proto_dot_knowledge_dot_healthcare_dot_req__res_dot_get__context__value__id__pb2
from jio.brain.proto.knowledge.healthcare.req_res import search_symptoms_pb2 as jio_dot_brain_dot_proto_dot_knowledge_dot_healthcare_dot_req__res_dot_search__symptoms__pb2
from jio.brain.proto.knowledge.healthcare.req_res import search_diseases_pb2 as jio_dot_brain_dot_proto_dot_knowledge_dot_healthcare_dot_req__res_dot_search__diseases__pb2
from jio.brain.proto.knowledge.healthcare.req_res import get_symptom_patient_state_pb2 as jio_dot_brain_dot_proto_dot_knowledge_dot_healthcare_dot_req__res_dot_get__symptom__patient__state__pb2
from jio.brain.proto.knowledge.healthcare.req_res import get_disease_patient_state_pb2 as jio_dot_brain_dot_proto_dot_knowledge_dot_healthcare_dot_req__res_dot_get__disease__patient__state__pb2
from jio.brain.proto.knowledge.healthcare.req_res import get_valid_symptom_attribute_values_given_filter_pb2 as jio_dot_brain_dot_proto_dot_knowledge_dot_healthcare_dot_req__res_dot_get__valid__symptom__attribute__values__given__filter__pb2
from jio.brain.proto.knowledge.healthcare.req_res import get_symptom_name_pb2 as jio_dot_brain_dot_proto_dot_knowledge_dot_healthcare_dot_req__res_dot_get__symptom__name__pb2
from jio.brain.proto.knowledge.healthcare.req_res import get_disease_name_pb2 as jio_dot_brain_dot_proto_dot_knowledge_dot_healthcare_dot_req__res_dot_get__disease__name__pb2
from jio.brain.proto.knowledge.healthcare.req_res import get_context_name_pb2 as jio_dot_brain_dot_proto_dot_knowledge_dot_healthcare_dot_req__res_dot_get__context__name__pb2
from jio.brain.proto.knowledge.healthcare.req_res import get_attribute_value_name_pb2 as jio_dot_brain_dot_proto_dot_knowledge_dot_healthcare_dot_req__res_dot_get__attribute__value__name__pb2
from jio.brain.proto.knowledge.healthcare.req_res import get_context_value_name_pb2 as jio_dot_brain_dot_proto_dot_knowledge_dot_healthcare_dot_req__res_dot_get__context__value__name__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='jio/brain/proto/knowledge/healthcare/api/healthcare_kg_service.proto',
  package='jio.brain.proto.knowledge.healthcare',
  syntax='proto3',
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\nDjio/brain/proto/knowledge/healthcare/api/healthcare_kg_service.proto\x12$jio.brain.proto.knowledge.healthcare\x1a\x42jio/brain/proto/knowledge/healthcare/req_res/get_all_disease.proto\x1a>jio/brain/proto/knowledge/healthcare/req_res/get_disease.proto\x1aLjio/brain/proto/knowledge/healthcare/req_res/get_disease_given_symptom.proto\x1aLjio/brain/proto/knowledge/healthcare/req_res/get_symptom_given_disease.proto\x1a\x42jio/brain/proto/knowledge/healthcare/req_res/get_all_symptom.proto\x1a>jio/brain/proto/knowledge/healthcare/req_res/get_symptom.proto\x1a@jio/brain/proto/knowledge/healthcare/req_res/get_attribute.proto\x1a\x46jio/brain/proto/knowledge/healthcare/req_res/get_attribute_value.proto\x1a\x46jio/brain/proto/knowledge/healthcare/req_res/get_attribute_order.proto\x1a\x45jio/brain/proto/knowledge/healthcare/req_res/get_attribute_name.proto\x1a\x43jio/brain/proto/knowledge/healthcare/req_res/get_attribute_id.proto\x1aPjio/brain/proto/knowledge/healthcare/req_res/get_symptom_bucket_in_disease.proto\x1aOjio/brain/proto/knowledge/healthcare/req_res/get_highest_attribute_bucket.proto\x1aRjio/brain/proto/knowledge/healthcare/req_res/get_attribute_bucket_in_disease.proto\x1aIjio/brain/proto/knowledge/healthcare/req_res/get_attribute_value_id.proto\x1aXjio/brain/proto/knowledge/healthcare/req_res/get_attributes_of_symptom_and_disease.proto\x1a\x41jio/brain/proto/knowledge/healthcare/req_res/get_disease_id.proto\x1a\x41jio/brain/proto/knowledge/healthcare/req_res/get_symptom_id.proto\x1a>jio/brain/proto/knowledge/healthcare/req_res/get_context.proto\x1a\x41jio/brain/proto/knowledge/healthcare/req_res/get_context_id.proto\x1aGjio/brain/proto/knowledge/healthcare/req_res/get_context_value_id.proto\x1a\x42jio/brain/proto/knowledge/healthcare/req_res/search_symptoms.proto\x1a\x42jio/brain/proto/knowledge/healthcare/req_res/search_diseases.proto\x1aLjio/brain/proto/knowledge/healthcare/req_res/get_symptom_patient_state.proto\x1aLjio/brain/proto/knowledge/healthcare/req_res/get_disease_patient_state.proto\x1a\x62jio/brain/proto/knowledge/healthcare/req_res/get_valid_symptom_attribute_values_given_filter.proto\x1a\x43jio/brain/proto/knowledge/healthcare/req_res/get_symptom_name.proto\x1a\x43jio/brain/proto/knowledge/healthcare/req_res/get_disease_name.proto\x1a\x43jio/brain/proto/knowledge/healthcare/req_res/get_context_name.proto\x1aKjio/brain/proto/knowledge/healthcare/req_res/get_attribute_value_name.proto\x1aIjio/brain/proto/knowledge/healthcare/req_res/get_context_value_name.proto2\xf1%\n\x1dHealthcareKnowledgeApiService\x12\x8a\x01\n\rGetAllDisease\x12:.jio.brain.proto.knowledge.healthcare.GetAllDiseaseRequest\x1a;.jio.brain.proto.knowledge.healthcare.GetAllDiseaseResponse\"\x00\x12\x81\x01\n\nGetDisease\x12\x37.jio.brain.proto.knowledge.healthcare.GetDiseaseRequest\x1a\x38.jio.brain.proto.knowledge.healthcare.GetDiseaseResponse\"\x00\x12\xa5\x01\n\x16GetDiseaseGivenSymptom\x12\x43.jio.brain.proto.knowledge.healthcare.GetDiseaseGivenSymptomRequest\x1a\x44.jio.brain.proto.knowledge.healthcare.GetDiseaseGivenSymptomResponse\"\x00\x12\x87\x01\n\x0cGetDiseaseId\x12\x39.jio.brain.proto.knowledge.healthcare.GetDiseaseIdRequest\x1a:.jio.brain.proto.knowledge.healthcare.GetDiseaseIdResponse\"\x00\x12\x8a\x01\n\rGetAllSymptom\x12:.jio.brain.proto.knowledge.healthcare.GetAllSymptomRequest\x1a;.jio.brain.proto.knowledge.healthcare.GetAllSymptomResponse\"\x00\x12\x81\x01\n\nGetSymptom\x12\x37.jio.brain.proto.knowledge.healthcare.GetSymptomRequest\x1a\x38.jio.brain.proto.knowledge.healthcare.GetSymptomResponse\"\x00\x12\xa5\x01\n\x16GetSymptomGivenDisease\x12\x43.jio.brain.proto.knowledge.healthcare.GetSymptomGivenDiseaseRequest\x1a\x44.jio.brain.proto.knowledge.healthcare.GetSymptomGivenDiseaseResponse\"\x00\x12\xae\x01\n\x19GetSymptomBucketInDisease\x12\x46.jio.brain.proto.knowledge.healthcare.GetSymptomBucketInDiseaseRequest\x1aG.jio.brain.proto.knowledge.healthcare.GetSymptomBucketInDiseaseResponse\"\x00\x12\x87\x01\n\x0cGetSymptomId\x12\x39.jio.brain.proto.knowledge.healthcare.GetSymptomIdRequest\x1a:.jio.brain.proto.knowledge.healthcare.GetSymptomIdResponse\"\x00\x12\x87\x01\n\x0cGetAttribute\x12\x39.jio.brain.proto.knowledge.healthcare.GetAttributeRequest\x1a:.jio.brain.proto.knowledge.healthcare.GetAttributeResponse\"\x00\x12\x96\x01\n\x11GetAttributeValue\x12>.jio.brain.proto.knowledge.healthcare.GetAttributeValueRequest\x1a?.jio.brain.proto.knowledge.healthcare.GetAttributeValueResponse\"\x00\x12\x96\x01\n\x11GetAttributeOrder\x12>.jio.brain.proto.knowledge.healthcare.GetAttributeOrderRequest\x1a?.jio.brain.proto.knowledge.healthcare.GetAttributeOrderResponse\"\x00\x12\x93\x01\n\x10GetAttributeName\x12=.jio.brain.proto.knowledge.healthcare.GetAttributeNameRequest\x1a>.jio.brain.proto.knowledge.healthcare.GetAttributeNameResponse\"\x00\x12\x8d\x01\n\x0eGetAttributeId\x12;.jio.brain.proto.knowledge.healthcare.GetAttributeIdRequest\x1a<.jio.brain.proto.knowledge.healthcare.GetAttributeIdResponse\"\x00\x12\x9c\x01\n\x13GetAttributeValueId\x12@.jio.brain.proto.knowledge.healthcare.GetAttributeValueIdRequest\x1a\x41.jio.brain.proto.knowledge.healthcare.GetAttributeValueIdResponse\"\x00\x12\xae\x01\n\x19GetHighestAttributeBucket\x12\x46.jio.brain.proto.knowledge.healthcare.GetHighestAttributeBucketRequest\x1aG.jio.brain.proto.knowledge.healthcare.GetHighestAttributeBucketResponse\"\x00\x12\xb4\x01\n\x1bGetAttributeBucketInDisease\x12H.jio.brain.proto.knowledge.healthcare.GetAttributeBucketInDiseaseRequest\x1aI.jio.brain.proto.knowledge.healthcare.GetAttributeBucketInDiseaseResponse\"\x00\x12\xc3\x01\n GetAttributesOfSymptomAndDisease\x12M.jio.brain.proto.knowledge.healthcare.GetAttributesOfSymptomAndDiseaseRequest\x1aN.jio.brain.proto.knowledge.healthcare.GetAttributesOfSymptomAndDiseaseResponse\"\x00\x12\x81\x01\n\nGetContext\x12\x37.jio.brain.proto.knowledge.healthcare.GetContextRequest\x1a\x38.jio.brain.proto.knowledge.healthcare.GetContextResponse\"\x00\x12\x87\x01\n\x0cGetContextId\x12\x39.jio.brain.proto.knowledge.healthcare.GetContextIdRequest\x1a:.jio.brain.proto.knowledge.healthcare.GetContextIdResponse\"\x00\x12\x96\x01\n\x11GetContextValueId\x12>.jio.brain.proto.knowledge.healthcare.GetContextValueIdRequest\x1a?.jio.brain.proto.knowledge.healthcare.GetContextValueIdResponse\"\x00\x12\xa5\x01\n\x16GetSymptomPatientState\x12\x43.jio.brain.proto.knowledge.healthcare.GetSymptomPatientStateRequest\x1a\x44.jio.brain.proto.knowledge.healthcare.GetSymptomPatientStateResponse\"\x00\x12\xa5\x01\n\x16GetDiseasePatientState\x12\x43.jio.brain.proto.knowledge.healthcare.GetDiseasePatientStateRequest\x1a\x44.jio.brain.proto.knowledge.healthcare.GetDiseasePatientStateResponse\"\x00\x12\x8d\x01\n\x0eSearchSymptoms\x12;.jio.brain.proto.knowledge.healthcare.SearchSymptomsRequest\x1a<.jio.brain.proto.knowledge.healthcare.SearchSymptomsResponse\"\x00\x12\x8d\x01\n\x0eSearchDiseases\x12;.jio.brain.proto.knowledge.healthcare.SearchDiseasesRequest\x1a<.jio.brain.proto.knowledge.healthcare.SearchDiseasesResponse\"\x00\x12\xde\x01\n)GetValidSymptomAttributeValuesGivenFilter\x12V.jio.brain.proto.knowledge.healthcare.GetValidSymptomAttributeValuesGivenFilterRequest\x1aW.jio.brain.proto.knowledge.healthcare.GetValidSymptomAttributeValuesGivenFilterResponse\"\x00\x12\x8d\x01\n\x0eGetDiseaseName\x12;.jio.brain.proto.knowledge.healthcare.GetDiseaseNameRequest\x1a<.jio.brain.proto.knowledge.healthcare.GetDiseaseNameResponse\"\x00\x12\x8d\x01\n\x0eGetSymptomName\x12;.jio.brain.proto.knowledge.healthcare.GetSymptomNameRequest\x1a<.jio.brain.proto.knowledge.healthcare.GetSymptomNameResponse\"\x00\x12\xa2\x01\n\x15GetAttributeValueName\x12\x42.jio.brain.proto.knowledge.healthcare.GetAttributeValueNameRequest\x1a\x43.jio.brain.proto.knowledge.healthcare.GetAttributeValueNameResponse\"\x00\x12\x8d\x01\n\x0eGetContextName\x12;.jio.brain.proto.knowledge.healthcare.GetContextNameRequest\x1a<.jio.brain.proto.knowledge.healthcare.GetContextNameResponse\"\x00\x12\x9c\x01\n\x13GetContextValueName\x12@.jio.brain.proto.knowledge.healthcare.GetContextValueNameRequest\x1a\x41.jio.brain.proto.knowledge.healthcare.GetContextValueNameResponse\"\x00\x62\x06proto3'
  ,
  dependencies=[jio_dot_brain_dot_proto_dot_knowledge_dot_healthcare_dot_req__res_dot_get__all__disease__pb2.DESCRIPTOR,jio_dot_brain_dot_proto_dot_knowledge_dot_healthcare_dot_req__res_dot_get__disease__pb2.DESCRIPTOR,jio_dot_brain_dot_proto_dot_knowledge_dot_healthcare_dot_req__res_dot_get__disease__given__symptom__pb2.DESCRIPTOR,jio_dot_brain_dot_proto_dot_knowledge_dot_healthcare_dot_req__res_dot_get__symptom__given__disease__pb2.DESCRIPTOR,jio_dot_brain_dot_proto_dot_knowledge_dot_healthcare_dot_req__res_dot_get__all__symptom__pb2.DESCRIPTOR,jio_dot_brain_dot_proto_dot_knowledge_dot_healthcare_dot_req__res_dot_get__symptom__pb2.DESCRIPTOR,jio_dot_brain_dot_proto_dot_knowledge_dot_healthcare_dot_req__res_dot_get__attribute__pb2.DESCRIPTOR,jio_dot_brain_dot_proto_dot_knowledge_dot_healthcare_dot_req__res_dot_get__attribute__value__pb2.DESCRIPTOR,jio_dot_brain_dot_proto_dot_knowledge_dot_healthcare_dot_req__res_dot_get__attribute__order__pb2.DESCRIPTOR,jio_dot_brain_dot_proto_dot_knowledge_dot_healthcare_dot_req__res_dot_get__attribute__name__pb2.DESCRIPTOR,jio_dot_brain_dot_proto_dot_knowledge_dot_healthcare_dot_req__res_dot_get__attribute__id__pb2.DESCRIPTOR,jio_dot_brain_dot_proto_dot_knowledge_dot_healthcare_dot_req__res_dot_get__symptom__bucket__in__disease__pb2.DESCRIPTOR,jio_dot_brain_dot_proto_dot_knowledge_dot_healthcare_dot_req__res_dot_get__highest__attribute__bucket__pb2.DESCRIPTOR,jio_dot_brain_dot_proto_dot_knowledge_dot_healthcare_dot_req__res_dot_get__attribute__bucket__in__disease__pb2.DESCRIPTOR,jio_dot_brain_dot_proto_dot_knowledge_dot_healthcare_dot_req__res_dot_get__attribute__value__id__pb2.DESCRIPTOR,jio_dot_brain_dot_proto_dot_knowledge_dot_healthcare_dot_req__res_dot_get__attributes__of__symptom__and__disease__pb2.DESCRIPTOR,jio_dot_brain_dot_proto_dot_knowledge_dot_healthcare_dot_req__res_dot_get__disease__id__pb2.DESCRIPTOR,jio_dot_brain_dot_proto_dot_knowledge_dot_healthcare_dot_req__res_dot_get__symptom__id__pb2.DESCRIPTOR,jio_dot_brain_dot_proto_dot_knowledge_dot_healthcare_dot_req__res_dot_get__context__pb2.DESCRIPTOR,jio_dot_brain_dot_proto_dot_knowledge_dot_healthcare_dot_req__res_dot_get__context__id__pb2.DESCRIPTOR,jio_dot_brain_dot_proto_dot_knowledge_dot_healthcare_dot_req__res_dot_get__context__value__id__pb2.DESCRIPTOR,jio_dot_brain_dot_proto_dot_knowledge_dot_healthcare_dot_req__res_dot_search__symptoms__pb2.DESCRIPTOR,jio_dot_brain_dot_proto_dot_knowledge_dot_healthcare_dot_req__res_dot_search__diseases__pb2.DESCRIPTOR,jio_dot_brain_dot_proto_dot_knowledge_dot_healthcare_dot_req__res_dot_get__symptom__patient__state__pb2.DESCRIPTOR,jio_dot_brain_dot_proto_dot_knowledge_dot_healthcare_dot_req__res_dot_get__disease__patient__state__pb2.DESCRIPTOR,jio_dot_brain_dot_proto_dot_knowledge_dot_healthcare_dot_req__res_dot_get__valid__symptom__attribute__values__given__filter__pb2.DESCRIPTOR,jio_dot_brain_dot_proto_dot_knowledge_dot_healthcare_dot_req__res_dot_get__symptom__name__pb2.DESCRIPTOR,jio_dot_brain_dot_proto_dot_knowledge_dot_healthcare_dot_req__res_dot_get__disease__name__pb2.DESCRIPTOR,jio_dot_brain_dot_proto_dot_knowledge_dot_healthcare_dot_req__res_dot_get__context__name__pb2.DESCRIPTOR,jio_dot_brain_dot_proto_dot_knowledge_dot_healthcare_dot_req__res_dot_get__attribute__value__name__pb2.DESCRIPTOR,jio_dot_brain_dot_proto_dot_knowledge_dot_healthcare_dot_req__res_dot_get__context__value__name__pb2.DESCRIPTOR,])



_sym_db.RegisterFileDescriptor(DESCRIPTOR)



_HEALTHCAREKNOWLEDGEAPISERVICE = _descriptor.ServiceDescriptor(
  name='HealthcareKnowledgeApiService',
  full_name='jio.brain.proto.knowledge.healthcare.HealthcareKnowledgeApiService',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_start=2382,
  serialized_end=7231,
  methods=[
  _descriptor.MethodDescriptor(
    name='GetAllDisease',
    full_name='jio.brain.proto.knowledge.healthcare.HealthcareKnowledgeApiService.GetAllDisease',
    index=0,
    containing_service=None,
    input_type=jio_dot_brain_dot_proto_dot_knowledge_dot_healthcare_dot_req__res_dot_get__all__disease__pb2._GETALLDISEASEREQUEST,
    output_type=jio_dot_brain_dot_proto_dot_knowledge_dot_healthcare_dot_req__res_dot_get__all__disease__pb2._GETALLDISEASERESPONSE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='GetDisease',
    full_name='jio.brain.proto.knowledge.healthcare.HealthcareKnowledgeApiService.GetDisease',
    index=1,
    containing_service=None,
    input_type=jio_dot_brain_dot_proto_dot_knowledge_dot_healthcare_dot_req__res_dot_get__disease__pb2._GETDISEASEREQUEST,
    output_type=jio_dot_brain_dot_proto_dot_knowledge_dot_healthcare_dot_req__res_dot_get__disease__pb2._GETDISEASERESPONSE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='GetDiseaseGivenSymptom',
    full_name='jio.brain.proto.knowledge.healthcare.HealthcareKnowledgeApiService.GetDiseaseGivenSymptom',
    index=2,
    containing_service=None,
    input_type=jio_dot_brain_dot_proto_dot_knowledge_dot_healthcare_dot_req__res_dot_get__disease__given__symptom__pb2._GETDISEASEGIVENSYMPTOMREQUEST,
    output_type=jio_dot_brain_dot_proto_dot_knowledge_dot_healthcare_dot_req__res_dot_get__disease__given__symptom__pb2._GETDISEASEGIVENSYMPTOMRESPONSE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='GetDiseaseId',
    full_name='jio.brain.proto.knowledge.healthcare.HealthcareKnowledgeApiService.GetDiseaseId',
    index=3,
    containing_service=None,
    input_type=jio_dot_brain_dot_proto_dot_knowledge_dot_healthcare_dot_req__res_dot_get__disease__id__pb2._GETDISEASEIDREQUEST,
    output_type=jio_dot_brain_dot_proto_dot_knowledge_dot_healthcare_dot_req__res_dot_get__disease__id__pb2._GETDISEASEIDRESPONSE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='GetAllSymptom',
    full_name='jio.brain.proto.knowledge.healthcare.HealthcareKnowledgeApiService.GetAllSymptom',
    index=4,
    containing_service=None,
    input_type=jio_dot_brain_dot_proto_dot_knowledge_dot_healthcare_dot_req__res_dot_get__all__symptom__pb2._GETALLSYMPTOMREQUEST,
    output_type=jio_dot_brain_dot_proto_dot_knowledge_dot_healthcare_dot_req__res_dot_get__all__symptom__pb2._GETALLSYMPTOMRESPONSE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='GetSymptom',
    full_name='jio.brain.proto.knowledge.healthcare.HealthcareKnowledgeApiService.GetSymptom',
    index=5,
    containing_service=None,
    input_type=jio_dot_brain_dot_proto_dot_knowledge_dot_healthcare_dot_req__res_dot_get__symptom__pb2._GETSYMPTOMREQUEST,
    output_type=jio_dot_brain_dot_proto_dot_knowledge_dot_healthcare_dot_req__res_dot_get__symptom__pb2._GETSYMPTOMRESPONSE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='GetSymptomGivenDisease',
    full_name='jio.brain.proto.knowledge.healthcare.HealthcareKnowledgeApiService.GetSymptomGivenDisease',
    index=6,
    containing_service=None,
    input_type=jio_dot_brain_dot_proto_dot_knowledge_dot_healthcare_dot_req__res_dot_get__symptom__given__disease__pb2._GETSYMPTOMGIVENDISEASEREQUEST,
    output_type=jio_dot_brain_dot_proto_dot_knowledge_dot_healthcare_dot_req__res_dot_get__symptom__given__disease__pb2._GETSYMPTOMGIVENDISEASERESPONSE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='GetSymptomBucketInDisease',
    full_name='jio.brain.proto.knowledge.healthcare.HealthcareKnowledgeApiService.GetSymptomBucketInDisease',
    index=7,
    containing_service=None,
    input_type=jio_dot_brain_dot_proto_dot_knowledge_dot_healthcare_dot_req__res_dot_get__symptom__bucket__in__disease__pb2._GETSYMPTOMBUCKETINDISEASEREQUEST,
    output_type=jio_dot_brain_dot_proto_dot_knowledge_dot_healthcare_dot_req__res_dot_get__symptom__bucket__in__disease__pb2._GETSYMPTOMBUCKETINDISEASERESPONSE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='GetSymptomId',
    full_name='jio.brain.proto.knowledge.healthcare.HealthcareKnowledgeApiService.GetSymptomId',
    index=8,
    containing_service=None,
    input_type=jio_dot_brain_dot_proto_dot_knowledge_dot_healthcare_dot_req__res_dot_get__symptom__id__pb2._GETSYMPTOMIDREQUEST,
    output_type=jio_dot_brain_dot_proto_dot_knowledge_dot_healthcare_dot_req__res_dot_get__symptom__id__pb2._GETSYMPTOMIDRESPONSE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='GetAttribute',
    full_name='jio.brain.proto.knowledge.healthcare.HealthcareKnowledgeApiService.GetAttribute',
    index=9,
    containing_service=None,
    input_type=jio_dot_brain_dot_proto_dot_knowledge_dot_healthcare_dot_req__res_dot_get__attribute__pb2._GETATTRIBUTEREQUEST,
    output_type=jio_dot_brain_dot_proto_dot_knowledge_dot_healthcare_dot_req__res_dot_get__attribute__pb2._GETATTRIBUTERESPONSE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='GetAttributeValue',
    full_name='jio.brain.proto.knowledge.healthcare.HealthcareKnowledgeApiService.GetAttributeValue',
    index=10,
    containing_service=None,
    input_type=jio_dot_brain_dot_proto_dot_knowledge_dot_healthcare_dot_req__res_dot_get__attribute__value__pb2._GETATTRIBUTEVALUEREQUEST,
    output_type=jio_dot_brain_dot_proto_dot_knowledge_dot_healthcare_dot_req__res_dot_get__attribute__value__pb2._GETATTRIBUTEVALUERESPONSE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='GetAttributeOrder',
    full_name='jio.brain.proto.knowledge.healthcare.HealthcareKnowledgeApiService.GetAttributeOrder',
    index=11,
    containing_service=None,
    input_type=jio_dot_brain_dot_proto_dot_knowledge_dot_healthcare_dot_req__res_dot_get__attribute__order__pb2._GETATTRIBUTEORDERREQUEST,
    output_type=jio_dot_brain_dot_proto_dot_knowledge_dot_healthcare_dot_req__res_dot_get__attribute__order__pb2._GETATTRIBUTEORDERRESPONSE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='GetAttributeName',
    full_name='jio.brain.proto.knowledge.healthcare.HealthcareKnowledgeApiService.GetAttributeName',
    index=12,
    containing_service=None,
    input_type=jio_dot_brain_dot_proto_dot_knowledge_dot_healthcare_dot_req__res_dot_get__attribute__name__pb2._GETATTRIBUTENAMEREQUEST,
    output_type=jio_dot_brain_dot_proto_dot_knowledge_dot_healthcare_dot_req__res_dot_get__attribute__name__pb2._GETATTRIBUTENAMERESPONSE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='GetAttributeId',
    full_name='jio.brain.proto.knowledge.healthcare.HealthcareKnowledgeApiService.GetAttributeId',
    index=13,
    containing_service=None,
    input_type=jio_dot_brain_dot_proto_dot_knowledge_dot_healthcare_dot_req__res_dot_get__attribute__id__pb2._GETATTRIBUTEIDREQUEST,
    output_type=jio_dot_brain_dot_proto_dot_knowledge_dot_healthcare_dot_req__res_dot_get__attribute__id__pb2._GETATTRIBUTEIDRESPONSE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='GetAttributeValueId',
    full_name='jio.brain.proto.knowledge.healthcare.HealthcareKnowledgeApiService.GetAttributeValueId',
    index=14,
    containing_service=None,
    input_type=jio_dot_brain_dot_proto_dot_knowledge_dot_healthcare_dot_req__res_dot_get__attribute__value__id__pb2._GETATTRIBUTEVALUEIDREQUEST,
    output_type=jio_dot_brain_dot_proto_dot_knowledge_dot_healthcare_dot_req__res_dot_get__attribute__value__id__pb2._GETATTRIBUTEVALUEIDRESPONSE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='GetHighestAttributeBucket',
    full_name='jio.brain.proto.knowledge.healthcare.HealthcareKnowledgeApiService.GetHighestAttributeBucket',
    index=15,
    containing_service=None,
    input_type=jio_dot_brain_dot_proto_dot_knowledge_dot_healthcare_dot_req__res_dot_get__highest__attribute__bucket__pb2._GETHIGHESTATTRIBUTEBUCKETREQUEST,
    output_type=jio_dot_brain_dot_proto_dot_knowledge_dot_healthcare_dot_req__res_dot_get__highest__attribute__bucket__pb2._GETHIGHESTATTRIBUTEBUCKETRESPONSE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='GetAttributeBucketInDisease',
    full_name='jio.brain.proto.knowledge.healthcare.HealthcareKnowledgeApiService.GetAttributeBucketInDisease',
    index=16,
    containing_service=None,
    input_type=jio_dot_brain_dot_proto_dot_knowledge_dot_healthcare_dot_req__res_dot_get__attribute__bucket__in__disease__pb2._GETATTRIBUTEBUCKETINDISEASEREQUEST,
    output_type=jio_dot_brain_dot_proto_dot_knowledge_dot_healthcare_dot_req__res_dot_get__attribute__bucket__in__disease__pb2._GETATTRIBUTEBUCKETINDISEASERESPONSE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='GetAttributesOfSymptomAndDisease',
    full_name='jio.brain.proto.knowledge.healthcare.HealthcareKnowledgeApiService.GetAttributesOfSymptomAndDisease',
    index=17,
    containing_service=None,
    input_type=jio_dot_brain_dot_proto_dot_knowledge_dot_healthcare_dot_req__res_dot_get__attributes__of__symptom__and__disease__pb2._GETATTRIBUTESOFSYMPTOMANDDISEASEREQUEST,
    output_type=jio_dot_brain_dot_proto_dot_knowledge_dot_healthcare_dot_req__res_dot_get__attributes__of__symptom__and__disease__pb2._GETATTRIBUTESOFSYMPTOMANDDISEASERESPONSE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='GetContext',
    full_name='jio.brain.proto.knowledge.healthcare.HealthcareKnowledgeApiService.GetContext',
    index=18,
    containing_service=None,
    input_type=jio_dot_brain_dot_proto_dot_knowledge_dot_healthcare_dot_req__res_dot_get__context__pb2._GETCONTEXTREQUEST,
    output_type=jio_dot_brain_dot_proto_dot_knowledge_dot_healthcare_dot_req__res_dot_get__context__pb2._GETCONTEXTRESPONSE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='GetContextId',
    full_name='jio.brain.proto.knowledge.healthcare.HealthcareKnowledgeApiService.GetContextId',
    index=19,
    containing_service=None,
    input_type=jio_dot_brain_dot_proto_dot_knowledge_dot_healthcare_dot_req__res_dot_get__context__id__pb2._GETCONTEXTIDREQUEST,
    output_type=jio_dot_brain_dot_proto_dot_knowledge_dot_healthcare_dot_req__res_dot_get__context__id__pb2._GETCONTEXTIDRESPONSE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='GetContextValueId',
    full_name='jio.brain.proto.knowledge.healthcare.HealthcareKnowledgeApiService.GetContextValueId',
    index=20,
    containing_service=None,
    input_type=jio_dot_brain_dot_proto_dot_knowledge_dot_healthcare_dot_req__res_dot_get__context__value__id__pb2._GETCONTEXTVALUEIDREQUEST,
    output_type=jio_dot_brain_dot_proto_dot_knowledge_dot_healthcare_dot_req__res_dot_get__context__value__id__pb2._GETCONTEXTVALUEIDRESPONSE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='GetSymptomPatientState',
    full_name='jio.brain.proto.knowledge.healthcare.HealthcareKnowledgeApiService.GetSymptomPatientState',
    index=21,
    containing_service=None,
    input_type=jio_dot_brain_dot_proto_dot_knowledge_dot_healthcare_dot_req__res_dot_get__symptom__patient__state__pb2._GETSYMPTOMPATIENTSTATEREQUEST,
    output_type=jio_dot_brain_dot_proto_dot_knowledge_dot_healthcare_dot_req__res_dot_get__symptom__patient__state__pb2._GETSYMPTOMPATIENTSTATERESPONSE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='GetDiseasePatientState',
    full_name='jio.brain.proto.knowledge.healthcare.HealthcareKnowledgeApiService.GetDiseasePatientState',
    index=22,
    containing_service=None,
    input_type=jio_dot_brain_dot_proto_dot_knowledge_dot_healthcare_dot_req__res_dot_get__disease__patient__state__pb2._GETDISEASEPATIENTSTATEREQUEST,
    output_type=jio_dot_brain_dot_proto_dot_knowledge_dot_healthcare_dot_req__res_dot_get__disease__patient__state__pb2._GETDISEASEPATIENTSTATERESPONSE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='SearchSymptoms',
    full_name='jio.brain.proto.knowledge.healthcare.HealthcareKnowledgeApiService.SearchSymptoms',
    index=23,
    containing_service=None,
    input_type=jio_dot_brain_dot_proto_dot_knowledge_dot_healthcare_dot_req__res_dot_search__symptoms__pb2._SEARCHSYMPTOMSREQUEST,
    output_type=jio_dot_brain_dot_proto_dot_knowledge_dot_healthcare_dot_req__res_dot_search__symptoms__pb2._SEARCHSYMPTOMSRESPONSE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='SearchDiseases',
    full_name='jio.brain.proto.knowledge.healthcare.HealthcareKnowledgeApiService.SearchDiseases',
    index=24,
    containing_service=None,
    input_type=jio_dot_brain_dot_proto_dot_knowledge_dot_healthcare_dot_req__res_dot_search__diseases__pb2._SEARCHDISEASESREQUEST,
    output_type=jio_dot_brain_dot_proto_dot_knowledge_dot_healthcare_dot_req__res_dot_search__diseases__pb2._SEARCHDISEASESRESPONSE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='GetValidSymptomAttributeValuesGivenFilter',
    full_name='jio.brain.proto.knowledge.healthcare.HealthcareKnowledgeApiService.GetValidSymptomAttributeValuesGivenFilter',
    index=25,
    containing_service=None,
    input_type=jio_dot_brain_dot_proto_dot_knowledge_dot_healthcare_dot_req__res_dot_get__valid__symptom__attribute__values__given__filter__pb2._GETVALIDSYMPTOMATTRIBUTEVALUESGIVENFILTERREQUEST,
    output_type=jio_dot_brain_dot_proto_dot_knowledge_dot_healthcare_dot_req__res_dot_get__valid__symptom__attribute__values__given__filter__pb2._GETVALIDSYMPTOMATTRIBUTEVALUESGIVENFILTERRESPONSE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='GetDiseaseName',
    full_name='jio.brain.proto.knowledge.healthcare.HealthcareKnowledgeApiService.GetDiseaseName',
    index=26,
    containing_service=None,
    input_type=jio_dot_brain_dot_proto_dot_knowledge_dot_healthcare_dot_req__res_dot_get__disease__name__pb2._GETDISEASENAMEREQUEST,
    output_type=jio_dot_brain_dot_proto_dot_knowledge_dot_healthcare_dot_req__res_dot_get__disease__name__pb2._GETDISEASENAMERESPONSE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='GetSymptomName',
    full_name='jio.brain.proto.knowledge.healthcare.HealthcareKnowledgeApiService.GetSymptomName',
    index=27,
    containing_service=None,
    input_type=jio_dot_brain_dot_proto_dot_knowledge_dot_healthcare_dot_req__res_dot_get__symptom__name__pb2._GETSYMPTOMNAMEREQUEST,
    output_type=jio_dot_brain_dot_proto_dot_knowledge_dot_healthcare_dot_req__res_dot_get__symptom__name__pb2._GETSYMPTOMNAMERESPONSE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='GetAttributeValueName',
    full_name='jio.brain.proto.knowledge.healthcare.HealthcareKnowledgeApiService.GetAttributeValueName',
    index=28,
    containing_service=None,
    input_type=jio_dot_brain_dot_proto_dot_knowledge_dot_healthcare_dot_req__res_dot_get__attribute__value__name__pb2._GETATTRIBUTEVALUENAMEREQUEST,
    output_type=jio_dot_brain_dot_proto_dot_knowledge_dot_healthcare_dot_req__res_dot_get__attribute__value__name__pb2._GETATTRIBUTEVALUENAMERESPONSE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='GetContextName',
    full_name='jio.brain.proto.knowledge.healthcare.HealthcareKnowledgeApiService.GetContextName',
    index=29,
    containing_service=None,
    input_type=jio_dot_brain_dot_proto_dot_knowledge_dot_healthcare_dot_req__res_dot_get__context__name__pb2._GETCONTEXTNAMEREQUEST,
    output_type=jio_dot_brain_dot_proto_dot_knowledge_dot_healthcare_dot_req__res_dot_get__context__name__pb2._GETCONTEXTNAMERESPONSE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='GetContextValueName',
    full_name='jio.brain.proto.knowledge.healthcare.HealthcareKnowledgeApiService.GetContextValueName',
    index=30,
    containing_service=None,
    input_type=jio_dot_brain_dot_proto_dot_knowledge_dot_healthcare_dot_req__res_dot_get__context__value__name__pb2._GETCONTEXTVALUENAMEREQUEST,
    output_type=jio_dot_brain_dot_proto_dot_knowledge_dot_healthcare_dot_req__res_dot_get__context__value__name__pb2._GETCONTEXTVALUENAMERESPONSE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
])
_sym_db.RegisterServiceDescriptor(_HEALTHCAREKNOWLEDGEAPISERVICE)

DESCRIPTOR.services_by_name['HealthcareKnowledgeApiService'] = _HEALTHCAREKNOWLEDGEAPISERVICE

# @@protoc_insertion_point(module_scope)
