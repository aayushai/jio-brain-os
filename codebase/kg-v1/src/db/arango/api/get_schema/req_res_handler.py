import json
import logging as logger
from db.arango.utils.config import *
from db.arango.api.get_schema.query import *

'''
the pre_processing_function takes the static request as input
and generates the arangoDb query.
i/p: request
o/p: query,status
'''
def pre_process_function(request):
	logger.debug(PREPROCESSING)
	
	query_dict = {}
	query_dict["query_type"] = QueryType.Multi
	brain_status["is_ok"] = True
	brain_status["brain_status_instance"][0]["parameters"]["msg"] = "no error"

	queries = []

	collection_name = request.collection_name
	_query = query%(collection_name)
	_query_attr = query_req_attributes%(collection_name)
	queries.append(_query)
	queries.append(_query_attr)

	query_dict["query"] = queries
	logger.info(PREPROCESSING_COMPLETED)
	return query_dict,brain_status

		
'''
the post_process_function takes the arango response and status as the
input and sets the status and returns the appropritate response.
i/p:cursor,status
o/p:response
'''
def post_process_function(cursor, status):
	logger.debug(POSTPROCESSING)
	cursor[0][0]["required_attributes"] = cursor[1][0]
	return cursor, status