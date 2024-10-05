import json
import logging as logger
from db.arango.utils.config import *
from db.arango.api.get_entity.query import query

'''
the preprocess_function takes the static request as input and generates the 
arango query and returns the query to the DAO layer.
i/p: static request
o/p: query, brain_status
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

	entity_id = request.entity_id
	_query = query%(entity_id)

	query_dict["query"] = _query
	print(query_dict)
	logger.info(PREPROCESSING_COMPLETED)
	return query_dict,brain_status
'''
The validate method checks if the request has the entity id or not
It returns back a count error if the entity_id is missing.
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
the post_process_function takes the arango response and stautus as input and furthur
evaluates for any errors and returns a brain_status
i/p: arango response, brain_status
o/p: brain_status
'''
def post_process_function(cursor, brain_status):
	logger.debug(POSTPROCESSING)
	
	try:
		if not brain_status["is_ok"]:
			brain_status["brain_status_instance"][0]["parameters"]["msg"] = ERROR_MESSAGE + brain_status["brain_status_instance"][0]["parameters"]["msg"]
			logger.error(brain_status["brain_status_instance"][0]["parameters"]["msg"])
			
		else:
			if str(cursor) == "[{'entity_type': None, 'biz_id': None, 'name': None, 'attributes': None}]":
				brain_status["brain_status_instance"][0]["parameters"]["msg"] = ERROR_MESSAGE
				brain_status["is_ok"] = False
			
		return cursor, brain_status
		
	except Exception as e:
		logger.error(e)
		return str(e)