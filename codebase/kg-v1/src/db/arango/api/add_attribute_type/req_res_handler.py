from google.protobuf.json_format import MessageToDict
import logging as logger
from .config import *


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
	query_dict["query_type"] = QueryType.AddAttributeType
	query_dict["request"] = request
	query_dict["collection_type"] = request.collection_type
	query_dict["attribute_name"] = request.attribute_name
	
	attribute_schema = request.attribute_schema
		
	query_dict["attribute_schema"] = MessageToDict(attribute_schema)
	query_dict["attribute_required"] = request.attribute_required

	logger.info(PREPROCESSING_COMPLETED) 
	return query_dict, brain_status


def post_process_function(cursor,status):
	logger.debug(POSTPROCESSING)
	
	if status["is_ok"]:
		status["brain_status_instance"][0]["status_code"] = BrainStatusCode.KNOWLEDGE_GRAPH_ATTRIBUTE_ADDED
		status["brain_status_instance"][0]["parameters"]["msg"] = "Attribute type added to schema"

	return cursor,status