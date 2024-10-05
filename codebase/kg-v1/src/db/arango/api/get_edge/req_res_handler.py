from db.arango.api.get_edge.query import query
from db.arango.api.get_edge.config import *
import logging as logger

'''
The pre_process_function takes in the static request and generates the arango query
i/p: static request
o/p: arrange_query and status
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

	query_dict = {}
	query_dict["query_type"] = QueryType.Query
	edge_collection = request.edge_collection
	from_id = request.from_id
	to_id = request.to_id
	brain_status["is_ok"] = True
	brain_status["brain_status_instance"][0]["parameters"]["msg"] = "no error"
	try:
		query_dict["query"] = query%(edge_collection, from_id, to_id)		
	except Exception as e:
		brain_status["is_ok"] = False
		## TODO : move this to BrainStatusInstance Object
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
	if(cursor == []):
		brain_status["is_ok"] = False
		brain_status["brain_status_instance"][0]["parameters"]["msg"] = "Set of ids has no exact match"
	print(brain_status)
	return cursor, brain_status
	