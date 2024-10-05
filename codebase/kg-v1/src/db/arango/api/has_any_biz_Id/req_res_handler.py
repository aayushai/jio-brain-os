from db.arango.api.has_any_biz_id.query import query
import json
from db.arango.api.has_any_biz_id.config import *
import logging as logger

'''
The pre_process_function takes in the static request and generates the arango query
i/p: static reqest
o/p: arango_query and status
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
	query_dict = {}
	query_dict["query_type"] = QueryType.Query
	try:
		_query = query%(entity_id)
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
the post_process_function checks the response from arango 
and returns a response along with a status(if all went okay or some error occured)
i/p: response from arango -> list containing entity_id of added entity OR the error message
o/p: entity_id of entity and status OR Error Message with status
'''		

def post_process_function(cursor, brain_status):
	logger.debug(POSTPROCESSING)
	print(cursor)
	try:
		if brain_status["is_ok"]:
			if cursor == [None] or cursor == [] or cursor is None:	
				brain_status["is_ok"] = True
				brain_status["brain_status_instance"][0]["parameters"]["msg"] = NOT_HAVE_BIZ_ID
				logger.error(brain_status["brain_status_instance"][0]["parameters"]["msg"])

			
		return cursor, brain_status
		
	except Exception as e:
		logger.error(e)
		return str(e)