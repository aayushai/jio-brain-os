import logging as logger
from db.arango.dao.db_init import arango
from kgschemalib import SchemaClient
from db.generic.api.add_collection_type.config import *
from google.protobuf.json_format import MessageToDict
from jio.brain.proto.knowledge.api.schema.add_collection_type_pb2 import AddCollectionTypeResponse
from db.generic.api.add_collection_type.datatype_store import data_types

def pre_process_function(request):
	logger.debug(PREPROCESSING)

	is_valid, msg = validate(request)
	if not is_valid:
		brain_status["is_ok"] = is_valid
		brain_status["brain_status_instance"][0]["parameters"]["msg"] = msg
		logger.debug(PREPROCESSING_INCOMPLETE)
		return None, None, brain_status

	dynamic_request = None
	
	logger.info(PREPROCESSING_COMPLETED)    
	return request,dynamic_request,brain_status


def validate(request):
	logger.debug(VALIDATION)
	if request.vertical is None or request.collection_name is None or request.is_predicate is None or request.schema is None:
		logger.error(INPUT_PARAMETER_COUNT_ERROR)
		return False,INPUT_PARAMETER_COUNT_ERROR
	else:
		logger.info(VALIDATED)
		return True,None 


def post_process_function(cursor,status):
	logger.debug(POSTPROCESSING)
	
	if status['is_ok']:
		cursor = cursor["static_cursor"][0]
		update_schema(cursor)

	response = AddCollectionTypeResponse(status = status)
	logger.info(POSTPROCESSING_COMPLETED)
	return response


def update_schema(cursor):
	vertical = cursor.vertical
	entity_type = cursor.collection_name
	collection_name = vertical+NAMESPACE_DELIMITER+entity_type
	is_predicate = cursor.is_predicate

	schema = MessageToDict(cursor.schema)

	schema_entity_predicate = {}
	schema_entity_predicate["static_attributes"] = list(schema['static'].keys())
	schema_entity_predicate["dynamic_attributes"] = list(schema['dynamic'].keys())


	schema_attribute = {}

	for static_attribute in schema_entity_predicate["static_attributes"]:
		schema_attribute[static_attribute] = ["static",list(schema['static'][static_attribute]['schema']['properties'].keys())[0]]

	for dynamic_attribute in schema_entity_predicate["dynamic_attributes"]:
		schema_attribute[dynamic_attribute] = ["dynamic",list(schema['dynamic'][dynamic_attribute]['schema']['properties'].keys())[0]]

	vertical_param = {"is_predicate":is_predicate,"vertical":vertical,"entity_type":entity_type}
	attribute_param = {"collection_name":collection_name,"schema_attribute":schema_attribute}
	entity_predicate_param = {"collection_name":collection_name, "schema_entity_predicate":schema_entity_predicate}
	client = SchemaClient(arango.host,arango.db_name,arango.username,arango.password)
	client.add_collection_type(vertical_param,attribute_param,entity_predicate_param)