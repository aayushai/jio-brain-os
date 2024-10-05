import json
import logging as logger
from db.arango.utils.config import *
from db.arango.api.get_predicate.query import query

'''
The pre_process_function takes in the static request and generates the arango query
i/p: static reqest
o/p: arango_query and brain_status
'''
def pre_process_function(request):
	logger.debug(PREPROCESSING)
	query_dict = {}
	query_dict["query_type"] = QueryType.Query
	collection_name = request.collection_name
	predicate_type = collection_name

	_from = request.from_id
	_to = request.to_id
	brain_status["is_ok"] = True
	brain_status["brain_status_instance"][0]["parameters"]["msg"] = "no error"
	try:
		_query = query%(predicate_type,_from,_to)
		query_dict["query"] = _query
	except Exception as e:
		brain_status["is_ok"] = False
		brain_status["brain_status_instance"][0]["parameters"]["msg"] = str(e)
		logger.error(e)
		return None,brain_status
	print(query_dict)
	logger.info(PREPROCESSING_COMPLETED)
	return query_dict,brain_status 

'''
the post_process_function checks the response from arango 
and returns a response along with a brain_status(if all went okay or some error occured)
i/p: response from arango -> list containing entity_id of added entity OR the error message
o/p: entity_id of entity and brain_status OR Error Message with brain_status
'''		

def post_process_function(cursor, brain_status):
	logger.debug(POSTPROCESSING)
	try:
		if brain_status["is_ok"]:
			if cursor == []:
				brain_status["is_ok"] = False
				brain_status["brain_status_instance"][0]["parameters"]["msg"] = ERROR_MESSAGE
				logger.debug(ERROR_MESSAGE)
		
		logger.info(POSTPROCESSING_COMPLETED)
		return cursor, brain_status

	except Exception as e:
		logger.error(e)
		brain_status["is_ok"] = False
		brain_status["brain_status_instance"][0]["parameters"]["msg"] = str(e)
		return cursor, brain_status