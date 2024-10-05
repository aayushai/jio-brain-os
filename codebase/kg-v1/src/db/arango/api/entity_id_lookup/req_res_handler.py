import json
import humps
import logging as logger
from db.arango.utils.config import *
from db.arango.api.entity_id_lookup.query import *

'''
The pre_process_function takes in the static request and generates the arango query
i/p: static reqest
o/p: arango_query and brain_status
'''
def pre_process_function(request):
	logger.debug(PREPROCESSING)
	collection_name = request.key
	brain_id = int(request.id)

	_query = query%(collection_name, brain_id)

	query_ = {}
	query_["query_type"] = QueryType.Query
	query_["query"] = _query
	query_["request"] = request

	logger.info(PREPROCESSING_COMPLETED)
	return query_,brain_status 

'''
the post_process_function checks the response from arango 
and returns a response along with a brain_status(if all went okay or some error occured)
i/p: response from arango -> list containing entity_id of added entity OR the error message
o/p: entity_id of entity and brain_status OR Error Message with brain_status
'''		
	
def post_process_function(cursor, brain_status):

	return cursor, brain_status