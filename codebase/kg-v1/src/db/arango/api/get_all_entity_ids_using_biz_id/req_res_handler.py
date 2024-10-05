from google.protobuf.json_format import MessageToDict
from db.arango.utils.config import QueryType
import json
from .config import *
import logging as logger
from db.arango.api.get_all_entity_ids_using_biz_id.query import query
'''
the pre_processing_function takes the static request as input
and generates the arangoDb query.
i/p: request
o/p: query,status
'''
def pre_process_function(request):
	logger.debug(PREPROCESSING)
	query_dict = {}
	query_dict["query_type"] = QueryType.Query
	req =  str(request)
	is_valid, msg = validate(req)
	
	if not is_valid:
		brain_status["is_ok"] = is_valid
		brain_status["brain_status_instance"][0]["parameters"]["msg"] = BrainStatusCode.BRAIN_STATUS_CODE_INVALID_DATA
		logger.debug(PREPROCESSING_INCOMPLETE)
		return None, brain_status

	biz_id = request.biz_id
	collecttion_name = request.collection_name
	print(biz_id.type)
	_query = query%(collecttion_name,biz_id.type, biz_id.value)
	query_dict["query"] = _query
	brain_status["is_ok"] = True
	brain_status["brain_status_instance"][0]["parameters"]["msg"] = "no error"
	logger.info(PREPROCESSING_COMPLETED)
	return query_dict,brain_status 

'''
Validate method checks if all the required inputs are present
it returns an Input parameter count error if not
i/p: string(request)
o/p:flag,error message
'''
def validate(req):
	logger.debug(VALIDATION)

	if "collection_name" in req and "biz_id" in req:
		logger.info(VALIDATED)
		return True, None
	else:
		logger.error(INPUT_PARAMETER_COUNT_ERROR)
		return False, INPUT_PARAMETER_COUNT_ERROR



'''
the post_process_function takes the arango response and status as the
input and sets the status and returns the appropritate response.
i/p:cursor,status
o/p:response
'''
def post_process_function(cursor, status):
	logger.debug(POSTPROCESSING)
	try:		
		logger.info(POSTPROCESSING_COMPLETED)
		return cursor,status
	except Exception as e:
		logger.error(e)
		status["is_ok"] = False
		status["brain_status_instance"][0]["parameters"]["msg"] = BrainStatusCode.BRAIN_STATUS_CODE_INVALID_DATA
		return cursor ,status




