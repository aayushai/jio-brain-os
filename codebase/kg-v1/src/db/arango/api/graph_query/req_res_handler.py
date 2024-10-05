import json
import logging as logger
from db.arango.utils.config import *
from jio.brain.proto.knowledge.api.data.graph_query_pb2 import GraphQueryResponse

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

	query = request.query
	query_dict = {}
	query_dict["query_type"] = QueryType.Query
	query_dict["query"] = query

	logger.info(PREPROCESSING_COMPLETED)

	return query_dict, brain_status

'''
the post_process_function takes the arango response and status as the
input and sets the status and returns the appropritate response.
i/p:cursor,status
o/p:response
'''
def post_process_function(cursor, brain_status):
	if not cursor or None in cursor:
		brain_status["is_ok"] = False
		brain_status["brain_status_instance"][0]["parameters"]["msg"] = "No match found in database"
	cursor = str(cursor)	
	print(brain_status)
	return cursor, brain_status
