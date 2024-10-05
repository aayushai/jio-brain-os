from google.protobuf.json_format import MessageToDict
from .query import query
import json
from .config import *
import logging as logger
from db.arango.utils.config import *
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
		return None,brain_status

	entity_id = request.entity_id
	entity_type = entity_id.split("/")[0].strip() #entity_type is collection_name

	language_ = request.language
	language = language_.language
	

	alias = request.alias
	canonical_name = request.canonical_name

	_query = query%(entity_id,language,canonical_name,alias,entity_type)

	query_dict["query"] = _query
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

	if "entity_id" in req and "language" in req and "alias" in req and "canonical_name" in req:
		logger.info(VALIDATED)
		return True,None 

	else:
		logger.error("INPUT_PARAMETER_COUNT_ERROR")
		return False,"INPUT_PARAMETER_COUNT_ERROR"

'''
the post_process_function takes the arango response and status as the
input and sets the status and returns the appropritate response.
i/p:cursor,status
o/p:response
'''
def post_process_function(cursor, status):
	logger.debug(POSTPROCESSING)
	print("***")
	print(status)
	try:		
		logger.info(POSTPROCESSING_COMPLETED)
		return cursor, status
	except Exception as e:
		logger.error(e)
		status["is_ok"] = False
		status["brain_status_instance"][0]["parameters"]["msg"] = str(e)
		return None ,status
	