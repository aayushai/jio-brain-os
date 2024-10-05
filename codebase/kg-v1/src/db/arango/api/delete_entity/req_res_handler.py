import json
import logging as logger
from db.arango.utils.config import *
from db.arango.api.delete_entity.query import query

'''
the pre_processing_function takes the static request as input
and generates the arangoDb query.
i/p: request
o/p: query,status
'''
def pre_process_function(request):
	logger.debug(PREPROCESSING)
	req =  str(request)
	is_valid, msg = validate(req)
	query_dict = {}
	query_dict["query_type"] = QueryType.Query
	if not is_valid:
		brain_status["is_ok"] = is_valid
		brain_status["brain_status_instance"][0]["parameters"]["msg"] = msg
		_query = None

		logger.debug(PREPROCESSING_INCOMPLETE)
		return _query, brain_status

	brain_status["is_ok"] = True
	brain_status["brain_status_instance"][0]["parameters"]["msg"] = "no error"

	entity_id = request.entity_id
	key = entity_id.split("/")[1].strip()
	entity_type = entity_id.split("/")[0].strip()
	
	_query = query%(key,entity_type)

	query_dict["query"] = _query
	logger.info(PREPROCESSING_COMPLETED)
	return query_dict,brain_status

'''
Validate method checks if all the required inputs are present
it returns an Input parameter count error if not
i/p: string(request)
o/p:flag,error message
'''
def validate(req):
	logger.debug(VALIDATION)

	if "entity_id" in req:
		logger.debug(VALIDATED)
		return True, None
	else:
		logger.info(INPUT_PARAMETER_COUNT_ERROR)
		return False, INPUT_PARAMETER_COUNT_ERROR
		
'''
the post_process_function takes the arango response and status as the
input and sets the status and returns the appropritate response.
i/p:cursor,status
o/p:response
'''
def post_process_function(cursor, status):
	logger.debug(POSTPROCESSING)
	try:
		if status["is_ok"]:
			if cursor:
				status["brain_status_instance"][0]["parameters"]["msg"] = ENTITY_DELETED
			else:
				status["brain_status_instance"][0]["parameters"]["msg"] = ENTITY_DOES_NOT_EXIST
		else:
			status["brain_status_instance"][0]["parameters"]["msg"] = ERROR_MESSAGE + status["brain_status_instance"][0]["parameters"]["msg"]
			logger.error(status["brain_status_instance"][0]["parameters"]["msg"])
		
		logger.info(POSTPROCESSING_COMPLETED)
		return cursor, status
	
	except Exception as e:
		logger.error(e)
		return None, str(e)