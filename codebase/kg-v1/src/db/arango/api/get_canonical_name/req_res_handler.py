from db.arango.api.get_canonical_name.query import query
import json
from db.arango.api.get_canonical_name.config import *
import logging as logger
'''
the pre_processing_function takes the static request as input
and generates the arangoDb query.
i/p: request
o/p: query,status
'''
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
	
	entity_id = request.entity_id
	language = request.language.language
	is_valid, msg = validate(request)

	query_dict = {}
	query_dict["query_type"] = QueryType.Query
	if not is_valid:
		brain_status["is_ok"] = is_valid
		brain_status["brain_status_instance"][0]["parameters"]["msg"] = msg
		_query = None

		logger.debug(PREPROCESSING_INCOMPLETE)
		return _query, brain_status

	try:
		_query = query%(entity_id, language)
	except Exception as e:
		brain_status["is_ok"] = False
		brain_status["brain_status_instance"][0]["parameters"]["msg"] = str(e)
		logger.error(e)
		return None,brain_status

	print(_query)
	query_dict["query"] = _query
	logger.info(PREPROCESSING_COMPLETED)
	return query_dict,brain_status 

'''
Validate method checks if all the required inputs are present
it returns an Input parameter count error if not
i/p: string(request)
o/p:flag,error message
'''
def validate(request):
	logger.debug(VALIDATION)

	if request.entity_id and request.language :
		logger.info(VALIDATED)
		return True, None
	else:
		logger.error("INPUT_PARAMETER_COUNT_ERROR")
		return False, "INPUT_PARAMETER_COUNT_ERROR"
'''
the post_process_function takes the arango response and status as the
input and sets the status and returns the appropritate response.
i/p:cursor,status
o/p:response
'''


def post_process_function(cursor, brain_status):
	logger.debug(POSTPROCESSING)
	
	try:
		if  brain_status["is_ok"]:
			if cursor == [None]:	
				brain_status["is_ok"] = False
				brain_status["brain_status_instance"][0]["parameters"]["msg"] = NOT_HAVE_CANONICAL_NAME
				logger.error(brain_status["brain_status_instance"][0]["parameters"]["msg"])

			else:
				brain_status["brain_status_instance"][0]["parameters"]["msg"] = CANONICAL_NAME
		
		return cursor, brain_status
		
	except Exception as e:
		logger.error(e)
		return str(e)

