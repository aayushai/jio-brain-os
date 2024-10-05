import json
import logging as logger
from db.arango.utils.config import *
from db.arango.api.get_entities_with_canonical_name.query import query
'''
The pre_process_function takes in the static request and generates the arango query
i/p: static reqest
o/p: arango_query and status
'''
def pre_process_function(request):
	logger.debug(PREPROCESSING)
	query_dict = {}
	query_dict["query_type"] = QueryType.Query
	brain_status["is_ok"] = True
	brain_status["brain_status_instance"][0]["parameters"]["msg"] = "no error"

	entity_type = request.entity_type
	canonical_name = request.canonical_name

	language_proto = request.language
	language_val = language_proto.language

	try:
		_query = query%(entity_type, language_val, canonical_name)
		query_dict["query"] = _query

	except Exception as e:
		brain_status["is_ok"] = False
		brain_status["brain_status_instance"][0]["parameters"]["msg"] = str(e)
		logger.error(e)
		return None,brain_status

	logger.info(PREPROCESSING_COMPLETED)
	return query_dict,brain_status 

'''
the post_process_function checks the response from arango 
and returns a response along with a status(if all went okay or some error occured)
i/p: response from arango -> list containing entity_id of added entity OR the error message
o/p: entity_id of entity and status OR Error Message with status
'''		

def post_process_function(cursor, brain_status):
	logger.debug(POSTPROCESSING)
	
	return cursor, brain_status