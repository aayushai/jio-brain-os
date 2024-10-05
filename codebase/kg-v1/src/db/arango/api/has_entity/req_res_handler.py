from db.arango.api.has_entity.query import query
import json
from db.arango.api.has_entity.config import *
import logging as logger
import sys
'''
The pre_process_function takes in the static request and generates the arango query
i/p: static reqest
o/p: arango_query and status
'''
def pre_process_function(request):
	logger.debug(PREPROCESSING)
	brain_status = {
		"is_ok": True,
		"brain_status_instance": [{
			"status_code": BrainStatusCode.BRAIN_STATUS_CODE_OK,
			"parameters": {
				"NO_ERROR": "no error"
			}
		}]
	}

	query_dict = {}
	query_dict["query_type"] = QueryType.Query
	entity_id = request.entity_id

	_query = query%(entity_id)
	query_dict["query"] = _query
	logger.info(PREPROCESSING_COMPLETED)
	
	return query_dict,brain_status 


def post_process_function(cursor, brain_status):
	logger.debug(POSTPROCESSING)

	try:
		if  brain_status["is_ok"]:
			if cursor == [None]:
				brain_status["is_ok"] = False
				# brain_status["brain_status_instance"][0]["parameters"]["msg"] = NOT_HAVE_ENTITY
				parameters = {
					"NOT_PRESENT": "Entity"
				}
				brain_status["brain_status_instance"][0]["parameters"] = parameters
				logger.error(brain_status["brain_status_instance"][0]["parameters"]["NOT_PRESENT"])

			
		return cursor, brain_status
		
	except Exception as e:
		logger.error(e)
		return str(e)