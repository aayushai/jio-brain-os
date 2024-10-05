import json
import logging as logger
from db.arango.utils.config import *
from db.arango.api.add_attribute.query import *
from google.protobuf.json_format import MessageToDict

'''
the pre_processing_function takes the static request as input
and generates the arangoDb query.
i/p: request
o/p: query,status
'''
def pre_process_function(request):
	logger.debug(PREPROCESSING)

	query_dict = {}
	query_dict["query_type"] = QueryType.Query
	brain_status["is_ok"] = True
	brain_status["brain_status_instance"][0]["parameters"]["msg"] = "no error"
	
	req =  str(request)
	is_valid, msg = validate(req)
	if not is_valid:
		brain_status["is_ok"] = is_valid
		brain_status["brain_status_instance"][0]["parameters"]["msg"] = msg
		logger.debug(PREPROCESSING_INCOMPLETE)
		return None, status

	entity_type = request.entity_id.split("/")[0].strip()
	entity_id = request.entity_id.split("/")[1].strip()
	attribute_name = request.attribute_name 

	attribute_val = request.attribute_value
	attribute_type_static = MessageToDict(attribute_val)
	
	_query = query%(entity_type+"/"+entity_id,attribute_name,attribute_type_static,entity_type)
	query_dict["query"] = _query
	logger.info(PREPROCESSING_COMPLETED)

	return query_dict, brain_status

'''
Validate method checks if all the required inputs are present
it returns an Input parameter count error if not
i/p: string(request)
o/p:flag,error message
'''
def validate(req):
	logger.debug(VALIDATION)

	if "entity_id" in req and "attribute" in req:
		logger.info(VALIDATED)
		return True,None 

	else:
		logger.error(INPUT_PARAMETER_COUNT_ERROR)
		return False,INPUT_PARAMETER_COUNT_ERROR
		
'''
the post_process_function takes the arango response and status as the
input and sets the status and returns the appropritate response.
i/p:cursor,status
o/p:Response
'''
def post_process_function(cursor, status):
	logger.debug(POSTPROCESSING)

	return cursor, status