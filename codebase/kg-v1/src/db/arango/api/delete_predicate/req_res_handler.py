import json
from db.arango.api.delete_predicate.query import query
from google.protobuf.json_format import MessageToDict
from db.arango.utils.config import *
import logging as logger

'''
The pre_process_function takes in the static request and generates the arango query
i/p: static reqest
o/p: arango_query and brain_status
'''
def pre_process_function(request):
	logger.debug(PREPROCESSING)
	query_dict = {}
	query_dict["query_type"] = QueryType.Query

	from_entity_id = request.from_entity_id
	to_entity_id = request.to_entity_id
	predicate_name = request.predicate_name

	brain_status["is_ok"] = True
	brain_status["brain_status_instance"][0]["parameters"]["msg"] = "no error"

	try:
		_query = query%(predicate_name, from_entity_id, to_entity_id, predicate_name)

	except Exception as e:
		brain_status["is_ok"] = False
		brain_status["brain_status_instance"][0]["parameters"]["msg"] = str(e)
		brain_status["brain_status_instance"][0]["parameters"]["msg"] = str(e)
		logger.error(e)
		return None,brain_status
	
	query_dict["query"] = _query
	logger.info(PREPROCESSING_COMPLETED)
	print(query_dict)
	return query_dict,brain_status 

'''
the post_process_function checks the response from arango 
and returns a response along with a brain_status(if all went okay or some error occured)
i/p: response from arango -> list containing entity_id of added entity OR the error message
o/p: entity_id of entity and brain_status OR Error Message with brain_status
'''		

def post_process_function(cursor, brain_status):
	logger.debug(POSTPROCESSING)
	if(cursor == []):
		brain_status["brain_status_instance"][0]["parameters"]["msg"] = "Check the Entity IDs or the Predicate has already been deleted."
	else:
		brain_status["brain_status_instance"][0]["parameters"]["msg"] = PREDICATE_DELETED
	return cursor, brain_status