import json
from db.arango.api.add_predicate.query import query
from google.protobuf.json_format import MessageToDict
from db.arango.utils.config import *
from test.api.add_predicate.client import logger

'''
The pre_process_function takes in the static request and generates the arango query
i/p: static reqest
o/p: arango_query and brain_status
'''
def pre_process_function(request):
	logger.debug(PREPROCESSING)
	query_dict = {}
	query_dict["query_type"] = QueryType.Query
	predicate = request.predicate
	from_entity_id = request.from_entity_id
	to_entity_id = request.to_entity_id
	predicate_name = predicate.predicate_name
	attribute_value = predicate.attributes

	brain_status["is_ok"] = True
	brain_status["brain_status_instance"][0]["parameters"]["msg"] = "no error"
	attribute_str = json.dumps(dict([(key, MessageToDict(value)) for key,value in attribute_value.items()]))

	try:
		_query = query%(from_entity_id,to_entity_id,predicate_name,attribute_str,predicate_name)

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

	return cursor, brain_status