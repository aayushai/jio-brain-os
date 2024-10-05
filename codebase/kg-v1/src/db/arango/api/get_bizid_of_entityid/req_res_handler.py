from db.arango.api.get_bizid_of_entityid.query import query
import json
from db.arango.api.get_bizid_of_entityid.config import *
import logging as logger
'''
the pre_processing_function takes the static request as input
and generates the arangoDb query.
i/p: request
o/p: query,status
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
	biz_id_type = request.biz_type

	query_dict = {}
	query_dict["query_type"] = QueryType.Query

	try:
		_query = query%(entity_id, biz_id_type)
	except Exception as e:
		brain_status["is_ok"] = False
		brain_status["brain_status_instance"][0]["parameters"]["msg"] = str(e)
		logger.error(e)
		return None,brain_status
	
	query_dict["query"] = _query

	print(query_dict)
	logger.info(PREPROCESSING_COMPLETED)
	return query_dict,brain_status 

'''
the post_process_function takes the arango response and status as the
input and sets the status and returns the appropritate response.
i/p:cursor,status
o/p:response
'''
def post_process_function(cursor, brain_status):
	logger.debug(POSTPROCESSING)
	print(cursor)

	return cursor, brain_status

