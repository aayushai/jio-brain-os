import json
import logging as logger
from db.arango.utils.config import *
from db.arango.api.get_all_biz_id_types_of_entity_id.query import query
'''
the pre_processing_function takes the static request as input
and generates the arangoDb query.
i/p: request
o/p: query,brain_status
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
		query_dict["query"] = None

		logger.debug(PREPROCESSING_INCOMPLETE)
		return query_dict, brain_status

	entity_id = request.entity_id
	_query = query%(entity_id)
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
		logger.info(VALIDATED)
		return True, None
	else:
		logger.error(INPUT_PARAMETER_COUNT_ERROR)
		return False, INPUT_PARAMETER_COUNT_ERROR

'''
the post_process_function takes the arango response and brain_status as the
input and sets the brain_status and returns the appropritate response.
i/p:cursor,brain_status
o/p:response
'''
def post_process_function(cursor, brain_status):
	logger.debug(POSTPROCESSING)

	return cursor, brain_status