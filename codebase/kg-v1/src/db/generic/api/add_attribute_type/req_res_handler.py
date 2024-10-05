import logging as logger
from db.arango.dao.db_init import arango
from kgschemalib import SchemaClient
from db.generic.api.add_collection_type.config import *
from google.protobuf.json_format import MessageToDict
from jio.brain.proto.knowledge.api.schema.add_attribute_type_pb2 import AddAttributeTypeResponse


def pre_process_function(request):
	logger.debug(PREPROCESSING)

	is_valid, msg = validate(request)

	if not is_valid:
		brain_status["is_ok"] = is_valid
		brain_status["brain_status_instance"][0]["parameters"]["msg"] = msg
		logger.debug(PREPROCESSING_INCOMPLETE)
		return None, None, brain_status
	
	logger.info(PREPROCESSING_COMPLETED)    
	return request,None,brain_status


def validate(request):
	logger.debug(VALIDATION)
	if request.collection_type is None or request.attribute_name is None or request.attribute_schema is None or request.attribute_required is None:
		logger.error(INPUT_PARAMETER_COUNT_ERROR)
		return False,INPUT_PARAMETER_COUNT_ERROR
	else:
		logger.info(VALIDATED)
		return True,None 


def post_process_function(cursor,status):
	logger.debug(POSTPROCESSING)
	if status['is_ok']:
		try:
			cursor = cursor["static_cursor"][0]
			update_schema(cursor)
		except Exception as e:
			brain_status["brain_status_instance"][0]["parameters"]["msg"] = "Schema Update Error!"

	response = AddAttributeTypeResponse(status = status)
	logger.info(POSTPROCESSING_COMPLETED)
	return response


def update_schema(cursor):
	collection_name = cursor.collection_type
	attribute_name = cursor.attribute_name
	attribute = MessageToDict(cursor)["attributeSchema"]
	static_attributes = []
	dynamic_attributes = []
	if (list(attribute.keys())[0]).lower() == "static":
		attribute_type = "static"
		static_attributes = attribute_name
	else:
		attribute_type = "dynamic"
		dynamic_attributes = attribute_name

	quantity_type = list(attribute[attribute_type]["schema"]["properties"].keys())[0]

	attribute_param = {}
	schema_attribute = {}
	schema_entity_predicate = {}

	schema_attribute["%s"%attribute_name] = [attribute_type,quantity_type]
	if(static_attributes == []):
		schema_entity_predicate["static_attributes"] = []
	else:
		schema_entity_predicate["static_attributes"] = [static_attributes]
	if(dynamic_attributes == []):
		schema_entity_predicate["dynamic_attributes"] = []
	else:
		schema_entity_predicate["dynamic_attributes"] = [dynamic_attributes]

	attribute_param = {"collection_name":collection_name,"schema_attribute":schema_attribute}
	entity_predicate_param = {"collection_name":collection_name, "schema_entity_predicate":schema_entity_predicate}
	client = SchemaClient(arango.host,arango.db_name,arango.username,arango.password)
	client.add_attribute_type(attribute_param, entity_predicate_param)