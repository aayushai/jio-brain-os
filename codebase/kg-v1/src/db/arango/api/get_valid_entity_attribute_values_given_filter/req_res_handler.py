import json
import logging as logger
from db.arango.utils.config import *
from db.arango.api.get_valid_entity_attribute_values_given_filter.query import *

'''
the preprocess_function takes the static request as input and generates the 
arango query and returns the query to the DAO layer.
i/p: static request
o/p: query, brain_status
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

	entity_id = request.entity_id
	entity_type  = request.entity_type  
	context_id  = request.context_id
	attribute_id = request.attribute_id 

	print(entity_id, context_id, entity_type, attribute_id)

	if not context_id:
		_query = query_without_context%(entity_id, entity_type, attribute_id)
	else:
		_query = query_with_context%(entity_id, context_id, entity_type, attribute_id)

	query_dict["query"] = _query
	logger.info(PREPROCESSING_COMPLETED)
	return query_dict,brain_status
'''
The validate method checks if the request has the entity id or not
It returns back a count error if the entity_id is missing.
'''
def validate(req):
	logger.debug(VALIDATION)

	if "entity_id" in req and "entity_type" in req and "attribute_id" in req:
		logger.info(VALIDATED)
		return True, None
	else:
		logger.error(INPUT_PARAMETER_COUNT_ERROR)
		return False, INPUT_PARAMETER_COUNT_ERROR

'''
the post_process_function takes the arango response and stautus as input and furthur
evaluates for any errors and returns a brain_status
i/p: arango response, brain_status
o/p: brain_status
'''
def post_process_function(cursor, brain_status):
	cursor = cursor[0]
	if(cursor == []):
		brain_status["is_ok"] = False
		brain_status["brain_status_instance"][0]["parameters"]["msg"] = "No exact match found in database"
	print(brain_status)
	return cursor, brain_status