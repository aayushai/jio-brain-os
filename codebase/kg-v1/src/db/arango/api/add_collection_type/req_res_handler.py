import logging as logger
from db.arango.api.add_collection_type.config import *
from google.protobuf.json_format import MessageToDict
from .schema_store import *
from .schema import *
from .datatype_store import *
from pprint import pprint

def pre_process_function(request):
	logger.debug(PREPROCESSING)
	
	brain_status = {
		"is_ok": True,
		"brain_status_instance": [{
			"status_code": BrainStatusCode.BRAIN_STATUS_CODE_OK,
			"parameters": {
				"msg": "no error"
			}
		}]
	}

	query_dict = {}
	query_dict["request"] = request
	static_request = build_static_request(request)

	vertical = static_request["vertical"]
	entity_type = static_request["collectionName"]
	collection_name = vertical+NAMESPACE_DELIMITER+entity_type
	is_predicate = static_request["isPredicate"]
	schema = static_request["schema"]
	
	query_dict["query_type"] = QueryType.AddType
	query_dict["collection_name"] = collection_name
	query_dict["edge_variable"] = is_predicate
	query_dict["schema"] = schema
	
	logger.info(PREPROCESSING_COMPLETED)
	return query_dict, brain_status


def build_static_request(request):
	logger.debug(BUILD_STATIC_REQ)
	
	is_predicate = request.is_predicate
	request = MessageToDict(request)
	schema = {}

	if is_predicate is False:
		request["isPredicate"] = False
		schema = entity_schema

	else:
		schema = predicate_schema
	static_attributes = request["schema"]['static']
	schema["rule"]["properties"]["attributes"]["required"] = []
	schema["rule"]["properties"]["attributes"]["properties"] = {}
	
	for attribute in static_attributes:
		is_required_attribute = request["schema"]["static"][attribute]["is_required"]
		schema["rule"]["properties"]["attributes"]["properties"][attribute] = request["schema"]["static"][attribute]["schema"]
		if is_required_attribute :
			schema["rule"]["properties"]["attributes"]["required"].append(attribute)

	if not schema["rule"]["properties"]["attributes"]["required"]:
		logger.info("Required Attributes are empty")
		schema["rule"]["properties"]["attributes"].pop('required', None)

	request["schema"] = schema
	logger.info(STATIC_REQ_BUILT)
	return request


def post_process_function(cursor,status):
	logger.debug(POSTPROCESSING)
	
	if status["is_ok"]:
		status["brain_status_instance"][0]["status_code"] = BrainStatusCode.KNOWLEDGE_GRAPH_COLLECTION_ADDED
		
	return cursor,status
